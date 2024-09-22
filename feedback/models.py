from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    product = models.CharField(max_length)

    def __str__(self):
        return f"{self.name} - {self.product}"