from django.db import models
from django.core import validators

# Create your models here.
class Religion(models.Model):
    name = models.CharField(verbose_name="Religion Name", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "religion"
        verbose_name = "Religion"
        verbose_name_plural = "Religions"

    def __str__(self):
        return self.name


class Mothertongue(models.Model):
    name = models.CharField(verbose_name="Mother Tongue", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "mother_tongue"
        verbose_name = "Mother Tongue"
        verbose_name_plural = "Mother Tongues"

    def __str__(self):
        return self.name


class Caste(models.Model):
    name = models.CharField(verbose_name="Caste", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "caste"
        verbose_name = "Caste"
        verbose_name_plural = "Castes"

    def __str__(self):
        return self.name


class SubCaste(models.Model):
    name = models.CharField(verbose_name="Sub Caste", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "sub_cast"
        verbose_name = "Sub Caste"
        verbose_name_plural = "Sub Castes"

    def __str__(self):
        return self.name


class Gotra(models.Model):
    name = models.CharField(verbose_name="Gotra", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "gotra"
        verbose_name = "Gotra"
        verbose_name_plural = "Gotras"

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(verbose_name="Education", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "education"
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(verbose_name="Occupation", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "occupation"
        verbose_name = "Occupation"
        verbose_name_plural = "Occupations"

    def __str__(self):
        return self.name