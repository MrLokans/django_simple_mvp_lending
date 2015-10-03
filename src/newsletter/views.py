from django.shortcuts import render

from .forms import SignUpForm
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