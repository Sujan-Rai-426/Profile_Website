from django.contrib import admin

# Register your models here.

from Home.models import Achivements, Back_End_Skill, CurrentAddress, Download, Project, Front_End_Skill


admin.site.register(Project)
admin.site.register(Front_End_Skill)
admin.site.register(Back_End_Skill)
admin.site.register(Download)
admin.site.register(CurrentAddress)
admin.site.register(Achivements)