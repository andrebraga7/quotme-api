from django.db import models
from django.contrib.auth.models import User
from authors.models import Author


class Quote(models.Model):

    CATEGORY_CHOICES = (
        ('books', 'Books'),
        ('lyrics', 'Lyrics'),
        ('statements', 'Statements'),
        ('originals', 'Originals'),
        ('out_of_the_box', 'Out of the box')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)

    class Meta:
        ordering = ['-created_at']
