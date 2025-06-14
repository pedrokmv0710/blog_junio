from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post-list.html'  # Specify your template name here

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')  # Order posts by creation date, newest first