from django import forms
from .models import Posting, Reply

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        # fields = '__all__'
        exclude = ('user', )


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        # fields = '__all__'
        fields = ('content', )
        # exclude = ('posting', )

        