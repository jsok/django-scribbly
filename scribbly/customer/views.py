from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse, HttpResponseRedirect

from customer.models import Customer

def login(request, template_name="scribbly/customer/login.html"):
    login_form = AuthenticationForm()
    login_form.fields["username"].label = u"Email"

    if request.POST.get("action") == "login":
        login_form = AuthenticationForm(data=request.POST)
        login_form.fields["username"].label = u"Email"

        if login_form.is_valid():
            from django.contrib.auth import login
            login(request, login_form.get_user())
            response = HttpResponseRedirect(request.POST.get("next"))
            return response

    # Get next_url
    next_url = request.REQUEST.get("next")
    if next_url is None:
        next_url = request.META.get("HTTP_REFERER")
    if next_url is None:
        next_url = reverse("customer.views.account")

    try:
        login_form_errors = login_form.errors["__all__"]
    except KeyError:
        login_form_errors = None

    return render_to_response(template_name, RequestContext(request, {
        "login_form": login_form,
        "login_form_errors": login_form_errors,
        "next_url": next_url,
        }))

def logout(request):
    if isinstance(request.user, AnonymousUser):
        return HttpResponse("You are not currently logged in.")

    # Clear the session on logout
    request.session.flush()

    from django.contrib.auth import logout
    logout(request)
    return HttpResponse("You have been logged out.")

@login_required
def account(request):
    customer = Customer.objects.get(user=request.user)

    return HttpResponse("You are logged in as %s" % customer)
