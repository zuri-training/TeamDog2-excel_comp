from django.db import models

# Create your models here.
class Excel_doc_one(models.Model):
    file_one = models.FileField(upload_to='saved/%Y/%m/%d/')
    

class Excel_doc_two(models.Model):
    file_two = models.FileField(upload_to='saved/%Y/%m/%d/',)

