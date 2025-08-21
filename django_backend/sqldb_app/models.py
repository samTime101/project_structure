# SAMIP REGMI
# AUGUST 20
# THE MODELS ARE REFERENCED FROM <../SQLcommands.txt> AS PROVIDED BY ARVIND SIR

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phonenumber, firstname, lastname, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not phonenumber:
            raise ValueError("Users must have a phone number")
        if not firstname:
            raise ValueError("Users must have a first name")
        if not lastname:
            raise ValueError("Users must have a last name")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phonenumber=phonenumber,
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        # PASSWORD HASHING
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phonenumber, firstname, lastname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email=email,
            username=username,
            phonenumber=phonenumber,
            firstname=firstname,
            lastname=lastname,
            password=password,
            **extra_fields
        )

# USER MODEL
class User(AbstractBaseUser, PermissionsMixin):
    userId = models.AutoField(primary_key=True)
    userGuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phonenumber = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=30, default="system")
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=30, default="system")
    status = models.IntegerField(default=1)

    # DJANGO AUTH FIELDS
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    # LOGIN WITH EMAIL
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["username", "phonenumber", "firstname", "lastname"]

    def __str__(self):
        return self.email

# CATEGORY MODELS
class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=20)


class SubCategory(models.Model):
    subCategoryId = models.AutoField(primary_key=True)
    subCategoryName = models.CharField(max_length=20)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)

class SubSubCategory(models.Model):
    subSubCategoryId = models.AutoField(primary_key=True)
    subSubCategoryName = models.CharField(max_length=20)
    subCategoryID = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
