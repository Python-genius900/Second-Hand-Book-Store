"""Online_Grocery_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('signup',Signup,name="signup"),
	path('about/',About,name='about'),
	path('contact/',Contact,name='contact'),
    path('login',Login,name="login"),
    path('logout/',Logout,name="logout"),
    path('view_user',View_user,name="view_user"),
    path('add_product',Add_Product,name="add_product"),
    path('view_feedback', View_feedback, name='view_feedback'),
    path('view_product/<int:pid>', View_prodcut, name='view_product'),
    path('admin_view_product', Admin_View_product, name='admin_view_product'),
    path('login_admin',Admin_Login,name="login_admin"),
    path('admin_viewBooking', Admin_View_Booking, name='admin_viewBooking'),
    path('view_categary/', View_Categary, name='view_categary'),
    path('add_categary', Add_Categary, name='add_categary'),
    path('add_cart/<int:pid>', Add_Cart, name='add_cart'),
    path('delete_product/<int:pid>', delete_product, name='delete_product'),
    path('delete_user/<int:pid>', delete_user, name='delete_user'),
    path('delete_feedback/<int:pid>', delete_feedback, name='delete_feedback'),
    path('cart', view_cart, name='cart'),
    path('payment(?P<total>[0-9]+)', payment, name='payment'),
    path('delete_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_booking, name='delete_booking'),
    path('delete_admin_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_admin_booking, name='delete_admin_booking'),
    path('booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)', booking_detail, name='booking_detail'),
    path('admin_booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)/(?P<uid>[0-9]+)', admin_booking_detail, name='admin_booking_detail'),
    path('Edit_status/(?P<str:pid>)/(?P<bid>[0-9]+)', Edit_status, name='Edit_status'),
    path('remove_cart/<int:pid>', remove_cart, name='remove_cart'),
    path('booking(?P<str:pid>)', Booking_order, name="booking"),
    path('view_booking', View_Booking, name='view_booking'),
    path('profile', profile, name='profile'),
    path('edit_profile', Edit_profile, name='edit_profile'),
    path('delete_category/<int:pid>', delete_category, name='delete_category'),
    path('admin-home/', Admin_Home, name='admin_home'),
    path('change_password', Change_Password, name="change_password"),
    path('send_feedback/<int:pid>', Feedback, name='send_feedback'),
    path('product_detail/<int:pid>', product_detail, name="product_detail"),
    path('edit_product/<int:pid>', edit_product, name="edit_product"),
    path('sold_product/<int:pid>', sold_product, name="sold_product"),
    path('sold_product_admin/<int:pid>', sold_product_admin, name="sold_product_admin"),
    path('my_product/', my_product, name="my_product"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
