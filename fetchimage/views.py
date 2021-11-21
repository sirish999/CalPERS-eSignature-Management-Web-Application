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
	
def FetchImageView(request):
	current_user = request.user
	profile_detail = Profile.objects.get(user=current_user)
	tempstring = profile_detail.signature_store[2:]
	print(tempstring)
	if 'iVBORw0KGgo' in tempstring[:11]:
		final= "data:image/png;charset=utf-8;base64,"+str(tempstring[:-1])
		content= json.dumps({'base64link': final})
		return HttpResponse(content)
	elif '/9j' in tempstring[:3]:
		final= "data:image/jpeg;charset=utf-8;base64,"+str(tempstring[:-1])
		content= json.dumps({'base64link': final})
		return HttpResponse(content)
	else:
		final= ""
		content= json.dumps({'base64link': final})
		return HttpResponse(content)



 