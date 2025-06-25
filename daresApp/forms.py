from django import forms
from .models import Votes

class VoteForm(forms.ModelForm):

    class Meta:

        model=Votes
        fields="__all__"
        labels={
            "image_id":"Image Id",
            "image_file":"Contestant Photo",
            "Category":"Gender",
            "votes":"Loved By",
        }
        wigdets={

            "Image Id":forms.IntegerField(),
            "image_file":forms.ImageField(),
            "votes":forms.IntegerField()
        }