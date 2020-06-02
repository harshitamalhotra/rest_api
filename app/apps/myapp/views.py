from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
from .forms import Newuser

def index(request):
    form=Newuser()


    if request.method=="POST":
        form=Newuser(request.POST)



        if form.is_valid():
            form.save(commit=True)



        else:
            print("ERROR")

    return render(request,'index.html',{"form":form})


class Userlist(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=User.objects.all()
            serial=UserSerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=UserSerializer(data=request.data)
             if (serializer.is_valid()):
                 serializer.save()
                 return Response(serializer.data)
