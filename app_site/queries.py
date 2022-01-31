from .models import *


def get_first_image():
    return Image.objects.first()


def get_all_blogs():
    return Blog.objects.all()


def get_all_images():
    return Image.objects.all()


def get_blog(pk: int):
    try:
        blog = Blog.objects.get(pk=pk)
        return blog
    except Blog.DoesNotExisit:
        print('Object blog does not exsist')


def get_img(img_id: int):
    try:
        img = Image.objects.get(pk=img_id)
        return img
    except Image.DoesNotExist:
        print('Object image does not exsist')
