from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    company_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
