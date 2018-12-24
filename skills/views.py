from django.shortcuts import render
from skills.models import JobRecord, Skill
from users.models import User
from .forms import JobForm
from django.shortcuts import redirect
from users.forms import CustomUserCreationForm as UserForm

def count_objects(obj):
	return int(obj.count())

jobs = JobRecord.objects.order_by('-match')
users = User.objects.filter(is_staff=False)
num_jobs = count_objects(jobs.all())

#num_jobs = 3
#jobs = []

def add_job(request):
	if request.method == "POST":
		form = JobForm(request.POST)
		if form.is_valid():
			job = form.save(commit=False)
			job.created_by = request.user
			job.save()
			return redirect('home')

	else:
		form = JobForm()
	return render(request, 'main/add_job.html', {'form': form})

#def edit_job(request, job):

#	job_to_edit = JobRecord.objects.get(id=job)

#	if request.method == "POST":
#		form = JobForm(request.POST)
#		if form.is_valid():
#			job_to_edit = form.save(commit=False)
#			job_to_edit.save()
#			return redirect('home')

#	else:
#		form = JobForm()
#	return render(request, 'main/edit_job.html', {'form': form})

def delete_skill(request, skill_id):
	if skill_id in Skill.objects.filter(id=skill_id):
		skill = Skill.objects.get(id=skill_id)
		skill.delete()
	return render (request, 'main/profile.html')

def edit_user(request):
	if request.method != "POST":
		entry = User.objects.get(id=request.user.id)
		form = UserForm(instance=entry)
	else:
		form = UserForm(data=request.POST)
		if form.is_valid():
			request.user = form.save(commit=False)
			request.user.save()
			return redirect('home')
	return render(request, 'edit_user.html' , {'form': form})

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

	if request.GET.get('match-filter'):
		match_cutoff = request.GET.get('match-filter')
		jobs = JobRecord.objects.filter(match__gte=match_cutoff)
	elif request.GET.get('sort-by'):
		sort_term = request.GET.get('sort-by')
		jobs = JobRecord.objects.order_by(sort_term).reverse()
	else:
		jobs = JobRecord.objects.all()
	num_jobs = count_objects(jobs)
	return render(request, 'main/index.html', { 'num_jobs': num_jobs, 'jobs': jobs },)

def profile(request):
	return render(request, 'main/profile.html')

def candidates(request):
	return render(request, 'main/candidates.html', {'users': users})

def summary(request):
	return render(request, 'main/summary.html')
