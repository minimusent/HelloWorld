from django import template
from datetime import datetime
#from skills.middleware import get_current_user

register = template.Library()

def get_days_old_string(value):
    value = value.replace(tzinfo=None)
    delta = value - datetime.today()

    if delta.days == 0:
        return "posted today"
    elif delta.days < 1:
        return "posted %s %s ago" % (abs(delta.days), ("day" if abs(delta.days) == 1 else "days"))
    else:
        return "posted %s days ago" % delta.days

def get_skill_match(value, arg): # working 100%
    skill = value
    user = arg
    ratio = 0
    for userSkill in user.skills.all():
        if userSkill.title.lower() == skill.title.lower():
            ratio = int(userSkill.length.length) / int(skill.length.length)
    return round(ratio*100)

def get_match_color(value):
    match = value
    if match < 50:
        return 'red'
    elif match > 49 and match < 85:
        return 'orange'
    elif match > 84:
        return 'green'

register.filter('get_skill_match', get_skill_match)
register.filter('get_match_color', get_match_color)
register.filter('get_days_old_string', get_days_old_string)