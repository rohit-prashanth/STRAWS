"""Straws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from strawsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('shop_admin/',views.shop_admin,name='shop_admin'),
    path('worker/',views.worker,name='worker'),
    path('workers_profile/',views.workers_profile,name='workers_profile'),
    path('admin_profile/',views.admin_profile,name='admin_profile'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('w_signupform/',views.w_signupform,name='w_signupform'),
    path('update_table/<str:item>/',views.update_table,name='update_table'),
    path('table1/',views.table1,name='table1'),
    path('table2/',views.table2,name='table2'),
    path('table3/',views.table3,name='table3'),
    path('table4/',views.table4,name='table4'),
    path('table5/',views.table5,name='table5'),
    path('table6/',views.table6,name='table6'),
    path('table7/',views.table7,name='table7'),
    path('table8/',views.table8,name='table8'),
    path('table9/',views.table9,name='table9'),
    path('table10/',views.table10,name='table10'),
    path('checkout/<str:db>/',views.checkout,name='checkout'),
    path('clear/<str:db>/',views.clear,name='clear'),

]
