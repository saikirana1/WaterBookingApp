from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import WaterBooking
from .forms import WaterBookingForm

# User Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('waterbook:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Signup
def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('waterbook:login')
        else:
            messages.error(request, "Error creating account. Please check the details and try again.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('waterbook:login')

# Supplier Login
def supplier_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            supplier = authenticate(request, username=username, password=password)
            if supplier is not None and supplier.is_staff:
                login(request, supplier)
                messages.success(request, "Supplier login successful!")
                return redirect('waterbook:supplier_orders')
            else:
                messages.error(request, "Invalid supplier credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'supplier_login.html', {'form': form})

# Supplier Signup
def supplier_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.is_staff = True
            supplier.save()
            messages.success(request, "Supplier account created successfully! You can now log in.")
            return redirect('waterbook:supplier_login')
        else:
            messages.error(request, "Error creating supplier account. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'supplier_signup.html', {'form': form})

# Supplier Logout
def supplier_logout(request):
    logout(request)
    messages.success(request, "Supplier logged out successfully!")
    return redirect('waterbook:supplier_login')

# Book Water
@login_required
def book_water(request):
    if request.method == "POST":
        form = WaterBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Water booking successful!")
            return redirect('waterbook:home')
    else:
        form = WaterBookingForm()
    return render(request, 'book_water.html', {'form': form})

# Home
@login_required(login_url='waterbook:login')
def home(request):
    bookings = WaterBooking.objects.filter(user=request.user)
    return render(request, 'home.html', {'bookings': bookings, 'user_id': request.user.id})

# My Bookings
@login_required
def my_bookings(request):
    bookings = WaterBooking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

# Supplier Orders
def is_supplier(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='waterbook:supplier_login')
@user_passes_test(is_supplier, login_url='waterbook:supplier_login')
def supplier_orders(request):
    bookings = WaterBooking.objects.all()
    return render(request, 'supplier_orders.html', {'bookings': bookings})

# Update Delivery Status
def update_delivery_status(request, booking_id):
    booking = get_object_or_404(WaterBooking, id=booking_id)
    booking.delivery_status = 'DELIVERED'
    booking.save()
    return redirect('waterbook:supplier_orders')

# Static Pages
def supplier_home(request):
    return render(request, 'supplier_home.html')

def home2(request):
    return render(request, 'home2.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')
