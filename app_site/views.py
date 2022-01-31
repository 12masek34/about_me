from django.shortcuts import render
from .models import *
from .queries import *


def index(request):
    img1 = get_first_image()
    blogs = get_all_blogs()
    imgs = get_all_images()
    context = {'img1': img1,
               'blogs': blogs,
               'imgs': imgs
               }
    return render(request, 'app_site/index.html', context=context)


def detail(request, pk):
    blog = get_blog(pk)
    if blog.img_id is not None:
        img = get_img(blog.img_id)
    else:
        img = False
    blogs = get_all_blogs()
    imgs = get_all_images()
    context = {'img': img,
               'blogs': blogs,
               'imgs': imgs,
               'blog': blog,
               'pk': pk
               }
    return render(request, 'app_site/detail.html', context=context)
