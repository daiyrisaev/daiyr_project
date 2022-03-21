from django import forms


class UserCommentForm(forms.Form):
    name= forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=False)
    text = forms.CharField(required=True, max_length=100)




