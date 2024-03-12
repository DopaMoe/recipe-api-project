from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    A custom manager for the User model.
    This manager provides methods for creating and managing user objects.
    """

    def create_user(self, email, password, **extra_fields) -> 'User':
        """
         Creates and saves a new user with the given email and password.
            Args:
                email (str): The email address of the user.
                password (str): The password for the user.
                **extra_fields: Additional fields to be set for the user.
            Returns:
                User: The created user object.
        """
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(user_email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password) -> 'User':
        """
        Creates and saves a new superuser with the given email and password.
            Args:
                email (str): The email address of the superuser.
                password (str): The password for the superuser.
            Returns:
                User: The created superuser object.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    A custom User model that extends the AbstractBaseUser and PermissionsMixin classes.
    it uses the user_email field as a username instead of the default
    Attributes:
        user_email (EmailField): The email address of the user.
        name (CharField): The name of the user.
        is_active (BooleanField): Indicates whether the user is active or not.
        is_staff (BooleanField): Indicates whether the user is a staff member or not.

    Methods:
        create_user(email, password, **extra_fields): Creates and saves a new user with the given email and password.
        create_superuser(email, password): Creates and saves a new superuser with the given email and password.
    """

    user_email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'user_email'
