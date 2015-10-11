from django.conf import settings

from django.shortcuts import render
from django.core.mail import send_mail



from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
    title = "Hello."
    # Note, you may use request and auth objects right in the template
    # due to context_processors option in TEMPLATES section of settings.py
    # if request.user.is_authenticated():
    #     title = "Hello, {}".format(request.user)
    # print request
    # if request.method == "POST":
    #     print request.POST
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form_instance = form.save(commit=False)
        if not form_instance.full_name:
            form_instance.full_name = "John Galt"
        form_instance.save()
    context = {
        "title": title,
        "user": request.user,
        "form": form,
    }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name =form.cleaned_data.get("full_name")

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourother@email.com']
        contact_message = "{}: {} via {}".format(form_full_name, form_message, form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)


    context = {
        "form": form,
    }
    return render(request, "forms.html", context)