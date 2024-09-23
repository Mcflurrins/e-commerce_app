from django.db import models
from django.contrib.auth.models import User
import uuid  # add this line at the very top


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # add this line
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
