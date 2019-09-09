from django.shortcuts import render
from basicapp.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basicapp:login'))


def register(request):
    if(request.method=="POST"):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()     
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return HttpResponseRedirect(reverse('basicapp:login'))
        else:
            print(user_form.errors,profile_form.errors) 
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()     
        return render(request,'basicapp/registration.html',{'user_form':user_form,'profile_form':profile_form}) 

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('basicapp:user_dashboard'))
        else:
            return render(request,'basicapp/login.html',{'login':False})
    else:
        return render(request, 'basicapp/login.html', {'login':True})
