from django.db import models

# Create your models here.
class checkoutUserDetails(models.Model):

    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()
    destination = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField('DD-MM-YYYY')
    unique_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.destination