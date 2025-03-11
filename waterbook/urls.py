from django.urls import path
from .views import user_login, user_signup, user_logout
from waterbook import views

app_name = 'waterbook'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('supplier/login/', views.supplier_login, name='supplier_login'),
    path('supplier/signup/', views.supplier_signup, name='supplier_signup'),
    path('supplier/logout/', views.supplier_logout, name='supplier_logout'),
    path('home/', views.home2, name='home2'), 
   
    path('j/', views.home, name='home'),
    path('book/', views.book_water, name='book_water'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('supplier/orders/', views.supplier_orders, name='supplier_orders'),
    
    path('supplier/update-delivery-status/<int:booking_id>/', views.update_delivery_status, name='update_delivery_status'),
    path('supplier/home/', views.supplier_home, name='supplier_home'),
    
     path('about-us/', views.about_us, name='about_us'),  
    path('contact-us/', views.contact_us, name='contact_us'), 
 
]


