from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote


class Like(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(
        Quote, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'quote']

    def __str__(self):
        return f'{self.owner}, {self.quote}'
