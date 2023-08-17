from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('normaluser', 'Normal User'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
        ('blogadmin', 'Blog Admin'),
    )
    
    EDUCATION_CHOICES = (
        ('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
    )
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    username=models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    company_website = models.URLField(blank=True)
    designation = models.CharField(max_length=50)
    annual_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    instagram_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'  

    REQUIRED_FIELDS = ['user_type','country_code','mobile','education','gender',
                       'company_website','designation','annual_revenue','instagram_profile','linkedin_profile','portfolio','is_active','first_name']

    
    custom_groups = models.ManyToManyField(
        Group,
        through='CustomUserGroup',
        through_fields=('user', 'group'),
        related_name='custom_users'
    )

    custom_permissions = models.ManyToManyField(
        Permission,
        through='CustomUserPermission',
        through_fields=('user', 'permission'),
        related_name='custom_users'
    )

    def __str__(self):
        return self.username

class CustomUserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class CustomUserPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
