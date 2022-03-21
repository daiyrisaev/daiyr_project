from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=200)


    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


    def __str__(self):
        return self.name


class Publication(models.Model):
    category=models.ForeignKey(to=Category,null=True, on_delete=models.SET_NULL,)
    name=models.CharField(max_length=220)
    description=models.TextField(max_length=250)
    poster=models.ImageField(upload_to='publication_images',
                               null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return self.name


class EmailUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    text = models.TextField()

    class Meta:
        verbose_name = 'пользаватель'
        verbose_name_plural = 'пользаватели'

    def __str__(self):
        return self.name
