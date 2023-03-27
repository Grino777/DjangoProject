from django.db import models

# Create your models here.

class Gallary(models.Model):
    #------------------------------------
    image = models.FileField(upload_to='my_gallary')
    #upload_to - ссылка на файл. Указывается папка (которая будет создана в корне проекта)
    #Если создан MEDIA_ROOT в settings, то upload_to будет создавать подкаталог в этой папке
    #-------------------------------------