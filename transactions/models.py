from datetime import datetime
from django.db import models

# Create your models here.
class UnvalidTransactions(models.Model):
    created_date = models.DateTimeField()
    sender = models.CharField(max_length=200)
    amount = models.IntegerField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        print("HOOO")
        if not self.id:
            self.created_date = datetime.now()

        return super(UnvalidTransactions, self).save(*args, **kwargs)

class Transactions(models.Model):
    created_date = models.DateTimeField()
    sender = models.CharField(max_length=200)
    amount = models.IntegerField()