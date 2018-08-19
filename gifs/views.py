from django.shortcuts import HttpResponse
from django.template import loader
from .models import Gif

def index(request):
	most_viewed_gifs = Gif.objects.order_by('-contador')[:10]
	template = loader.get_template('index.html')
	context = {
		'most_viewed_gifs': most_viewed_gifs,
	}
	return HttpResponse(template.render(context, request))
