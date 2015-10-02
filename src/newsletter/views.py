from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Hello."
    # Note, you may use request and auth objects right in the template
    # due to context_processors option in TEMPLATES section of settings.py
    if request.user.is_authenticated():
        title = "Hello, {}".format(request.user)
    context = {
        "title": title,
        "user": request.user,
    }

    return render(request, "home.html", context)