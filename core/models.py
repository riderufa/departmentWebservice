from django.db import models
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.utils import timezone


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    STUDENT, TEACHER = range(2)
    TYPE_CHOICES = [
        (STUDENT, 'Студент'),
        (TEACHER, 'Преподаватель'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    patronymic = models.CharField('Отчество', max_length=255)

    type = models.SmallIntegerField('Тип', choices=TYPE_CHOICES)
    user_group = models.ForeignKey(
        'UserGroup', on_delete=models.SET_NULL, verbose_name='Группа',
        related_name='user_profiles', null=True, blank=True
    )
    department = models.ForeignKey(
        'Department', on_delete=models.PROTECT, verbose_name='Кафедра', related_name='user_profiles', null=True,
        blank=True
    )
    image = models.ImageField('Фотография', upload_to='images/%Y/%m/%d', max_length=255, null=True, blank=True)

    @property
    def image_url(self):
        if self.image:
            return getattr(self.image, 'url', None)
        return None

    def __str__(self):
        return self.user.username


class UserGroup(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    title = models.CharField('Наименование', max_length=255)

    def __str__(self):
        return self.title


class Department(models.Model):
    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    title = models.CharField('Наименование', max_length=255)
    class_schedule = models.FileField('Расписание занятий', upload_to='files/%Y/%m/%d', null=True, blank=True)
    session_schedule = models.FileField('Расписание сессии', upload_to='files/%Y/%m/%d', null=True, blank=True)

    @property
    def class_schedule_url(self):
        if self.class_schedule:
            return getattr(self.class_schedule, 'url', None)
        return None

    def pdf_view(self):
        # try:
        return FileResponse(open(self.class_schedule_url, 'rb'), content_type='application/pdf')
        # except FileNotFoundError:
        #     raise Http404()

    def __str__(self):
        return self.title


class Discipline(models.Model):
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    title = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name='Кафедра', related_name='disciplines'
    )
    tutorial = models.FileField('Учебник', upload_to='files/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    class Meta:
        verbose_name = 'Материал лекции'
        verbose_name_plural = 'Материалы лекций'

    title = models.CharField('Наименование', max_length=255)
    created_at = models.DateField('Дата создания', default=timezone.now)
    discipline = models.ForeignKey(
        Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина', related_name='lectures'
    )
    file = models.FileField('Файл', upload_to='files/%Y/%m/%d')

    def __str__(self):
        return self.title
