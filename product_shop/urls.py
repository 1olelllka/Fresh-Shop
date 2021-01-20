from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('search/', views.Search.as_view(), name='search'),
    path('user/register/', views.registration, name='register'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout'),
    path('product/<slug:slug>/', views.product_detail, name='product'),
    path('category/<slug:slug>/', views.ShowCategories.as_view(), name='category'),
    path('add_to_cart/<slug:product_slug>/', views.add_to_cart, name='add_cart'),
    path('remove_from_cart/<slug:product_slug>/',views.remove_from_cart, name='remove_cart')
]