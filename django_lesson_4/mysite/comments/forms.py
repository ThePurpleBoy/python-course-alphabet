from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        labels = {
            'author': 'Who are you?',
        }
        widgets = {'author': forms.HiddenInput(),
                   'article': forms.HiddenInput(),
                   'pub_date': forms.SplitHiddenDateTimeWidget()}

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False
        self.fields['article'].required = False



