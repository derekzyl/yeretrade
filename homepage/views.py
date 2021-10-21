from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View

from core.models import Plans
from homepage.forms import Contact, News
from homepage.models import Transaction, Withdrawal, Blog, TopInvestor, Comment, TeamMembers, Slider


#blog
class Home(View):
    def get(self, *args, **kwargs):
        plan = Plans.objects.all()
        blog = Blog.objects.all()
        transaction= Transaction.objects.all()
        withdrawal = Withdrawal.objects.all()
        top_investor = TopInvestor.objects.all()
        comment = Comment.objects.all()
        team_members = TeamMembers.objects.all()
        new = News()
        slider = Slider.objects.all()
        context ={
        'plan': plan,
        'blog': blog,
        'transaction': transaction,
        'withdrawal': withdrawal,
            'new': new,
            'top_investor':top_investor,
            'comment': comment,
            'team_members': team_members,
            'slider': slider

        }

        return render(self.request, 'homepage/index.html', context)


def blog(request):
    blog= Blog.objects.all()
    context={
        'blog': blog
    }
    return render(request, 'homepage/blog.html', context)


def about(request):
    team_members = TeamMembers.objects.all()
    context ={
        'team_members':team_members
    }

    return render(request, 'homepage/about.html', context)


class blogdetails(View):
    def get(self, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=kwargs['slug'])
        context= {
            'blog': blog
        }
        return render(self.request, 'homepage/blog-details.html', context)

class Contact(View):
    def get(self, *args, **kwargs):
        form = Contact()
        context = {
        'form' : form
     }
        return render(self.request, 'homepage/contact.html', context)


def plan(request):
    plan = Plans.objects.all()
    context ={
        'plan':plan
    }
    return render(request, 'homepage/plan.html', context)


def terms(request):
    return render(request, 'homepage/termsandcondition.html')

def privacy(request):
    return render(request, 'homepage/privacyandpolicy.html')

def certificate(request):
    return render(request, 'homepage/license.html')