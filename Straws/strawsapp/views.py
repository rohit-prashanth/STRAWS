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
from .forms import TableModelForm1,TableModelForm2,TableModelForm3,TableModelForm4,TableModelForm5,TableModelForm6,TableModelForm7,TableModelForm8,TableModelForm9,TableModelForm10
from .models import TableForm1,TablesHistoryDatabase,TableForm2,TableForm3,TableForm4,TableForm5,TableForm6,TableForm7,TableForm8,TableForm9,TableForm10
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
        data1 = TableForm1.objects.last()
        data2 = TableForm2.objects.last()
        data3 = TableForm3.objects.last()
        data4 = TableForm4.objects.last()
        data5 = TableForm5.objects.last()
        data6 = TableForm6.objects.last()
        data7 = TableForm7.objects.last()
        data8 = TableForm8.objects.last()
        data9 = TableForm9.objects.last()
        data10 = TableForm10.objects.last()
        table_form1 = TableModelForm1(instance=data1)
        table_form2 = TableModelForm2(instance=data2)
        table_form3 = TableModelForm3(instance=data3)
        table_form4 = TableModelForm4(instance=data4)
        table_form5 = TableModelForm5(instance=data5)
        table_form6 = TableModelForm6(instance=data6)
        table_form7 = TableModelForm7(instance=data7)
        table_form8 = TableModelForm8(instance=data8)
        table_form9 = TableModelForm9(instance=data9)
        table_form10 = TableModelForm10(instance=data10)
        return render(request,'workers_profile.html',{'form1':table_form1,'form2':table_form2,'form3':table_form3,'form4':table_form4,'form5':table_form5,'form6':table_form6,'form7':table_form7,'form8':table_form8,'form9':table_form9,'form10':table_form10,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,'data7':data7,'data8':data8,'data9':data9,'data10':data10,})
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
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm1(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data1 = TableForm1.objects.last()
            if data1:
                table_form1 = TableModelForm1(instance=data1)
                return render(request, 'workers_profile.html', {'form1': table_form1, 'data1': data1})
            else:
                table_form1 = TableModelForm1()
                return render(request, 'workers_profile.html', {'form1': table_form1})
    else:
        return HttpResponseRedirect('/worker/')

def table2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm2(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data2 = TableForm2.objects.last()
            if data2:
                table_form2 = TableModelForm2(instance=data2)
                return render(request,'workers_profile.html',{'form1':table_form2,'data2':data2})
            else:
                table_form2 = TableModelForm2()
                return render(request, 'workers_profile.html', {'form1': table_form2})
    else:
        return HttpResponseRedirect('/worker/')

def table3(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm3(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data3 = TableForm3.objects.last()
            if data3:
                table_form3 = TableModelForm3(instance=data3)
                return render(request, 'workers_profile.html', {'form3': table_form3, 'data3': data3})
            else:
                table_form3 = TableModelForm3()
                return render(request, 'workers_profile.html', {'form3': table_form3})
    else:
        return HttpResponseRedirect('/worker/')


def table4(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm4(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data4 = TableForm4.objects.last()
            if data4:
                table_form4 = TableModelForm4(instance=data4)
                return render(request, 'workers_profile.html', {'form4': table_form4, 'data4': data4})
            else:
                table_form4 = TableModelForm4()
                return render(request, 'workers_profile.html', {'form4': table_form4})
    else:
        return HttpResponseRedirect('/worker/')


def table5(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm5(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data5 = TableForm5.objects.last()
            if data5:
                table_form5 = TableModelForm5(instance=data5)
                return render(request, 'workers_profile.html', {'form5': table_form5, 'data5': data5})
            else:
                table_form5 = TableModelForm5()
                return render(request, 'workers_profile.html', {'form5': table_form5})
    else:
        return HttpResponseRedirect('/worker/')


def table6(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm6(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data6 = TableForm6.objects.last()
            if data6:
                table_form6 = TableModelForm6(instance=data6)
                return render(request, 'workers_profile.html', {'form6': table_form6, 'data6': data6})
            else:
                table_form6 = TableModelForm6()
                return render(request, 'workers_profile.html', {'form6': table_form6})
    else:
        return HttpResponseRedirect('/worker/')

def table7(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm7(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data7 = TableForm7.objects.last()
            if data7:
                table_form7 = TableModelForm7(instance=data7)
                return render(request, 'workers_profile.html', {'form7': table_form7, 'data7': data7})
            else:
                table_form7 = TableModelForm7()
                return render(request, 'workers_profile.html', {'form7': table_form7})
    else:
        return HttpResponseRedirect('/worker/')


def table8(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm8(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data8 = TableForm8.objects.last()
            if data8:
                table_form8 = TableModelForm8(instance=data8)
                return render(request, 'workers_profile.html', {'form8': table_form8, 'data8': data8})
            else:
                table_form8 = TableModelForm8()
                return render(request, 'workers_profile.html', {'form8': table_form8})
    else:
        return HttpResponseRedirect('/worker/')


def table9(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm9(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data9 = TableForm9.objects.last()
            if data9:
                table_form9 = TableModelForm9(instance=data9)
                return render(request, 'workers_profile.html', {'form9': table_form9, 'data9': data9})
            else:
                table_form9 = TableModelForm9()
                return render(request, 'workers_profile.html', {'form9': table_form9})
    else:
        return HttpResponseRedirect('/worker/')


def table10(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            table_form = TableModelForm10(request.POST)
            if table_form.is_valid():
                table_form.save()
                return HttpResponseRedirect('/workers_profile/')
            else:
                return HttpResponseRedirect('/workers_profile/')

        else:
            data10 = TableForm10.objects.last()
            if data10:
                table_form10 = TableModelForm10(instance=data10)
                return render(request, 'workers_profile.html', {'form10': table_form10, 'data10': data10})
            else:
                table_form10 = TableModelForm10()
                return render(request, 'workers_profile.html', {'form10': table_form10})
    else:
        return HttpResponseRedirect('/worker/')

def clear(request,db):
    table_list=['TableForm1','TableForm2','TableForm3','TableForm4','TableForm5','TableForm6','TableForm7','TableForm8','TableForm9','TableForm10']
    try:
        if table_list[0] == db :
            TableForm1.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[1] == db :
            TableForm2.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[2] == db :
            TableForm3.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[3] == db :
            TableForm4.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[4] == db :
            TableForm5.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[5] == db :
            TableForm6.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[6] == db :
            TableForm7.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[7] == db :
            TableForm8.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[8] == db :
            TableForm9.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[9] == db :
            TableForm10.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
    except:
        messages.info(request, 'No Data Exists In the Form')
        return HttpResponseRedirect('/workers_profile/')



def checkout(request,db):
    table_list=['TableForm1','TableForm2','TableForm3','TableForm4','TableForm5','TableForm6','TableForm7','TableForm8','TableForm9','TableForm10']
    print(db,type(db))
    try:
        if table_list[0] == db :
            d1 = TableForm1.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm1.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[1] == db :
            d1 = TableForm2.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm2.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[2] == db :
            d1 = TableForm3.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm3.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[3] == db :
            d1 = TableForm4.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm4.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[4] == db :
            d1 = TableForm5.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm5.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[5] == db :
            d1 = TableForm6.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm6.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[6] == db :
            d1 = TableForm7.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm7.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[7] == db :
            d1 = TableForm8.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm8.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[8] == db :
            d1 = TableForm9.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm9.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
        if table_list[9] == db :
            d1 = TableForm10.objects.last()
            data = TablesHistoryDatabase(name= d1.name,mobile_number=d1.mobile_number,items=d1.items,total_amount=d1.total_amount,payment_mode=d1.payment_mode)
            data.save()
            TableForm10.objects.all().delete()
            return HttpResponseRedirect('/workers_profile/')
    except:
        messages.info(request,'No Data Exists In the Form')
        return HttpResponseRedirect('/workers_profile/')

