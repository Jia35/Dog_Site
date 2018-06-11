from django.db import models
from django.utils import timezone

class Alluser(models.Model):
    account = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'user_pictures',blank=True)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    residential_location = models.CharField(max_length=30)
    housing_condition = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100,blank=True)
    score = models.DecimalField(max_digits=3,decimal_places=1,default = 0)
    evaluation = models.CharField(max_length=100,blank=True)
    introduce = models.TextField(max_length=500,blank=True)

    collection_user = models.CharField(max_length=1000,blank=True)
    chat_user = models.CharField(max_length=1000,blank=True)
    creation_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name


class Dogs(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'dog_pictures',blank=True)
    gender = models.CharField(max_length=10)
    age = models.DecimalField(max_digits=3,decimal_places=0)
    breed = models.CharField(max_length=20)
    character = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200)
    is_foster = models.BooleanField(default = False)
    master = models.ForeignKey(Alluser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GPSs(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=6)  #緯度
    longitude = models.DecimalField(max_digits=10,decimal_places=6) #經度
    dog = models.ForeignKey(Dogs,on_delete=models.CASCADE)
    

'''class Chat(models.Model):
    sender = models.ForeignKey(Alluser,on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u'%s' % self.content
    '''

class Message(models.Model):
    account = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default = timezone.now)
