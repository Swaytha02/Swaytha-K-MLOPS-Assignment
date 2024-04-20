from django.db import models

class React(models.Model):
    number_courses = models.IntegerField()
    time_study = models.IntegerField()
    def __str__(self):
        return f"Number of Courses: {self.number_courses}, Time: {self.time_study}"
