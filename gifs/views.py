from django.shortcuts import HttpResponse
from django.template import loader
from .models import Gif
import time

def index(request):
	start_time = time.time()
	most_viewed_gifs = Gif.objects.order_by('-contador')[:10]
	end_time = (time.time() - start_time)
	template = loader.get_template('index.html')
	context = {
		'most_viewed_gifs': most_viewed_gifs,
		'end_time': end_time,
	}
	return HttpResponse(template.render(context, request))
