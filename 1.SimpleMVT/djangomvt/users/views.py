from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm

from .utils import compress_image
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                if 'image' in request.FILES:
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(300,300))
                    user.image_small.save(image_name, optimized_image, save=False)
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(800,800))
                    user.image_medium.save(image_name, optimized_image, save=False)
                    optimized_image, image_name = compress_image(request.FILES['image'], size=(1200,1200))
                    user.image_large.save(image_name, optimized_image, save=False)
                user.save()
                return redirect('polls:index')
            except Exception as e:
                messages.error(request, f'Помилка при реєстрації: {str(e)}')
        else:
            messages.success(request, 'Виправте помилки в формі')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
 


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # змініть на вашу домашню сторінку
        else:
            messages.error(request, 'Невірний логін або пароль')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})    


def logout_view(request):
    logout(request)
    return redirect('/')  # або інша ваша домашня сторінка