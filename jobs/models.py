from django.db import models
import datetime
from django_countries.fields import CountryField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    


class Jobs(models.Model):
    JOBTYPES = (('Full Time', 'Full Time'), ('Part Time', 'Part Time'),
                ('Temporary', 'Temporary'), ('Free Lance', 'Free Lance'), ('Internship', 'Internship'))
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True)
    company = models.CharField(max_length=50)
    company_website = models.CharField(max_length=50, null=True)
    country = CountryField(blank_label='Select Country')
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=10, choices=JOBTYPES)
    no_of_vacancies = models.IntegerField(default=1)
    experience = models.CharField(max_length=5, help_text="In years")
    salary = models.CharField(
        max_length=10, default="Negotiable", help_text="Per Month")
    responsibilities = models.TextField()
    key_skills = models.TextField()
    job_description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    last_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug":self.slug})
