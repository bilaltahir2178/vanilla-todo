from django.db import models

# Create your models here.
class Task:
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        is_completed = 'Completed' if self.completed else 'Incomplete'
        return self.title + " -> " + is_completed
        