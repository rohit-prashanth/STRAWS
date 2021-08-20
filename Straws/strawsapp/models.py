from django.db import models

# Create your models here.
class WorkersDetail(models.Model):
    worker_id = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    address = models.TextField()
    id_types = [('Adhr','Aadhaar'), ('Pn','Pan'), ('DL','Driving License'), ('Pp','Passport')]
    identity_type = models.CharField(choices=id_types,default='Aadhaar', max_length=20)
    identity_number = models.CharField(max_length=20)

class StoresList(models.Model):
    store_code = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    manager_id = models.CharField(max_length=20)

class ManagerDetail(models.Model):
    manager_id = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    address = models.TextField()
    id_types = [('Adhr','Aadhaar'), ('Pn','Pan'), ('DL','Driving License'), ('Pp','Passport')]
    identity_type = models.CharField(choices=id_types, default='Aadhaar',max_length=20)
    identity_number = models.CharField(max_length=20)

