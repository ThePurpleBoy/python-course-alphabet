from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Profile
from .forms import ProfileForm


class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        # Create profile
        profile = Profile.objects.create(user=created_user)
        # Authenticate User
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('profile', profile.id)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "account/profile_update.html"
    form_class = ProfileForm
    pk_url_kwarg = 'profile_id'

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.user.username = request.POST['user']
        profile.user.save()
        profile.bio = request.POST['bio']
        profile.location = request.POST['location']
        profile.save()
        return HttpResponseRedirect(reverse('profile', args=(profile.id,)))

    def get_form_kwargs(self):
        kwargs = super(ProfileUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs