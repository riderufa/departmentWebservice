from django.views.generic import ListView, DetailView

from core.models import Department, UserGroup, UserProfile, User


class DepartmentsListCreateView(ListView):
    model = Department
    template_name = 'core/departments.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = UserGroup.objects.all()
        context['department'] = Department.objects.get(pk=1)
        return context


class ClassScheduleDetailView(DetailView):
    model = Department
    template_name = 'core/department_class_schedule.html'


class UserGroupDetailView(DetailView):
    model = UserGroup
    template_name = 'core/user_groups.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = UserGroup.objects.all()
        context['students'] = User.objects.filter(profile__type=UserProfile.STUDENT, profile__user_group__pk=self.object.pk)
        context['department'] = Department.objects.get(pk=1)
        return context


class TeacherListView(ListView):
    model = User
    template_name = 'core/teachers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = UserGroup.objects.all()
        context['teachers'] = User.objects.filter(profile__type=UserProfile.TEACHER)
        context['department'] = Department.objects.get(pk=1)
        return context
