from django.db import models

# Create your models here.

# Foods field
class Foods(models.Model):
	title = models.CharField('Taom nomi', max_length=250)
	body = models.TextField("Taomga ta'rif")
	image = models.ImageField('Taom rasmi', upload_to='order_food/')
	cost = models.CharField('Narxi', max_length=10)

	class Meta:
		verbose_name = 'Taklif'
		verbose_name_plural = 'Takliflar'

	def __str__(self):
		return f"{self.title}"

# Order field
class OrderFood(models.Model):
	name = models.CharField('Ismi', max_length=100)
	surname = models.CharField('Familyasi', max_length=100)
	number = models.CharField('Tel raqami', max_length=15)

	class Meta:
		verbose_name = 'Byurtma'
		verbose_name_plural = 'Buyurtmalar'

	def __str__(self):
		return f"{self.name}"

# Place order field
class PlaceOrder(models.Model):
	name = models.CharField('Ismi', max_length=100)
	surname = models.CharField('Familyasi', max_length=100)
	number = models.CharField('Tel raqami', max_length=15)
	date = models.CharField('Sanasi', max_length=30)
	guest = models.CharField('Mehmon soni', max_length=3)
	time_from = models.CharField('Dan', max_length=6)
	time_to = models.CharField('Gacha', max_length=6)
	class Meta:
		verbose_name = 'Joy Byurtma'
		verbose_name_plural = 'Joy Buyurtmalar'

	def __str__(self):
		return f"{self.name}"
# Chef field
class Chefs(models.Model):
	image = models.ImageField('Chef rasmi', upload_to='chefs_image/')
	name = models.CharField('Chef ismi', max_length=100)
	body = models.TextField('Malumot')

	class Meta:
		verbose_name = 'Oshpaz'
		verbose_name_plural = 'Oshpazlar'

	def __str__(self):
		return f"{self.name}"