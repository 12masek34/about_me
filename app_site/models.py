from django.db import models


class Image(models.Model):
    title = models.CharField('Заголовок', max_length=255, blank=True, null=True)
    img = models.ImageField('изображение', upload_to='image/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата согдания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    img = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
