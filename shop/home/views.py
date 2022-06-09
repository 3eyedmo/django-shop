from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic


def home(request):
    return render(request, "home/index.html")



def test(request):
    print(request.user)
    print(request.POST)
    
    return JsonResponse(data={"name":"mohammad"})