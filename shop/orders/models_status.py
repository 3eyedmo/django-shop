from django.db import models

class OrderStatus(models.TextChoices):
    Pending = "P"
    Done = "D"
    Failed = "F"