from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    JINS = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    gender = models.CharField(max_length=6, choices = JINS)
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to = 'user_photos')
    def __str__(self):
        return self.username
    


class Bolim(models.Model):
    name = models.CharField(max_length=255)
    bolim_id = models.CharField(unique=True)
    


class Ish_turi(models.Model):
    ish_name = models.CharField(max_length=100)
    ish_id = models.CharField(unique=True)
    def __str__(self):
        return self.ish_name
    
	
class Maxsulot(models.Model):
    name = models.CharField(max_length=255)
    maxsulot_id = models.CharField(unique=True)
 


class Xodim(models.Model):
    JINS = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    gender = models.CharField(max_length=6, choices = JINS, null = True)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    image = models.ImageField(upload_to = 'xodim_photos')
    phone = models.CharField(max_length=13)
    ish_turi = models.ForeignKey(Ish_turi, on_delete = models.CASCADE, related_name = 'ish_turi')
    xodim_id = models.CharField(unique=True)
    bolimi = models.ForeignKey(Bolim, on_delete = models.CASCADE, related_name = 'bolim')
    def __str__(self):
        return self.name
    
class Problem(models.Model):
    xato_id = models.CharField(unique=True)
    problem_name = models.TextField()
    

class Mistakes(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, related_name='xodim')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem')
    rasm = models.ImageField(upload_to = 'MistakeFiles/', blank=True, null=True)
    file = models.FileField(upload_to = 'MistakeFiles/', null=True, blank=True)
    izoh = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE, related_name = 'maxsluot')