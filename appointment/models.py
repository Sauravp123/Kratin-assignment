from django.db import models
 
class Category(models.Model):
	name=models.CharField(max_length=200, db_index=True)
	

	class Meta:
		ordering = ('name',)
		verbose_name='category'
		verbose_name_plural='categories'

	def __str__(self):
		return self.name

class Patient(models.Model):
	category=models.ForeignKey(Category, related_name='products', on_delete=True)
	name=models.CharField(max_length=200, db_index=True)
	
	address=models.TextField(blank=True)
	
	available=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=('-created',)
		

	def __str__(self):
		return self.name
	


