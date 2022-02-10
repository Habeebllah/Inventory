from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import resolve_url, render, redirect, get_object_or_404
from django.views import View
from django.shortcuts import redirect
from inventory.decorators import *
from base.forms.login_form import LoginForm
from base.forms.signupform import CustomerSignUpForm, SalesSignUpForm
from base.models.users import User
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages



# User login view
""" class UserLoginView2(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    redirect_authenticated_user = False
    template_name = 'auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/dashboard/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(UserLoginView, self).form_valid(form)
 """


class SalesSignUpView(CreateView):
    model = User
    form_class = SalesSignUpForm
    template_name = 'users/createsales.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        messages.success(self.request, 'You Created New Sales Person')
        if self.request.user.is_staff:
            messages.success(self.request, 'You Created New Sales Customer')
            return redirect('dashboard')
        else:
            messages.success(self.request, 'You Created New Sales Customer')
            return redirect('sales-dashboard')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/createcustomer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #dj_login(self.request, user)
        if self.request.user.is_staff:
            messages.success(self.request, 'You Created New Sales Customer')
            return redirect('dashboard')
        else:
            messages.success(self.request, 'You Created New Sales Customer')
            return redirect('dashboard')



def UserLoginView(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if form.is_valid():
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                dj_login(request, user)

                if request.user.is_sales:
                    return redirect('sales-dashboard')
                elif request.user.is_customer:
                    return redirect('buyer:buyer-dashbooard')
                elif request.user.is_superuser:
                    return redirect('dashboard')

        else:
            args = {'form': form}
            return render(request, 'auth/login.html', args)

    else:
        form = AuthenticationForm

    args = {'form': form}
    return render(request, 'auth/login.html', args)


# Logout view
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
