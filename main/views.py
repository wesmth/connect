from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    print('A página --Main-- foi acessada.')
    context = {}
    return render(request,'main/index.html',context)