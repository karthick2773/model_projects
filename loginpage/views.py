from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    return render(request,'loginpage/login.html') 

class login_info_collect(View):
    def post(self,request):
        user_name=request.POST.get('user_name')
        password=request.POST.get('user_password')
        print('username: ',user_name,'password:',password)
        return HttpResponse("Succeed")
    