from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from appfolio.models import Post, PostCategory
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

# Create your views here.

def welcome(request):
    
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'portfolio/index.html', context)


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

def post_detail(request, pk):
    template = 'portfolio/post-detail.html'
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    post_id = Post.objects.get(pk=pk)
    
    nextpost = Post.objects.filter(pk__gt=post_id.id).order_by('pk').first()
    prevpost = Post.objects.filter(pk__lt=post_id.id).order_by('pk').last()


    context = {
        'post' : post,
        'posts': posts,
        'nextpost' : nextpost,
        'prevpost' : prevpost,
    }

    return render(request, template , context)

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'portfolio/post-detail.html'
#     paginate_by = 2

#     def get_context_data(self, **kwargs):
#         object_list = Post.objects.filter(title=self.object)
#         context = super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
#         return context


class Category(ListView):

    model = Post
    template_name = 'portfolio/categories.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(PostCategory, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(Category, self).get_context_data(**kwargs)
        context['category'] = self.category 
        return context

