
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userManagement.forms import UserForm
from userManagement.models import CustomUser


class UserCreateView(CreateView):
    template_name = 'userManagement/create_user.html'
    model = CustomUser
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.email = new_user.email.lower()

        new_user.first_name = new_user.first_name.lower()
        new_user.last_name = new_user.last_name.lower()
        new_user.nickname = new_user.nickname.title()


        new_user.save()
        return redirect('login')
