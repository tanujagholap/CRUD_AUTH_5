from django.db import models


class Create(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_price = models.IntegerField()
    pro_quantity = models.IntegerField()
    purchase_date = models.DateField()

