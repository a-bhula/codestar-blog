from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`

    **Template context processors:**
    - :func:`django.contrib.auth.context_processors.auth`
    - :func:`django.template.context_processors.debug`
    - :func:`django.template.context_processors.i18n`
    - :func:`django.template.context_processors.media`
    - :func:`django.template.context_processors.static`
    - :func:`django.template.context_processors.tz`
    **Template tags:**
    - :template:`blog/post_detail.html`
    **Template filters:**
    - :filter:`date`
    - :filter:`time`
    **Template variables:**
    - ``post``
        An instance of :model:`blog.Post`.
    - ``comments``
        A queryset of comments related to the post, ordered by creation date.
    - ``comment_count``
        The total number of approved comments for the post.
    - ``comment_form``
        An instance of :class:`blog.forms.CommentForm` for submitting new comments.
    **Example usage:**
    To display a post with its comments and a form to submit new comments, use the following in your template:  
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
            )   

    comment_form = CommentForm()
    print("About to render template")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    :param request: The HTTP request object.
    :param slug: The slug of the post to which the comment belongs.
    :param comment_id: The ID of the comment to be edited.
    :return: Redirects to the post detail page after editing the comment.
    :rtype: HttpResponseRedirect
    :raises: None
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    :param request: The HTTP request object.
    :param slug: The slug of the post to which the comment belongs.
    :param comment_id: The ID of the comment to be deleted.
    :return: Redirects to the post detail page after deleting the comment.
    :rtype: HttpResponseRedirect
    :raises: None
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))