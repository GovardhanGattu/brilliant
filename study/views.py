from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import *
from study.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	form=UserForm()
	if request.method == "POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			group = Group.objects.get(name='student')
			user.groups.add(group)
			messages.success(request,'Account created as '+ username)
			return redirect('login')
	context={"form":form}
	return render(request,'register.html',context)

def loginpage(request):
	if request.method=="POST":
		username = request.POST.get('username')
		password= request.POST.get('password')

		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('staffselect')
		else:
			messages.info(request,"username or password is incorrect")
	return render(request,'login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def trash(request,id):
	data=T6M.objects.get(id=id)
	data.delete()
	# return HttpResponse("Data Deleted Sucessfully...!!!")
	return redirect('fT6V')


@login_required(login_url='login')
def tl6(request):
	form=Tl6form()
	if request.method=="POST":
		data=Tl6form(request.POST)
		data.save()
		if True:
			return redirect('fT6V')
	return render(request,'staffselect/tl6.html',{"form":form})


@login_required(login_url='login')
def hl6(request):
	form=Hl6form()
	if request.method=="POST":
		data=Hl6form(request.POST)
		data.save()
		if True:
			return redirect('fH6V')
	return render(request,'staffselect/hl6.html',{"form":form})


@login_required(login_url='login')
def el6(request):
	form=El6form()
	if request.method=="POST":
		data=El6form(request.POST)
		data.save()
		if True:
			return redirect('fE6V')
	return render(request,'staffselect/el6.html',{"form":form})


@login_required(login_url='login')
def ml6(request):
	form=Ml6form()
	if request.method=="POST":
		data=Ml6form(request.POST)
		data.save()
		if True:
			return redirect('fM6V')
	return render(request,'staffselect/ml6.html',{"form":form})


@login_required(login_url='login')
def sl6(request):
	form=Sl6form()
	if request.method=="POST":
		data=Sl6form(request.POST)
		data.save()
		if True:
			return redirect('fS6V')
	return render(request,'staffselect/sl6.html',{"form":form})


@login_required(login_url='login')
def scl6(request):
	form=Scl6form()
	if request.method=="POST":
		data=Scl6form(request.POST)
		data.save()
		if True:
			return redirect('fSc6V')
	return render(request,'staffselect/scl6.html',{"form":form})





@login_required(login_url='login')
def T6V(request):
	obj=T6M.objects.all()
	return render(request,'select/class6/telugu.html',{"obj":obj})
@login_required(login_url='login')	
def fT6V(request):
	obj=T6M.objects.all()
	return render(request,'staffselect/class6/telugu.html',{"obj":obj})

@login_required(login_url='login')
def H6V(request):
	obj=H6M.objects.all()
	return render(request,'select/class6/hindi.html',{"obj":obj})
@login_required(login_url='login')	
def fH6V(request):
	obj=H6M.objects.all()
	return render(request,'staffselect/class6/hindi.html',{"obj":obj})
@login_required(login_url='login')
def E6V(request):
	obj=E6M.objects.all()
	return render(request,'select/class6/english.html',{"obj":obj})
@login_required(login_url='login')	
def fE6V(request):
	obj=E6M.objects.all()
	return render(request,'staffselect/class6/english.html',{"obj":obj})
@login_required(login_url='login')
def M6V(request):
	obj=M6M.objects.all()
	return render(request,'select/class6/maths.html',{"obj":obj})
@login_required(login_url='login')
def fM6V(request):
	obj=M6M.objects.all()
	return render(request,'staffselect/class6/maths.html',{"obj":obj})
@login_required(login_url='login')
def S6V(request):
	obj=S6M.objects.all()
	return render(request,'select/class6/science.html',{"obj":obj})
@login_required(login_url='login')
def fS6V(request):
	obj=S6M.objects.all()
	return render(request,'staffselect/class6/science.html',{"obj":obj})
@login_required(login_url='login')
def Sc6V(request):
	obj=Sc6M.objects.all()
	return render(request,'select/class6/social.html',{"obj":obj})
@login_required(login_url='login')
def fSc6V(request):
	obj=Sc6M.objects.all()
	return render(request,'staffselect/class6/social.html',{"obj":obj})




@login_required(login_url='login')

def selectpage(request):
	form=Selectform()
	if request.method=="POST":
		Class=request.POST.get('Class')
		Subject=request.POST.get('Subject')
		if Class=="VI class" and Subject=='Telugu':
			return redirect('T6V')
		elif Class=="VI class" and Subject=='Hindi':
			return redirect('H6V')
		elif Class=="VI class" and Subject=='English':
			return redirect('E6V')
		elif Class=="VI class" and Subject=='Maths':
			return redirect('M6V')
		elif Class=="VI class" and Subject=='Science':
			return redirect('S6V')
		elif Class=="VI class" and Subject=='Social':
			return redirect('Sc6V')
		elif Class=="VII class" and Subject=='Telugu':
			return render(request,'select/class7/telugu.html')
		elif Class=="VII class" and Subject=='Hindi':
			return render(request,'select/class7/hindi.html')
		elif Class=="VII class" and Subject=='English':
			return render(request,'select/class7/english.html')
		elif Class=="VII class" and Subject=='Maths':
			return render(request,'select/class7/maths.html')
		elif Class=="VII class" and Subject=='Science':
			return render(request,'select/class7/science.html')
		elif Class=="VII class" and Subject=='Social':
			return render(request,'select/class7/social.html')
		elif Class=="VIII class" and Subject=='Telugu':
			return render(request,'select/class8/telugu.html')
		elif Class=="VIII class" and Subject=='Hindi':
			return render(request,'select/class8/hindi.html')
		elif Class=="VIII class" and Subject=='English':
			return render(request,'select/class8/english.html')
		elif Class=="VIII class" and Subject=='Maths':
			return render(request,'select/class8/maths.html')
		elif Class=="VIII class" and Subject=='Science':
			return render(request,'select/class8/science.html')
		elif Class=="VIII class" and Subject=='Social':
			return render(request,'select/class8/social.html')
		elif Class=="IX class" and Subject=='Telugu':
			return render(request,'select/class9/telugu.html')
		elif Class=="IX class" and Subject=='Hindi':
			return render(request,'select/class9/hindi.html')
		elif Class=="IX class" and Subject=='English':
			return render(request,'select/class9/english.html')
		elif Class=="IX class" and Subject=='Maths':
			return render(request,'select/class9/maths.html')
		elif Class=="IX class" and Subject=='Science':
			return render(request,'select/class9/science.html')
		elif Class=="IX class" and Subject=='Social':
			return render(request,'select/class9/social.html')
		elif Class=="X class" and Subject=='Telugu':
			return render(request,'select/class10/telugu.html')
		elif Class=="X class" and Subject=='Hindi':
			return render(request,'select/class10/hindi.html')
		elif Class=="X class" and Subject=='English':
			return render(request,'select/class10/english.html')
		elif Class=="X class" and Subject=='Maths':
			return render(request,'select/class10/maths.html')
		elif Class=="X class" and Subject=='Science':
			return render(request,'select/class10/science.html')
		elif Class=="X class" and Subject=='Social':
			return render(request,'select/class10/social.html')

	return render(request,'selectpage.html',{"form":form})



@login_required(login_url='login')
@admin_only
def staffselect(request):
	form=Selectform()
	if request.method=="POST":
		Class=request.POST.get('Class')
		Subject=request.POST.get('Subject')
		if Class=="VI class" and Subject=='Telugu':
			return redirect("fT6V")
		elif Class=="VI class" and Subject=='Hindi':
			return redirect('fH6V')
		elif Class=="VI class" and Subject=='English':
			return redirect('fE6V')
		elif Class=="VI class" and Subject=='Maths':
			return redirect('fM6V')
		elif Class=="VI class" and Subject=='Science':
			return redirect('fS6V')
		elif Class=="VI class" and Subject=='Social':
			return redirect('fSc6V')
		elif Class=="VII class" and Subject=='Telugu':
			return render(request,'staffselect/class7/telugu.html')
		elif Class=="VII class" and Subject=='Hindi':
			return render(request,'staffselect/class7/hindi.html')
		elif Class=="VII class" and Subject=='English':
			return render(request,'staffselect/class7/english.html')
		elif Class=="VII class" and Subject=='Maths':
			return render(request,'staffselect/class7/maths.html')
		elif Class=="VII class" and Subject=='Science':
			return render(request,'staffselect/class7/science.html')
		elif Class=="VII class" and Subject=='Social':
			return render(request,'staffselect/class7/social.html')
		elif Class=="VIII class" and Subject=='Telugu':
			return render(request,'staffselect/class8/telugu.html')
		elif Class=="VIII class" and Subject=='Hindi':
			return render(request,'staffselect/class8/hindi.html')
		elif Class=="VIII class" and Subject=='English':
			return render(request,'staffselect/class8/english.html')
		elif Class=="VIII class" and Subject=='Maths':
			return render(request,'staffselect/class8/maths.html')
		elif Class=="VIII class" and Subject=='Science':
			return render(request,'staffselect/class8/science.html')
		elif Class=="VIII class" and Subject=='Social':
			return render(request,'staffselect/class8/social.html')
		elif Class=="IX class" and Subject=='Telugu':
			return render(request,'staffselect/class9/telugu.html')
		elif Class=="IX class" and Subject=='Hindi':
			return render(request,'staffselect/class9/hindi.html')
		elif Class=="IX class" and Subject=='English':
			return render(request,'staffselect/class9/english.html')
		elif Class=="IX class" and Subject=='Maths':
			return render(request,'staffselect/class9/maths.html')
		elif Class=="IX class" and Subject=='Science':
			return render(request,'staffselect/class9/science.html')
		elif Class=="IX class" and Subject=='Social':
			return render(request,'staffselect/class9/social.html')
		elif Class=="X class" and Subject=='Telugu':
			return render(request,'staffselect/class10/telugu.html')
		elif Class=="X class" and Subject=='Hindi':
			return render(request,'staffselect/class10/hindi.html')
		elif Class=="X class" and Subject=='English':
			return render(request,'staffselect/class10/english.html')
		elif Class=="X class" and Subject=='Maths':
			return render(request,'staffselect/class10/maths.html')
		elif Class=="X class" and Subject=='Science':
			return render(request,'staffselect/class10/science.html')
		elif Class=="X class" and Subject=='Social':
			return render(request,'staffselect/class10/social.html')
		
	return render(request,"staffselect/select.html",{"form":form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['management'])

def management(request):
	data =  User.objects.all()
	return render(request,'manage.html',{'data':data})
@login_required(login_url='login')
@allowed_users(allowed_roles=['management'])
def stafftrash(request,id):
	data = User.objects.get(id=id)
	data.delete()
	return redirect('management')


@login_required(login_url='login')
@allowed_users(allowed_roles=['management'])
def newstaff(request):
	form = StaffForm()
	if request.method == 'POST':
		form = StaffForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='staff')
			user.groups.add(group)
			return redirect('management')
	return render(request,'newstaff.html',{"form":form})












































































































































































































































































































































































































































































	