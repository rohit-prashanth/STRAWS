from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import worker_signup_form
from .models import StoresList
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def shop_admin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    if user.is_staff:
                        login(request, user)
                        return HttpResponseRedirect('/admin_profile/')
                    else:
                        messages.warning(request,'You are not authorised to login to Admin Page')
                        return HttpResponseRedirect('/shop_admin/')

        else:
            shop_admin_form = AuthenticationForm()
            return render(request,'shop_admin.html',{'sa_form':shop_admin_form})
    else:
        return HttpResponseRedirect('/admin_profile/')

def worker(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    to = 'rohitprshnth09@gmail.com'
                    content = f'Mr {uname} logged in as Worker'
                    print(to, content)
                    send_mail(
                        "testing",
                        content,
                        settings.EMAIL_HOST_USER,
                        [to]

                    )
                    return HttpResponseRedirect('/workers_profile/')
        else:
            worker_form = AuthenticationForm()
            return render(request,'worker.html',{'w_form':worker_form})
    else:
        return HttpResponseRedirect('/workers_profile/')

def workers_profile(request):
    if request.user.is_authenticated:
        return render(request,'workers_profile.html')
    else:
        return HttpResponseRedirect('/worker/')

def admin_profile(request):
    if request.user.is_authenticated:
        return render(request,'admin_profile.html')
    else:
        return HttpResponseRedirect('/shop_admin/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def w_signupform(request):
    if request.method == 'POST':
        form = worker_signup_form(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            sl = StoresList.objects.filter(manager_id=request.user)
            user_name = f'{f_name}_{sl.store_code}'
            form.save(commit=False)
            form.username, form.worker_id = user_name
            form.save()
            messages.success(request,'Successfully Created!')
            return HttpResponseRedirect('/w_signupform/')
    else:
        worker_form = worker_signup_form()
        return render(request, 'w_signupform.html', {'w_form': worker_form})

def update_table(request,item):
    pass


def table1(request):
    return render(request,'billing_page.html')
