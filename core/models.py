from django.db import models


class Data(models.Model):
    cpi = models.IntegerField()
    last_serve = models.IntegerField()

    def __str__(self):
        return f'({self.cpi}, {self.last_serve})'

    def save(self, *args, **kwargs):
        print(f' args: {args},\n kwargs: {kwargs} ')
        super().save(*args, **kwargs)


