from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from appfolio.models import Post

# Create your views here.
def welcome(request):
    return render(request, 'portfolio/index.html')


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['sujet']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['talbotdfn@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "portfolio/email.html", {'form': form})

def successView(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/appfolio/portfolio/')

def articleView(request):
    return render(request, 'portfolio/articles.html')

def test(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'portfolio/test.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post' : post,
    }
    return render(request, 'portfolio/post-detail.html', context)