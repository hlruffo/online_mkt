from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering:('name', ) #tupla para ordenar
        verbose_name_plural ="Categories" #ajusta o plural do nome no quadro de adm

    def __str__(self):  #mostra o nome dos itens salvos em categoria na lista
        return self.name
    
    
class Item(models.Model):
    categoty =models.ForeignKey(Category,related_name="items", on_delete=models.CASCADE)
    name =  models.CharField( max_length=255)
    description = models.TextField(blank = True, null = True)    
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    create_at =models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    
    def __str__(self):  #mostra o nome dos itens salvos em categoria na lista
        return self.name
