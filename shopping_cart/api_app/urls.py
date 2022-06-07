from django.urls import path
from rest_framework.urls import urlpatterns

from .views import CarItemViews

urlpatterns=[
    path('cart-Item/', CarItemViews.as_view()),
    path('cart-Item/<int:id>', CarItemViews.as_view())

]