from django.db import models





class Category(models.Model):

    name = models.CharField(max_length=255,verbose_name='cateqoriya adi')

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',)
       verbose_name = 'cateqoriya adi'
       verbose_name_plural = 'cateqoriya adlari'


class Item(models.Model):
   
    name = models.CharField(max_length=255,verbose_name='daxil edilen ')
    color = models.CharField(max_length=255,verbose_name='daxil edilen reng')
    price = models.FloatField(verbose_name='daxil edilen qiymey')
    count = models.IntegerField(verbose_name='daxil edilen say')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='media/',verbose_name = 'meslul sekili',null=True,blank=True)

    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name', )
       verbose_name = 'daxil edilen'
       verbose_name_plural = 'daxil edilenler'

