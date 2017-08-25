from django.db import models
from django.utils import timezone


class Asset(models.Model):
    name = models.CharField('Token name', max_length=100)
    amount = models.CharField('Amount', max_length=100)
    description = models.TextField('Description')
    reissuable = models.BooleanField()
    token_id = models.CharField('Token id', max_length=100)
    sender_id = models.CharField('Sender id', max_length=100)
    selected = models.BooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('assets:detail', kwargs={'token_id': self.token_id})
