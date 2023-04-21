from django.contrib.auth.models import User
from django.db import models


class Authors(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)


class Courses(models.Model):
    header = models.TextField()
    description = models.TextField()
    main_text = models.TextField()
    name = models.TextField()
    id_author = models.ForeignKey(Authors, on_delete=models.CASCADE)


class Timetable(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField(u"Conversation Date", blank=True)
    end_date = models.DateField(u"Conversation Date", blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class UsersCourses(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Applications(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    purpose = models.TextField()


class Complaints(models.Model):
    complaint = models.TextField()
    id_course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title
