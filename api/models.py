from django.db import models
import string
import random
def generate_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Channel.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class Channel(models.Model):
    code = models.CharField(max_length=8, default=generate_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_pause = models.BooleanField(null=False, default=False)
    votes_skip = models.IntegerField(null=False, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

