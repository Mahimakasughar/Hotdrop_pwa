from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('categories/', views.categories, name='categories'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-orders/', views.manage_orders, name='manage_orders'),
    path('logout/',views.logout_view, name='logout'),
    path('admin-orders/', views.admin_orders, name='admin_orders'),
    path('vendor-login/', views.vendor_login, name='vendor_login'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor-logout/', views.vendor_logout, name='vendor_logout'),
    path('vendor-register/', views.vendor_register, name='vendor_register'),
]