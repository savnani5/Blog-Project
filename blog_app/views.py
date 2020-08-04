# File to create the visual views on the website

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, RelatedPost, Subscription
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import PostForm, SubscriptionForm

# blog_app > templates > blog_app > .html files


# # Create your views here.
# def home(request):
#     context = {
#         'posts': Post.objects.all()             # to query data from data base
#         }
#     # It is a necessity to pass dictionary as third argument
#     return render(request, 'blog_app/home.html', context)   # render returns the Http Response using the template of home.html

class PostListView(ListView):

    # django class based views attributes(stick to conventions)
    model = Post
    template_name = 'blog_app/home.html'  # default naming convention if u dont want to use custom: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'# default name object if u do not want to use custom
    ordering = ['-date_posted']  # to order the blog posts using dates
    paginate_by = 4

    def post(self, request,  *args, **kwargs):
        email_id = request.POST.get("email_id")
        Subscription.objects.create(email= email_id)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         context = super(PostListView, self).get_context_data(**kwargs)
         context['RelatedPost'] = RelatedPost.objects.all()
         return context

class UserPostListView(ListView):

    # django class based views attributes(stick to conventions)
    model = Post
    template_name = 'blog_app/user_posts.html'  # default naming convention if u dont want to use custom: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'# default name object if u do not want to use custom
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):

    # django class based views attributes(stick to conventions)
    model = Post
    context_object_name = 'posts'
    # here we use default template name and default context_object_name

class PostCreateView(LoginRequiredMixin, CreateView):

    # django class based views attributes(stick to conventions)
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'image']       # use only if modelform is not created
    # here we use default template name and default context_object_name

    # to validate if user is there or not
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # django class based views attributes(stick to conventions)
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'image']       # use only if modelform is not created
    # here we use default template name and default context_object_name

    # to validate if user is there or not
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # to prevent other users to update anyone else's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(DeleteView):

    # django class based views attributes(stick to conventions)
    model = Post
    success_url = '/'

    # to prevent other users to update anyone else's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    # return HttpResponse("<h1>About home</h1>")
    return render(request, 'blog_app/about.html', {"title": "About"})
