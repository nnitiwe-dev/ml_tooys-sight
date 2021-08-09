from django.shortcuts import render
from django.conf import settings
import os


import pywhatkit as kit


# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def super_resolution(request):
	saved_image=None

	# if request.GET.get('comment', False) is not False:
	# 	path = os.path.join(settings.MEDIA_ROOT,'text_2_hand.png')
	# 	kit.text_to_handwriting(request.GET['comment'],save_to=path)

	# 	saved_image=path


	return render(request, 'super_resolution.html', {'image': saved_image})
