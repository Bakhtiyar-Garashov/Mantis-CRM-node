from django.db import models
from django.db.models.aggregates import Max

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class General(models.Model):
    address = models.CharField(max_length=150)
    image = models.FileField(null=True, blank=True)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    company = models.OneToOneField(
        Company, related_name="company_general", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "General information"
        verbose_name_plural = "General informations"

    def __str__(self):
        return self.company.name+"'s general info"


class Code(models.Model):
    code = models.CharField(max_length=10)
    general_info = models.ForeignKey(
        General, related_name="general_codes", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Code"
        verbose_name_plural = "Codes"


class Type(models.Model):
    company = models.ForeignKey(
        Company, related_name='company_type', on_delete=models.CASCADE)
    industry = models.CharField(max_length=150)
    notes = models.TextField()

    class Meta:
        verbose_name = "Company type"
        verbose_name_plural = "Company types"


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="company_contact_info", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(max_length=250)
    company_representative = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Contact detail"
        verbose_name_plural = "Contact details"


class Notes(models.Model):
    company = models.ForeignKey(
        Company, related_name="company_notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    activity_description = models.CharField(max_length=100)
    note_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
