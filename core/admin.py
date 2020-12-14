from django.contrib import admin
from core.models import UserProfile, UserGroup, Department, Discipline, Lecture


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    pass
