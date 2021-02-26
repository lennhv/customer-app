from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Customer
from .forms import CustomerForm


class CustomerView(ListView):
    model = Customer
    paginate_by = 2
    template_name = 'customers/index.html'


class CreateCustomerView(CreateView):
    template_name = 'customers/create_user_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-view')
