from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from rest_framework import viewsets
from .models import Iha, Kiralama
from .serializers import IhaSerializer, KiralamaSerializer

class IhaViewSet(viewsets.ModelViewSet):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer

class KiralamaViewSet(viewsets.ModelViewSet):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer
    
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('anasayfa')  
        else:
            return render(request, 'login.html', {'form': form, 'register_link': True})
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('anasayfa')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'myuser',
#         'PASSWORD': 'mypassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
