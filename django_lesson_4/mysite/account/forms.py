from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    user = forms.CharField(label='Name', widget=forms.TextInput(attrs={'maxlength': 150}))
    bio = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.initial['user'] = user.username

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'location')
