from django.db import models
from django.db.models.fields import CharField
import string
import random
# Create your models here.
class Listing(models.Model):
    code = models.CharField(max_length = 8, default = "", unique = True)
    name = models.TextField(max_length = 25)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)

def generate_unique_code():
    length = 6
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k = length))
        if Listing.objects.filter(code = code).count() == 0:
            break
    return code 

