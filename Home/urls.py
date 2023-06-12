from django.contrib import admin
from django.urls import path, include;
from Home import views;

urlpatterns = [
    path('', views.index, name="Home"),
    path('About',views.About, name="About"),
    path('FAQ',views.FAQ, name="FAQ"),
    path('Login',views.Login, name="Login"),
    path('Sign_up',views.Sign_up, name="SignUp"),
    path('Forget_password',views.Forget_password, name="Forget_password"),
    path('Services',views.Services, name="Services"),
    path('Customer', views.Customer, name='Customer'),
    # path('paytm', views.paytm, name='paytm'),
    # path('Payment', views.Payment, name='Payment'),
    path('Checkout', views.Checkout, name='Checkout'),
     path("handlerequest", views.handlerequest, name="HandleRequest"),
     path("After_Login", views.After_Login, name="After_Login"),
]