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
import time
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# @api_view(['GET'])

def cropper(base64image):
    print("entered cropper")
    #Author:@Sirish Prabakar
    #Project:Final Project- CSC 230

    import numpy as np
    import cv2

    from PIL import Image
    from io import BytesIO
    import base64

    # Convert Image to Base64 
    def im_2_b64(image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        buff = BytesIO()
        image.save(buff, format="JPEG")
        img_str = base64.b64encode(buff.getvalue())
        return img_str

    # Convert Base64 to Image
    def b64_2_img(data):
        buff = BytesIO(base64.b64decode(data))
        img=Image.open(buff)
        cv_image = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        return cv_image

    #trial base 64 inputs: input64 for blue sign, this is for testing only, actualy base 64 values should be directly inserted into this program from the calling function


    #bg and input64 are inputs to this whole program
    #----------------------------------------------------------------------------------
    image = b64_2_img(base64image)
    #----------------------------------------------------------------------------------



    import numpy as np
    import cv2
    result = image.copy()
    print("completed img copy")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    print("completed cv2 color")
    lower = np.array([0, 0, 0])
    upper = np.array([255, 255, 245])
    mask = cv2.inRange(image, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    print("completed cv2 getStructuringElement")
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)
    print("completed cv2 morphologyEx")
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    boxes = []
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        boxes.append([x,y, x+w,y+h])
    print("completed cv2 rect formation")
    boxes = np.asarray(boxes)
    left = np.min(boxes[:,0])
    top = np.min(boxes[:,1])
    right = np.max(boxes[:,2])
    bottom = np.max(boxes[:,3])
    result[close==0] = (235,243,232)
    print("forming ROI")
    ROI = result[top:bottom, left:right].copy()
    print(" ROI complete")
    cv2.rectangle(result, (left,top), (right,bottom), (36, 255, 12), 2)
    print("cv2 rect on result ROI")
    cv2.imshow('ROI', ROI)
    print(" ROI displayed")
    #cv2.imshow('close', close)
    #cv2.imwrite('result.png', result)
    #cv2.imwrite('ROI.png', ROI)
    cv2.waitKey(1)
    # cv2.destroyWindow('ROI')
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.waitKey(1)
    # cv2.waitKey(1)
    # cv2.waitKey(1)
    #----------------------------------------------------------------------------------
    final_64=im_2_b64(ROI)
    # print(final_64)
    #return final_64
    #----------------------------------------------------------------------------------
    print("completed cropper")
    return final_64
	
def SaveDrawnImageView(request, base64image):
    print ("Old image")
    # base64image=base64image.replace(r'/^data:image\/(png|jpg);base64,/', "")
    print (base64image)
    base64image_new = cropper(base64image);
    print ("New image")
    print (base64image_new)
    current_user = request.user    
    profile_detail = Profile.objects.get(user=current_user)
    profile_detail.signature_store=base64image_new
    profile_detail.save()
    return HttpResponse({"response":{"result":1,"Message":"Poll Entered Successfully."}})
