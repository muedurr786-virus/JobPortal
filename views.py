from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registerpage(req):
    
    if req.method == "POST":
        form =CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Account Created Successfully")
            return redirect('login')

    form =CreateUserForm()
    con={
        'form':form,
        'Form_titel':'Register Page',
        'btn':'Register'

    }
    return render(req,'auth/baseForm.html',con)

def loginpage(req):
    
    if req.method == "POST":
        form =AuthForm(req,req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req,"Login Successfully")
            return redirect('dashboard')

    form =AuthForm()
    con={
        'form':form,
        'Form_titel':'Login Page',
        'btn':'Login'

    }
    return render(req,'auth/baseForm.html',con)

def logoutpage(req):
    logout(req)
    return redirect('login')

@login_required
def dashboardpage(req):
    
    job = JobPostModel.objects.all()
    con={
        'job': job
    }

    return render(req,'dashboard.html',con)


def recuiterpage(req):
    try:
        recuiter = RceuiterModel.objects.get(user = req.user)
    except RceuiterModel.DoesNotExist:
        recuiter = RceuiterModel.objects.create(user= req.user)

    if req.method == "POST":
        form =CreateUserForm(req.POST,req.FILES, instance=recuiter)
        if form.is_valid():
            form.save()
            messages.success(req,"Profile Updated Successfully")
            return redirect('dashboard')

    form =rc()
    con={
        'form':form,
        'Form_titel':'Recuiter PAge',
        'btn':'Update'

    }

    return render(req,'baseform.html',con)

def JobSeekerpage(req):
    try:
        recuiter = JobPostModel.objects.get(user = req.user)
    except JobPostModel.DoesNotExist:
        recuiter = JobPostModel.objects.create(user= req.user)

    if req.method == "POST":
        form =JobPostForm(req.POST,req.FILES, instance=recuiter)
        if form.is_valid():
            form.save()
            messages.success(req,'Profiel Update')
            return redirect('dashboard')

    form =JobPostForm()
    con={
        'form':form,
        'Form_titel':'JobSeeker PAge',
        'btn':'Update'

    }

    return render(req,'baseform.html',con)

@login_required
def Jobpostpage(req):
    try:
        recuiter = JobPostModel.objects.get(user = req.user)
    except JobPostModel.DoesNotExist:
        recuiter = JobPostModel.objects.create(user= req.user)

    if req.method == "POST":
        form =JobPostForm(req.POST,req.FILES, instance=recuiter)
        if form.is_valid():
            form.save()
            messages.success(req,'Job Posted')
            return redirect('login')

    form =JobPostForm()
    con={
        'form':form,
        'Form_titel':'JobSeeker PAge',
        'btn':'Update'

    }

    return render(req,'baseform.html',con)

@login_required
def applicationpage(req):
    try:
        recruiter = RceuiterModel.objects.get(user = req.user)
    except RceuiterModel.DoesNotExist:
        recruiter = RceuiterModel.objects.create(user = req.user)
    if recruiter:
        Apply = AppliedJobModel.objects.filter(job__user = recruiter)

    con = {
        'Apply':Apply,
    }
    return render(req,'list.html',con)

@login_required
def myapplicationpage(req):
    try:
        recruiter = JobSeekerModel.objects.get(user = request.user)
    except JobSeekerModel.DoesNotExist:
        recruiter = JobSeekerModel.objects.create(user = request.user)
    if recruiter:
        myApplcation = AppliedJobModel.objects.filter(job__user = recruiter)

    con = {
        'myApplcation':myApplcation,
    }
    return render(req,'my_list.html',con)

@login_required
def skillmachingpage(req):
    
    try:
        user = JobSeekerModel.objects.get(user =req.user)
    except JobSeekerModel.DoesNotExist:
        return redirect('jobseeker')
    if user:
        user_skill =  user.skill_set.all()
        
        jobs = JobPostModel.objects.filter(skill_set__in = user_skill).distinct()
    
    con={
        'jobs': jobs
    }
    return render(req,'Skill_dashbaord.html',con)

@login_required
def skillPage(req):
    
   
    if req.method == "POST":
        form = SkillForm(req.POST)
        if form.is_valid():         
            form.save()            
            messages.success(req,'Skill Added')
            return redirect("dashboard")

    form = SkillForm()
    context={
        'form':form,
        'form_title':"Add A Skill",
        'btn':"Add"
    }
    return render(req,"pages=baseForm.html",context)

@login_required
def shortlistpage(req,id):
    
    appli_id = AppliedJobModel.objects.get(id=id)
    appli_id.status = 'ShortList'
    appli_id.save()
    
    return redirect('applicationlist')


@login_required
def rejectpage(req,id):
    
    appli_id = AppliedJobModel.objects.get(id=id)
    appli_id.status = 'Rejected'
    appli_id.save()
    
    return redirect('applicationlist')


@login_required
def pendingpage(req,id):
    
    appli_id = AppliedJobModel.objects.get(id=id)
    appli_id.status = 'Pending'
    appli_id.save()
    
    return redirect('applicationlist')


    
    
    








