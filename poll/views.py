# Create your views here.
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response , get_object_or_404
from poll.models import Poll, Choice, Person
from poll.forms import ContactForm, ContactForm1
from django.core.mail import send_mail
from django.template import RequestContext, Context
import pdb

from django.core.mail import send_mail, BadHeaderError

'''def index(request):
    poll_list = Poll.objects.all()
    return render_to_response('poll/index.html', {'poll_list': poll_list}
'''
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    p = Poll.objects.get(id=poll_id)
    choice_list = p.choice_set.all()
    return render_to_response('poll/detail.html', {'choice_list': choice_list, 'poll':p})
    
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def contact(request):
    #pdb.set_trace()
    if request.method == 'POST':
        form = ContactForm1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thankyou')) #'thankyou is a name given in urls.py ,if u dont use the name then give path poll/thankyou without reverse
    else:
        form = ContactForm1()
    return render_to_response('poll/contact.html', {'form': form}, context_instance=RequestContext(request)) #context here refers to a dict{form:form} csrf token
		

def thankyou(request):
    return render_to_response('poll/thankyou.html')
