from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Lessons(models.Model):
    lesson = models.CharField('Названия урока',max_length=50)
    about_lesson = models.TextField('Об уроке')
    photo = models.FileField(upload_to='photos/')
    
    def __str__(self):
        return self.lesson
    
    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        

class Now_Lessons(models.Model):
    lesson = models.CharField('Названия урока',max_length=50)
    about_lesson = models.TextField('Об уроке')
    photo = models.FileField(upload_to='photos/')
    def __str__(self):
        return self.lesson
    
    class Meta:
        verbose_name = 'now lesson'
        verbose_name_plural = 'now lessons'
    
    
class New_Lessons(models.Model):
    lesson = models.CharField('Названия урока',max_length=50)
    about_lesson = models.TextField('Об уроке')
    photo = models.FileField(upload_to='photos/')
    def __str__(self):
        return self.lesson
    class Meta:
        verbose_name = 'new lesson'
        verbose_name_plural = 'new lessons'
    
class Students(models.Model):
    kurs = models.CharField('Курс',max_length=50)
    full_name = models.CharField('Имя фамилия',max_length=50)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=50)
    created_at = models.DateTimeField()
   
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Users(models.Model):
    full_name = models.CharField('Имя фамилия',max_length=50)
    telegram_id = models.IntegerField('Telegram id', primary_key=True)
    username = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Bot_admin(models.Model):
    full_name = models.CharField('Имя фамилия',max_length=50)
    telegram_id = models.IntegerField('Telegram id', primary_key=True)
    username = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'



class Hendlers(models.Model):
   
    
    msg_start = models.CharField('start',max_length=100)
    msg_kurs = models.CharField('kurslar',max_length=100)
    msg_name = models.CharField('ism familiya',max_length=100)
    msg_phone = models.CharField('telefon raqam',max_length=100)
    msg_adres = models.CharField('uy manzil',max_length=100)
    reseption = models.CharField('resepyion',max_length=100)
    data_tel = models.CharField('data telefon raqam',max_length=100)
    now_lessons_msg = models.CharField('hozirgi kurslar',max_length=100)
    new_lessons_msg = models.CharField('yangi ochiladigan kurlar',max_length=100)
    lessons_msg = models.CharField('barcha kurslar',max_length=100)
    l_message = models.CharField('barcha kurslarimiz',max_length=100)
    new_message = models.CharField('endi ochiladigan kurslarimiz',max_length=100)
    now_message = models.CharField('hozirda ochiq kurlarimiz',max_length=100)
    
    def __str__(self):
        return self.msg_start[:16]
    class Meta:
        verbose_name = 'hendler'
        verbose_name_plural = 'hendlers'