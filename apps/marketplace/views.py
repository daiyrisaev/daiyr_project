from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from apps.marketplace.models import Publication, EmailUser

from apps.marketplace.forms import UserCommentForm


class PublicationListView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['publication_list'] = Publication.objects.all()
        return context


# def show_all_my_comment(request):
#     if request.method == 'GET':
#         user_form = UserCommentForm()
#         response = render(request, 'index.html',
#                               context={'form': user_form})
#         return response
#     elif request.method == 'POST':
#         print(request.POST)
#         EmailUser.objects.create(name=request.POST['name'], email=request.POST['email'],text=request.POST['text'])
#         return HttpResponse('<h>вы подписались на рассылку</h1>', status=201)

def show_all_my_comment(request):
    if request.method == 'POST':
        post_request = request.POST  # type dictionary  {'name': 'Имя которое ввел юзер',...
        email_form = UserCommentForm(post_request)
        if email_form.is_valid():
            comment = EmailUser.objects.create(
                text=email_form.data['text'],
                name=email_form.data['name'],
                email=email_form.data['email']
                )
            return HttpResponse(content='данные успешно отпрвлены.')
        else:
            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {email_form.errors}')

