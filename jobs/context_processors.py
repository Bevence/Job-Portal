from django.shortcuts import render
from jobs.models import Category, Jobs


def categories(request):
    category_list = Category.objects.all()
    print(category_list)
    return{"categories": category_list}


def jobs(request):
    jobs_list = Jobs.objects.all()
    job_count = Jobs.objects.count()
    # print(job_count)
    return {"jobs": jobs_list, "job_count" : job_count}
