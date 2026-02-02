import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class BaseModel(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	in_stock = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class Review(BaseModel):
	product = models.ForeignKey(
		Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews'
	)
	user = models.ForeignKey(
		User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews'
	)
	content = models.TextField()
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

	def __str__(self):
		return f"Review {self.pk} ({self.rating})"
