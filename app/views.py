from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import UserSignUpForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def userSignUpView(request):
    fm=UserSignUpForm()
    if request.method == 'POST':
        fm=UserSignUpForm(data=request.POST)
        if fm.is_valid():
            # fm.save()
            User.objects.create(first_name=fm.cleaned_data['first_name'],
                                last_name=fm.cleaned_data['last_name'],
                                email=fm.cleaned_data['email'],
                                username=fm.cleaned_data['username'],
                                password=fm.cleaned_data['password1'])
            
            return redirect('login')
        
    return render(request,'index.html',{'form':fm})

def userLogInView(request):
    fm=UserLoginForm()
    if request.method=='POST':
        fm=UserLoginForm(request.POST)
        if fm.is_valid():
            cleaned_data=fm.cleaned_data
            user=authenticate(**cleaned_data)
            if user:
                if user.is_authenticated:
                    login(request, user)
                    return render(request,'home.html')
            return HttpResponse('Invalid Credintials')

    return render(request,'login.html',{'form':fm})

@csrf_exempt
def userNameValidateView(request):
    import json
    data=json.loads(request.body)
    username=data['username']
    if User.objects.filter(username=username).exists():
        return JsonResponse({"user_name_error":"The username is in use"})
    else:
        return JsonResponse({'usertrue':True})
    
@csrf_exempt
def userEmailValidateView(request):
    import json
