from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
GENDER_CHOICES = (
    		('MEN' , 'MEN'),
    		('WOMEN' , 'WOMEN'),
    	)
SIZE_CHOICES = (
	('S','S'),
	('M','M'),
	('L','L'),
	('XL','XL'),
	('XXL','XXL'),
	('XXXL','XXXL'),
	)


class Profile(models.Model):
    adress = models.TextField()
    gender= models.CharField(max_length=6, choices = GENDER_CHOICES, default='MEN')
    top_size = models.CharField(max_length=6, choices = SIZE_CHOICES, default='M')
    bottom_size = models.CharField(max_length=6, choices = SIZE_CHOICES, default='M')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 업주 only
    is_store_owner = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True, verbose_name='휴대폰 번호', help_text='연락가능한 번호를 적어주세요')

    # 학생 only
    school = models.CharField(max_length=40, null=True, verbose_name='대학이름')
    major = models.CharField(max_length=40, null=True, verbose_name='소속', help_text='본인이 속한 단과대학이나 동아리 이름을 적어주세요.')
    
    name = models.CharField(max_length=40,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=40,null=True)
    favorites = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
