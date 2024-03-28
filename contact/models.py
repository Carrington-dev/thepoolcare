from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-date_sent']