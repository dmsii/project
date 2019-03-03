from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post

class BlogProjectIndexView(ListView):
	template_name='blog/project_index.html'
	context_object_name='blog'
	model=Post
	queryset={}
	def get(self, request):
		self.queryset['project']= self.model.objects.all().order_by('-published_date')
		return render(request, self.template_name, {self.context_object_name:self.queryset})

		

		
