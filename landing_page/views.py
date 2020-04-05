from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from landing_page.forms import UserForm, UserInfoForm
from landing_page.models import UserInfo
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
class AboutView(TemplateView):
    template_name = 'landing_page/about.html'
    form_class = UserForm
    model = UserInfo


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.save()

            info = user_info_form.save(commit=False)
            info.user = user
            info.save()

        else:
            print(user_form.errors)

        registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    return render(request, 'landing_page/about.html', {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered})