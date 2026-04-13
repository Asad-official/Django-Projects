from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job

# Create your views here.
@login_required
def home_view(request):
    all_jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/home.html', {'jobs': all_jobs})

@login_required
def create_job_view(request):
    if not request.user.is_employer:
        return redirect('home')
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.employer=request.user
            job.save()
            return redirect('home')
    else:
        form=JobForm()
    return render(request,'jobs/create_job.html',{'form':form})
    


