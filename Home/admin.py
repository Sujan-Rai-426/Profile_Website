from django.contrib import admin

# Register your models here.

from Home.models import Back_End_Skill, Download, Project, Front_End_Skill


admin.site.register(Project)
admin.site.register(Front_End_Skill)
admin.site.register(Back_End_Skill)
admin.site.register(Download)
