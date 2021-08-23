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
from .forms import TableModelForm1,TableModelForm2
from .models import TableForm1,TablesHistoryDatabase
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
                    messages.warning(request, 'You are not authorised to login to Admin Page')
                    return HttpResponseRedirect('/shop_admin/')
            else:
                messages.warning(request, 'You are not authorised to login to Admin Page')
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
                    to_1 = 'rohitprshnth09@gmail.com'
                    to_2 = 'sathwik777@gmail.com'
                    content = f'Mr {uname} logged in as Worker'
                    print(to_1, content)
                    print(to_2,content)
                    send_mail(
                        "testing",
                        content,
                        settings.EMAIL_HOST_USER,
                        [to_1,to_2]

                    )
                    return HttpResponseRedirect('/workers_profile/')
                else:
                    worker_form = AuthenticationForm()
                    messages.warning(request, 'You are not authorised to login to Admin Page')
                    return render(request, 'worker.html', {'w_form': worker_form})
            else:
                worker_form = AuthenticationForm()
                messages.warning(request, 'You are not authorised to login to Admin Page')
                return render(request, 'worker.html', {'w_form': worker_form})
        else:
            worker_form = AuthenticationForm()
            return render(request,'worker.html',{'w_form':worker_form})
    else:
        return HttpResponseRedirect('/workers_profile/')

def workers_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm1(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data = TableForm1.objects.first()
            if data:
                table_form1 = TableModelForm1(instance=data)
                #table_form2 = TableModelForm1(instance=data)
                return render(request, 'workers_profile.html', {'form': table_form1,'data':data})
            else:
                table_form1 = TableModelForm1()
                table_form2 = TableModelForm2()
                return render(request,'workers_profile.html',{'form1':table_form1,'form1':table_form2})
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
    else:
        worker_form = worker_signup_form()
        return render(request, 'w_signupform.html', {'w_form': worker_form})

def update_table(request,item):
    pass


def table1(request):
    return render(request,'billing_page.html')

def checkout(request,db):
    table_list=['TableForm1']
    print(db,type(db))
    try:
        if table_list[0] == db :
            d1 = TableForm1.objects.first()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm1.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
    except:
        messages.info(request,'No Data Exists In the Form')
        return HttpResponseRedirect('/workers_profile/')

