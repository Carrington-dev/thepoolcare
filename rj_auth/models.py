from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
# from PIL import Image
from rj_auth.countries import countries



class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	country 				= models.CharField(max_length=200, choices=countries, default="ZA")
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	first_name          	= models.CharField(max_length=30, unique=False)
	last_name 				= models.CharField(max_length=30, unique=False)
	phone   				= models.CharField(max_length=30, unique=False)
	disability 				= models.CharField(max_length=30, unique=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_teacher			    = models.BooleanField(default=False)
	is_student			    = models.BooleanField(default=True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	
	objects = MyAccountManager()
	
	def __str__(self):
		return self.email 	# For checking permissions. to keep it simple all admin have ALL permissons
	
	def has_perm(self, perm, obj=None):
		return self.is_admin 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
		
	def has_module_perms(self, app_label):
		return True

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"


# class Profile(models.Model):
# 	user = models.OneToOneField(Account, on_delete=models.CASCADE)
# 	image = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

# 	def save(self, *args, **kwargs):
# 		super().save(*args, **kwargs)

# 		img = Image.open(self.image.path)


# 		if img.height > 300 or img.width > 300:
# 			output_size = (300, 300)
# 			img.thumbnail(output_size)
# 			img.save(self.image.path)


# 	def __str__(self):
# 		return f"{self.user.username} Profile"
	

# 	@receiver(post_save, sender=Account)
# 	def create_profile(sender, instance, created, **kwargs):
# 		if created:
# 			# profile = 
# 			Profile.objects.create(user=instance)
# 			# profile.save()



# 	@receiver(post_save, sender=Account)
# 	def save_profile(sender, instance, **kwargs):
# 		instance.profile.save()

# 	class Meta:
# 		verbose_name = "User Profile"
# 		verbose_name_plural = "User Profiles"