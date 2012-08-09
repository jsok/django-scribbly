from customer.models import Customer

def get_current_customer(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    return customer

