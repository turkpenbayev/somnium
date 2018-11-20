from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from test_task.settings import EMAIL_HOST_USER

# Create your models here.


class Company(models.Model):

    class Meta:
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'

    name = models.CharField(verbose_name='Имя организации', max_length=64)
    description = models.TextField(verbose_name='Детально')

    def __str__(self):
        return self.name

    
class Department(models.Model):

    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отдели'

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя отдели', max_length=64)
    supervisor = models.OneToOneField(User, verbose_name = 'Начальник', on_delete=models.CASCADE)
    workers = models.ManyToManyField(User, verbose_name = 'Подчиненные', related_name='department_workers')

    def get_supervisor(self):
        return self.supervisor.profile.get_full_name()

    def get_number_of_workers(self):
        return self.workers.count()

    def __str__(self):
        return self.name


class Position(models.Model):

    class Meta:
        verbose_name = u'Должност'
        verbose_name_plural = u'Должности'

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя должности', max_length=64)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    User profile
    """

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ManyToManyField(Position, verbose_name = 'Должност')
    name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    phone = models.CharField(verbose_name='Номер тел', max_length=14, default = '87000000000')
    email = models.EmailField(verbose_name = 'Почта')    

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, EMAIL_HOST_USER, [self.email], fail_silently=True, **kwargs)
        return self.email

    def get_full_name(self):
        return ('%s %s'%(self.last_name, self.name))

    def __str__(self):
        return ('%s %s'%(self.last_name, self.name))


