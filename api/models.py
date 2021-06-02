from django.db import models
import string
import random
# Create your models here.
#these are database models

def generate_unique_code():
    length = 6

# assigns a random code if survey does not exist
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=1))
        if Survey.objects.filter(code=code).count() == 0:
            break

        return code


class Survey(models.Model):
    # database fields
    # must match fields from serializer('id', 'code', 'name', 'exampleBoolean', 'answersRequired', 'created_at')
    code = models.CharField(max_length=8, default="", unique=True)
    name = models.CharField(max_length=50, unique=True)
    exampleBoolean = models.BooleanField(null=False, default=False)
    answersRequired = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    #Django design philosophy- fat models and thin views
    # put more logic in models

