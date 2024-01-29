from django.db import models

# Create your models here.

NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('N', 'Never')
]

# subscriber model
class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    option = models.CharField(max_length=1, choices=NEWSLETTER_OPTION, default='W')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"