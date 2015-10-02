from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp
# Register your models here.
# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/


class SignUpAdmin(admin.ModelAdmin):
    # This is how we change the way model is displayed in the admin menu
    list_display = ["__unicode__", "timestamp", "updated"]

    form = SignUpForm
    # class Meta:
    #     model = SignUp


admin.site.register(SignUp, SignUpAdmin)