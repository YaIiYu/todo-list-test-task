from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('done', 'Done'), ('not_done', 'Not done')], default='not_done')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.title
