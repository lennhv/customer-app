from django.urls import path
from .views import CustomerView, CreateCustomerView

urlpatterns = [
    path('', CustomerView.as_view(), name='customer-view'),
    path('create_customer', CreateCustomerView.as_view(),
         name='customer-create-view'),
]
