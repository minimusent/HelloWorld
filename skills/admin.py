from django.contrib import admin
from skills.models import JobRecord
from skills.models import Skill
from skills.models import Length
from skills.models import Benefit
from skills.models import Requirement

admin.site.register(JobRecord)
admin.site.register(Skill)
admin.site.register(Length)
admin.site.register(Benefit)
admin.site.register(Requirement)
