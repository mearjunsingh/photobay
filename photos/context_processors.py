from .models import Category

# def title(request):
#     return {
#         'cms_title' : settings.CMS_TITLE,
#         'cms_slogan' : settings.CMS_SLOGAN
#     }

def category(request):
    cats = Category.objects.all()[:5]
    return {'cat_menu' : cats}

# def sidebars(request):
#     form = FollowerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Email Subscribed Succesfully')
#         form = FollowerForm()
#     trending = Post.objects.all().order_by('-Post_Views')[:5]
#     editor = Post.objects.all().order_by('Post_Views')[:5]
#     return {
#         'trending' : trending,
#         'editor' : editor,
#         'form' : form,
#         'fb_link' : settings.FACEBOOK_USERNAME,
#         'tw_link' : settings.TWITTER_USERNAME,
#         'in_link' : settings.INSTAGRAM_USERNAME
#     }