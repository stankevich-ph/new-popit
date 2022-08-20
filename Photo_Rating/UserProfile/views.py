from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import UpdateView
from UserProfile.models import UserProfile
from django.shortcuts import render, redirect


class add_user_settings(TemplateView):
    template_name = 'UserProfile/UserProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

def UpdateUserInformation (request, id):
    print('Привет', request.POST)
    if request.method == "POST":
        model = User.objects.get(id=id)
        model.username = request.POST['username']
        model.first_name = request.POST['first_name']
        model.last_name = request.POST['last_name']
        model.email = request.POST['email']
        userprofilemodel = UserProfile.objects.get(user_id=id)
        userprofilemodel.Patronymic = request.POST['Patronymic']
        userprofilemodel.Date_of_birth = request.POST['Date_of_birth']
        userprofilemodel.Avatar = request.POST['Avatar']
        model.save()
        userprofilemodel.save()
    else:
        model = User.objects.get(id=id)
        userprofilemodel = UserProfile.objects.get(user_id=id)
    sites = 'UserProfile/Edit.html'
    return render (request, sites, {'form': model, 'userprofilemodel':userprofilemodel})

def photographers_view (request):
    model = UserProfile.objects.select_related('user').all()
    sites = 'UserProfile/photographers.html'
    print('Hello', model)
    return render(request, sites, context={'model':model})

class photo_class(ListView):
    model = User

    template_name = 'UserProfile/photographers.html'
    def get_context_data(self, **kwargs):
        ctx = super(photo_class, self).get_context_data(**kwargs)
        ctx['polls'] = UserProfile.objects.all()
        print('Hello',ctx)
        return ctx

    def get_queryset(self):
        return User.objects.all()
