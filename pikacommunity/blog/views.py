from django.shortcuts import render
from django.views.generic.base import View
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import ObjectDoesNotExist
from .models import BlogTag,Blog
from .forms import BlogPulishForm  
from utils.mixin_utils import LoginRequiredMixin


class BlogHomeView(View):
    def get(self,request):
        tag_id = request.GET.get('tag',0)
        sort = request.GET.get('sort','')
        blog_tags = BlogTag.objects.all()
        blog_list = Blog.objects.all()
        tag = None
        if tag_id:
            tag = BlogTag.objects.get(id=tag_id)
            blog_list = blog_list.filter(tag=tag)

        if sort == 'hot':
            blog_list = blog_list.order_by('-click_num')
        else:
            blog_list = blog_list.order_by('-create_time')
        return render(request,'blog_home.html',{
            'blog_list': blog_list,
            'blog_tags': blog_tags,
            'blog_tag': tag,
            'sort':sort
        })


class BlogDetailView(View):
    def get(self,request,blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Exception:
            raise Http404('Blog does not exist')
        return render(request,'blog_detail.html',{
            'blog':blog,
        })


class BlogPulishView(LoginRequiredMixin,View):
    def get(self,request):
        form = BlogPulishForm()
        blog_tag = BlogTag.objects.all()
        return render(request,'blog_publish.html',{
            'publish_form':form,
            'tags':blog_tag,
        })

    def post(self,request):
        blog_form = BlogPulishForm(request.POST)
        tags_str = request.POST.get('tags',0)
        tags_int = tags_str.split(',')
        tag_list = []
        for i in tags_int:
            tag_list.append(int(i))
        if blog_form.is_valid():
            title = request.POST.get('title','')
            content = blog_form.cleaned_data['blog_content']
            new_blog = Blog()
            new_blog.name = title
            new_blog.content = content
            new_blog.author = request.user
            new_blog.save()
            new_blog.tag.set(tag_list)
            return HttpResponseRedirect(reverse('blog_home'))
        else:
            return render(request,'blog_publish.html',{'msg':'发表出错'})



