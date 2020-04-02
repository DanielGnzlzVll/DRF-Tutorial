from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Course(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    abstract = models.TextField()


def files_path(instance, filename):
    return f"{instance.course.topic.name}/{instance.course.name}/{instance.name}"


class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=files_path)
