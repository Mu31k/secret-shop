from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
   # img = models.ImageField(upload_to='photos/%y/%m/%d/')# height_field=100, width_field=100)
    price = models.CharField('Цена', max_length=20)
    date = models.DateTimeField('Дата публикации')


