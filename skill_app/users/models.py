from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    first_name = models.CharField(max_length = 30, blank = True, default='First')
    last_name = models.CharField(max_length = 30, blank = True, default='Last')
    email = models.EmailField(unique = True)
    city = models.CharField(max_length = 30, blank = True, default='Default Town')
    state = models.CharField(max_length = 2, default='CA')
    summary = models.TextField(max_length=250, default='Default summary')
    min_salary = models.IntegerField(blank = True, default='10000')
    skills = models.ManyToManyField('skills.Skill', help_text='Select each skill.', related_name='skill_model')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email