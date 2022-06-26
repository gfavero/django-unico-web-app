from django.db import models
from django.contrib.auth.models import User


class Theme_table(models.Model):
    theme_value = models.CharField(max_length=50)
    theme_text = models.TextField(blank=True)
    theme_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.theme_value

class Totem_table(models.Model):
    totem_value = models.CharField(max_length=50)
    totem_text = models.TextField(blank=True)
    totem_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.totem_value

# table to hold the 5 w categories
class Five_w_table(models.Model):
    five_w_value = models.CharField(max_length=50)
    five_w_text = models.TextField(blank=True)
    five_w_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.five_w_value

# in table to hold the in categories         
class In_table(models.Model):
    in_value = models.CharField(max_length=50)
    pda_01 = models.TextField()
    pda_01 = models.TextField()
    in_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.in_value

# Status table to hold status (e.g Open, close, WIP)
class Status_table(models.Model):
    content_status = models.CharField(max_length=50)
    def __str__(self):
        return self.content_status
    
# main table to hold the contene data    
class Content_table(models.Model):
    content_subject = models.CharField(max_length=255)
    content_reference = models.CharField(max_length=255, blank=True)
    content_five_w = models.ForeignKey(Five_w_table,null=True,blank=True, on_delete=models.SET_NULL)
    content_totem = models.ForeignKey(Totem_table,null=True,blank=True, on_delete=models.SET_NULL)
    content_theme = models.ForeignKey(Theme_table,null=True,blank=True, on_delete=models.SET_NULL)
    content_in = models.ForeignKey(In_table,null=True,blank=True, on_delete=models.SET_NULL)
    content_creation_date = models.DateField()
    content_comment_01 = models.TextField(max_length=255, blank=True)
    content_comment_02 = models.TextField( blank=True)
    content_comment_03 = models.TextField(max_length=255, blank=True)
    author = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)
    content_status = models.ForeignKey(Status_table, on_delete=models.CASCADE)

    def __str__(self):
        return self.content_subject


class Principal_table(models.Model):
    content_principal = models.TextField(max_length=255, blank=True, default='Principal')
    author = models.OneToOneField(User,  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content_principal


class Conjunto_table(models.Model):
    content_conjunto = models.TextField(max_length=255, blank=True)
    author = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content_conjunto

class Base_table_new(models.Model):
    content_base = models.TextField(max_length=255, blank=True)
    content_conjunto = models.ForeignKey(Conjunto_table,  null=True, blank=True, on_delete=models.CASCADE)
    author_user = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content_base

class Sub_base_table(models.Model):
    content_sub_base = models.TextField(max_length=255, blank=True)
    content_base = models.ForeignKey(Base_table_new,  null=True, blank=True, on_delete=models.CASCADE)
    author_user = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content_sub_base