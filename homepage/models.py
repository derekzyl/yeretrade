from django.db import models

# Create your models here.
from django.urls import reverse


class Transaction(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='_transact')
    name = models.CharField(max_length=20)
    date= models.DateField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='_blog')
    authur = models.CharField(max_length=20)
    date = models.DateField(blank=True, null=True)
    title=models.CharField(max_length=20)
    short_content = models.CharField(max_length=30, blank=True, null=True)
    content= models.TextField()
    slug = models.SlugField()


    def get_absolute_url(self):
        return reverse('blog-details', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.authur}'



class Withdrawal(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='_transact')
    name = models.CharField(max_length=20)
    date= models.DateField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'



class Comment(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to ='_testimony')
    comment =models.CharField(max_length = 20)
    Occupation = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class  TeamMembers(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=10)
    image = models.ImageField(default = 'default.jpg', upload_to ='_members')


    def __str__(self):
        return f'{self.name}'

class TopInvestor(models.Model):
    name = models.CharField(max_length=20)
    invested_amount = models.IntegerField()
    image = models.ImageField(default = 'default.jpg', upload_to ='_investor')



    def __str__(self):
        return f'{self.name}'


class Slider(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to ='_investor')
    comment = models.CharField(max_length=30)
    head = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.head}'
