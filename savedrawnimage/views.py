from apps.common.forms import SignUpForm, UserForm, ProfileForm
from apps.userprofile.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
import datetime
# from rest_framework.decorators import api_view
# def get_queryset(self):
#         return Userproject.objects.filter(user=self.request.user)
# def SaveDrawnImageView(request):
# 	return HttpResponse(get_queryset(self))
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# @api_view(['GET'])

# def blah(base64image):
# 	# ml code
# 	return base64image
	
def SaveDrawnImageView(request, base64image):
    # base64image = blah(base64image);


    current_user = request.user
    
    # profile_form = Profile(user=current_user, signature_store=base64image)

    profile_detail = Profile.objects.get(user=current_user)
    profile_detail.signature_store='bb'+base64image
    profile_detail.save()
    print(current_user)
    print(base64image)
    return HttpResponse( {"response":{"result":1,"Message":"Poll Entered Successfully."}})
    # messages.success(request, 'Your signature was successfully updated!')


 #    b4 = Blog(id=3, name='Not Cheddar', tagline='Anything but cheese.')
	# b4.save() 
    # return HttpResponse(html)
# def get_queryset(self):
#     return Userproject.objects.filter(user=self.request.user)
# def get_success_url(self):
#         user_id = self.request.user.id # Get user_id from request
#         return reverse_lazy('git_project:user_profile', kwargs={'id': user_id})
# Create your views here.
# class SaveDrawnImageView(LoginRequiredMixin, TemplateView):
#     # user_form = UserForm
#     # profile_form = ProfileForm
#     # template_name = 'common/profile-update.html'
#     # def savetodb(request, base64image):
# 	# html = "<html><body>It is now .</body></html>"
#     return HttpResponse("<html><body>It is now .</body></html>")


    # def post(self, request):

    #     post_data = request.POST or None
    #     file_data = request.FILES or None

    #     user_form = UserForm(post_data, instance=request.user)
    #     profile_form = ProfileForm(
    #         post_data, file_data, instance=request.user.profile)

    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         messages.success(request, 'Your profile was successfully updated!')
    #         return HttpResponseRedirect(reverse_lazy('profile'))

    #     context = self.get_context_data(
    #         user_form=user_form,
    #         profile_form=profile_form
    #     )

    #     return self.render_to_response(context)

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.request.user.id)
    #     context['book_list'] = self.request.user
    #     return context