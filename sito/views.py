from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail
# Create your views here.


def index(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    slider_list = Slider.objects.filter(active = '1').order_by('id')
    chisiamo = Page.objects.get(pk=1)
    biomed = Page.objects.get(pk=2)
    dentale = Page.objects.get(pk=3)
    context = {'slider_list': slider_list,
    			'chisiamo': chisiamo,
    			'biomed': biomed,
    			'dentale': dentale,
                'language': language,
                'session_language': session_language}
    return render(request, 'index.html', context)
	#return render_to_response('index.html', context_instance=RequestContext(request))


### contact
def contact(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'Messaggio dal Sito Internet www.pmdbiomedical.com'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/success/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    context = {'language': language,
                'session_language': session_language}

    #return render_to_response('contact.html', {'form': form,})
    return render_to_response('contact.html', context, context_instance=RequestContext(request))



def success(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    context = {'language': language,
                'session_language': session_language}
    return render_to_response('success.html', context, context_instance=RequestContext(request))



### setting language session
def language(request, language='it'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	request.session['lang'] = language
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))