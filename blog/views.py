from django.shortcuts import render
from .models import Post, FileTest

def index(request):
	return render(request, 'index.html')
# Create your views here.

def view_all(request):
	posts = Post.objects.all()
	return render(request, 'view_all.html', {'posts' : posts})

def view(request, post_id):
	post = Post.objects.get(id = post_id)
	return render(request, 'view_post.html', {'post' : post})

def add(request):
	if request.method == 'POST':
		title = request.POST['title']
		story = request.POST['post']
		new_post = Post(title = title, story = story)
		new_post.save()
		return render(request, 'add.html', {'success' : True, 'post' : new_post})
	return render(request, 'add.html')

def UploadFile(request):
	if request.method == 'POST':
		new_file = request.FILES['file']
		new_model = FileTest(f = new_file)
		new_model.save()
		return render(request, 'file.html', {'success' : True})
	return render(request, 'file.html')