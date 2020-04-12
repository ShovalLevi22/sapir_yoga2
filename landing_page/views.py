from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
import uuid

from django.urls import reverse_lazy
from landing_page.forms import UserForm, UserInfoForm
from landing_page.models import UserInfo, User
from django.shortcuts import render, get_object_or_404, redirect
from . main import send_mail

# Create your views here.
class AboutView(View):
    template_name = 'landing_page/about.html'
    form_class = UserForm
    model = UserInfo




def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm()
        if user_form.is_valid():  # and user_info_form.is_valid():
            user = user_form.save()

            user.save()

            info = user_info_form.save(commit=False)

            info.url_id = str(uuid.uuid1()).split('-')[1]
            info.user = user

            info.save()
            registered = True

            send_mail(to=user.email,
                      campaign_json='landing_page/Sapir.json',
                      url_id=info.url_id)
        else:
            print(user_form.errors, user_info_form.errors)


    else:
        user_form = UserForm()
        # user_info_form = UserInfoForm()

    return render(request, 'landing_page/about.html',
                  {'user_form': user_form, 'user_info_form': False, 'registered': registered})


class VideoPageView(TemplateView):
    template_name = 'video_page/video_page.html'

    def get(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # user_id = int(request.POST['id'])
            # user = UserInfo.objects.get(url_id=id)
            user = UserInfo.objects.all().filter(url_id=url_id)[0]  # .get(url_id=url_id)
            user.visits_counter = user.visits_counter + 1
            user.save()

        except User.DoesNotExist:
            return render(request, 'landing_page/about.html')

        return render(request, 'video_page/video_page.html')


class UnsubscribeView(View):
    template_name = 'email_page/unsubscribe.html'

    def get(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # user_id = int(request.POST['id'])
            user = UserInfo.objects.get(url_id=url_id)
            user.unsubscribe = 1
            user.save()

        except User.DoesNotExist:
            return render(request, 'landing_page/about.html')

        return render(request, 'email_page/unsubscribe.html')

    def post(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # url_id = int(request.POST['id'])
            user = UserInfo.objects.all().filter(url_id=url_id)[0]      #.get(url_id=url_id)
            user.unsubscribe = 0
            user.save()

        except User.DoesNotExist as e:
            print(e)
            return render(request, 'landing_page/about.html')
        except:
            return render(request, 'landing_page/about.html')

        return render(request, 'email_page/unsubscribe.html')
