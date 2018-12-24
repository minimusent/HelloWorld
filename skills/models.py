from django.db import models
from django.urls import reverse
from django_currentuser.middleware import (
    get_current_authenticated_user)

class Length(models.Model):
	length = models.IntegerField(help_text='months')

	def __str__(self):
		return str(self.length)

class Requirement(models.Model):
	title = models.CharField(max_length=100, help_text='Required element.')

	def __str__(self):
		return self.title

class Skill(models.Model):
	title = models.CharField(max_length=40, help_text="Enter skill name", default="Default")
	length = models.ForeignKey(Length, on_delete=models.CASCADE, default='0', help_text='months')

	def __str__(self):
		return self.title

# Used to identify benefits associated with each job, as well as desired benefits in the user model
class Benefit(models.Model):
	title = models.CharField(max_length=50, help_text='Enter benefit', default='Default')

	def __str__(self):
		return self.title

# Used to identify technology used for each job, as well as in the user profile
class Tech(models.Model):
	title = models.CharField(max_length=50, help_text='Enter tech', default='Default')

	def __str__(self):
		return self.title

class JobRecord(models.Model):
	title = models.CharField(max_length=20, help_text='Enter job title')
	city = models.CharField(max_length=30,default="Los Angeles")
	state = models.CharField(max_length=2,default="CA")
	co_name = models.CharField(max_length=30,default="Google")
	pos_type = models.CharField(max_length=20,default="Full Time")
	low_salary = models.IntegerField()
	high_salary = models.IntegerField()
	typical_day = models.TextField(default="")
	avg_day = models.TextField(default="")
	tech_used = models.TextField(default="")
	skills = models.ManyToManyField(Skill, help_text='Select each skill.')
	requirements = models.ManyToManyField(Requirement, help_text='Select each requirement.')
	match = models.IntegerField(default='1')
	benefit = models.ManyToManyField(Benefit, help_text='Select each benefit for this job.')
	tech = models.ManyToManyField(Tech, help_text='Select technology used for this job.')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, default=1)

	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])

	def __str__(self):
		return self.title

	def get_total_match(self):
		user = get_current_authenticated_user()
		matchCount = 0
		ratio = 0
		matchPercent = 0
		for skill in self.skills.all():
			for userSkill in user.skills.all():
				if userSkill.title.lower() == skill.title.lower():
					ratio = int(userSkill.length.length) / int(skill.length.length)
			matchPercent += ratio
			skill.match = round(ratio * 100)
			ratio = 0
			matchCount += 1
		if matchCount > 0:
			matchPercent = round((matchPercent / matchCount) * 100)
		self.match = matchPercent
		self.save()
		return matchPercent

class Meta:
	ordering = ['-title']
