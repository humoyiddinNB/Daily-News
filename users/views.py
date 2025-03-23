from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import RegisterForm, LoginForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form' : form })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
        return render(request, 'users/register.html', {'form' : form})



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Foydalanuvchi nomi yoki parol noto\'g\'ri.')
        return render(request, 'users/login.html', {'form': form})


class UpdateView(View):
    def get(self, request):
        user = request.user
        form = RegisterForm(instance=user)
        return render(request, 'users/update.html', {'form': form})

    def post(self, request):
        user = request.user
        form = RegisterForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)

            user.save()

            if password:
                login(request, user)

            return redirect('profile')

        return render(request, 'users/update.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'users/profile.html', {'user':user})



class LogOutView(View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        if request.POST.get('confirm') == 'yes':
            logout(request)
            return redirect('login')
        return redirect('profile')

