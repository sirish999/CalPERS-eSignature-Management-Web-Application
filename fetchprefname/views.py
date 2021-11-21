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
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json

# @csrf_exempt
# @api_view(['GET'])

# def blah(base64image):
# 	# ml code
# 	return base64image
	
def FetchPrefNameView(request):
	current_user = request.user
	print(current_user)
	profile_detail = Profile.objects.get(user=current_user)
	return(HttpResponse(json.dumps({'pref_name': profile_detail.pref_name})))

def SavePrefNameView(request, PreferredName):
	current_user = request.user
	print(current_user)
	profile_detail = Profile.objects.get(user=current_user)
	profile_detail.pref_name=PreferredName
	profile_detail.save()
	return HttpResponse({"response":{"result":1,"Message":"Poll Entered Successfully."}})



 