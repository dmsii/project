from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

class BlogProjectIndexView(ListView):
	template_name='blog/project_index.html'
	context_object_name='blog'
	model=Post
	context={}
	def get(self, request):
	    self.context['project']= self.model.objects.all().order_by('-published_date')
	    return render(request, self.template_name, {self.context_object_name:self.context})





