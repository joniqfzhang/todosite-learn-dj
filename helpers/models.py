from django.db import models
class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # record created time
    updated_at = models.DateTimeField(auto_now=True)  # record latest updates time

    class Meta:
        abstract = True
        ordering = ('-created_at',)  # descending order
