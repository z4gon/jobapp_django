from django.urls import path
from subscriptions import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscription_success', views.subscription_success, name='subscription_success'),
]
