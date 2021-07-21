from django.db import models
from django.contrib.auth.models import User
from django.core import validators
# Create your models here.
class PickList(models.Model):
	picklist_key = models.CharField(verbose_name="Pick List Key", null=False, max_length=20)
	# sub_picklist_id = models.DateField(verbose_name="Date of birth", default=null)
	# created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
	# updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)
	# picklist_item_key = models.TimeField(verbose_name="Time of birth")
	# picklist_parent_id = models.ForeignKey(City, verbose_name='Place of birth', related_name="placeOfBirth", null=1, on_delete=models.CASCADE)
	# is_active = models.CharField(verbose_name="Address", null=False, max_length=255)
	# deleted_at = models.ForeignKey(Country, verbose_name='Country', related_name="country", null=False, on_delete=models.CASCADE)
	
	class Meta:
		db_table = "pick_list"
		verbose_name = "Pick List"
		verbose_name_plural = "Pick Lists"

	def __str__(self):
		return f'{self.id}'
