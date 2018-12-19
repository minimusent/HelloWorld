from django.shortcuts import render
from skills.models import JobRecord
from users.models import User
from .forms import JobForm
from django.shortcuts import redirect

def count_objects(obj):
	return int(obj.count())

jobs = JobRecord.objects.order_by('-match')
users = User.objects.filter(is_staff=False)
num_jobs = count_objects(jobs.all())

#num_jobs = 3
#jobs = []

def job_new(request):
	if request.method == "POST":
		form = JobForm(request.POST)
		if form.is_valid():
			job = form.save(commit=False)
			job.save()
			return redirect('home')

	else:
		form = JobForm()
	return render(request, 'main/new_job.html', {'form': form})

# Create your views here.

def search(request):
	num_jobs = 0
	jobs = None
	if request.method == 'GET':
		job_name = request.GET.get('search')
		try:
			jobs = JobRecord.objects.filter(title__icontains=job_name)
		except JobRecord.DoesNotExist:
			jobs = None
		num_jobs = count_objects(jobs)
	return render(request, 'main/index.html', {'num_jobs': num_jobs, 'jobs': jobs},)

def home(request):
	return render(request, 'main/index.html', { 'num_jobs': num_jobs, 'jobs': jobs },)

def profile(request):
	return render(request, 'main/profile.html')

def candidates(request):
	return render(request, 'main/candidates.html', {'users': users})

def summary(request):
	return render(request, 'main/summary.html')
