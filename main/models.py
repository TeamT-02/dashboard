from django.db import models


class Home(models.Model):
    images = models.ImageField(upload_to='midea/home/')
    title = models.CharField(max_length=80)
    text = models.TextField()


class Statik(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=40)


class Problems_right(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    images = models.ImageField(upload_to='midea/solutions/')


class Problems_left(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    images = models.ImageField(upload_to='midea/solutions/')


class Social_Networks(models.Model):
    images = models.ImageField(upload_to='midea/social_networks/networks/')
    title = models.CharField(max_length=40)
    text = models.TextField()


class Social_Networks_link(models.Model):
    forkey = models.ForeignKey(Social_Networks, on_delete=models.CASCADE)
    instagram_link = models.CharField(max_length=250)
    # facebook_link = models.CharField(max_length=250)
    telegram_link = models.CharField(max_length=250)
    telegram_bot = models.CharField(max_length=250)


class Website_update(models.Model):
    date = models.DateField()
    text = models.TextField()
    funksiya_update_right = models.CharField(max_length=150)
    funksiya_update_left = models.CharField(max_length=150)