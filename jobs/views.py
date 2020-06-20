from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from jobs.models import Jobs, Category
from django.views.generic import TemplateView, DetailView
# Create your views here.

class JobsTemplateView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        category_jobs_list = {}
        for i, category in enumerate(categories):
            category_jobs_list[i] = Jobs.objects.filter(category=category).count()
        context["recent_jobs"] = Jobs.objects.all().order_by("-posted_on")
        context["category_jobs_list"] = category_jobs_list
        print(category_jobs_list)
        return context


class CategoryJobsView(View):
    def get(self, request, category_slug, *args, **kwargs):
        template_name = "jobs/categories.html"
        category = get_object_or_404(Category, slug = category_slug)
        category_jobs_list = Jobs.objects.filter(category=category).order_by("-posted_on")
        return render(
            request, template_name, {"category_jobs_list":category_jobs_list, "category":Category}
        )

class JobDetailView(DetailView):
    model = Jobs
    template_name = "jobs/job_detail.html"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = Jobs.objects.all() 
        return context
    
