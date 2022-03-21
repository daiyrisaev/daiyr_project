from django.contrib import admin

from apps.marketplace.models import Category, Publication, EmailUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailUser)
class EmailUserAdmin(admin.ModelAdmin):
    pass
