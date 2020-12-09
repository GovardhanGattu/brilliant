"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from study import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('selectpage/',views.selectpage,name='selectpage'),
    path('staffselect/',views.staffselect,name='staffselect'),
    path('trash/<int:id>',views.trash,name="trash"),
    path("management/",views.management,name='management'),
    path('stafftrash/<int:id>',views.stafftrash,name="stafftrash"),
    path('newstaff/',views.newstaff,name='newstaff'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
        name='password_change'),

     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),


    
    path('T6V/',views.T6V,name='T6V'),
    path('tl6/',views.tl6,name='tl6'),
    path('fT6V/',views.fT6V,name='fT6V'),
    
    path('H6V/',views.H6V,name='H6V'),
    path('hl6/',views.hl6,name='hl6'),
    path('fH6V/',views.fH6V,name='fH6V'),
    
    path('E6V/',views.E6V,name='E6V'),
    path('el6/',views.el6,name='el6'),
    path('fE6V/',views.fE6V,name='fE6V'),

    path('M6V/',views.M6V,name='M6V'),
    path('ml6/',views.ml6,name='ml6'),
    path('fM6V/',views.fM6V,name='fM6V'),

    path('S6V/',views.S6V,name='S6V'),
    path('sl6/',views.sl6,name='sl6'),
    path('fS6V/',views.fS6V,name='fS6V'),

    path('Sc6V/',views.Sc6V,name='Sc6V'),
    path('scl6/',views.scl6,name='scl6'),
    path('fSc6V/',views.fSc6V,name='fSc6V'),

]

