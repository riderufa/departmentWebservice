from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import DepartmentsListCreateView, UserGroupDetailView, ClassScheduleDetailView, TeacherListView


urlpatterns = [
    path('', DepartmentsListCreateView.as_view(), name='main'),
    path('user_group/<int:pk>', UserGroupDetailView.as_view(), name='user_group_detail'),
    path('department/<int:pk>/class_schedule', ClassScheduleDetailView.as_view(), name='department_class_schedule'),
    path('department/teachers', TeacherListView.as_view(), name='department_teachers'),
]