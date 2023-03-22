from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job


# Create your views here.
def job_list(request):
    context = {'job_list' : Job.objects.all()}
    return render(request, "job_application/job_list.html", context)

def job_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = JobForm()
        else:
            job =Job.objects.get(pk=id)
            form = JobForm(instance=job)
        return render(request, "job_application/job_form.html", {'form':form})
    else:
        if id==0:
            form = JobForm(request.POST)
        else:
            job =Job.objects.get(pk=id)
            form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
        return redirect('/jobs/list/')




def job_delete(request, id):
    job =Job.objects.get(pk=id)
    job.delete()
    return redirect('/jobs/list/')