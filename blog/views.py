from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.order_by('-created_date')
    #从posts中拿出所有的行，并根据created_date逆序排列
    #select * from posts order by created_date DESC
    #[post1,post2,post3]
    return render(request, 'blog/post_list.html', {'posts': posts})


def show(request,post_id):
	post= get_object_or_404(Post,pk=post_id)#pk:主键
	return render(request, 'blog/post_detail.html', {'post': post})

