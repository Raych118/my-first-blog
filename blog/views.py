from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
	return render(request, 'blog/post_list.html', {})

