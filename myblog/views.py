from django.shortcuts import render, get_object_or_404
from django.views import View
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import CustomUser
from .forms import SignUpForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/index.html'
        )

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer