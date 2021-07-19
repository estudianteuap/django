from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic
from netmiko import ConnectHandler

# Create your views here.
class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    

class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

class ResultsView(generic.DetailView):
    module=Question
    template_name="polls/results.html"


def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',
        {'question':question,'error_message':'You didnt select a choice'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def router(request):
    sshCli = ConnectHandler(
        device_type="cisco_ios",
        host="192.168.56.102",
        port=830,
        username="cisco",
        password="cisco123!"
    )
    output=sshCli.send_command("show ip interface brief")
    return HttpResponse("output")
