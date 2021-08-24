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

class TablesHistoryDatabase(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm1(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm2(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm3(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm4(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm5(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm6(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm7(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm8(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm9(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)

class TableForm10(models.Model):
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    items = models.TextField()
    total_amount = models.IntegerField()
    mode_choice = [('Cash','Cash'),('UPI','UPI'),('Card Payment','Card Payment')]
    payment_mode = models.CharField(choices=mode_choice, default='Cash', max_length=50)