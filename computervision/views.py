from django.shortcuts import render
from django.conf import settings
import os
from cv_models import super_resolution as sr


# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def super_resolution(request):
	saved_image=None


	lr_image = sr.preprocess_image(IMAGE_PATH)

	model = sr.load_model()
	start = time.time()
	gen_image = model(lr_image)
	gen_image = tf.squeeze(gen_image)
	print("Time Taken: %f" % (time.time() - start))
	
	# if request.GET.get('comment', False) is not False:
	# 	path = os.path.join(settings.MEDIA_ROOT,'text_2_hand.png')
	# 	kit.text_to_handwriting(request.GET['comment'],save_to=path)

	# 	saved_image=path


	return render(request, 'super_resolution.html', {'image': saved_image})
