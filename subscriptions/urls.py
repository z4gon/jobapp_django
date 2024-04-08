from django.urls import path
from subscriptions import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscribe/manual', views.subscribe_manual, name='subscribe_manual'),
    path('subscribe/success', views.subscription_success, name='subscription_success'),
]
