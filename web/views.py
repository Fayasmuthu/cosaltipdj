from django.shortcuts import render ,redirect
from .models import BlogPost,Tag,gallery_photo,boxform,ReceptPost,Category
from .models import Comment
from .forms import CommentForm,ServiceForm
from django.contrib import messages
# from .models import EmailSubscription
# from .forms import EmailSubscriptionForm
from .forms import ContactForm
from .forms import SubscriptionForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SubscribeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




import json
from django.http import JsonResponse

# Create your views here.

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def about(request):
    # Your view logic here
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success message or redirection here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/about.html', {'form': ServiceForm()})
            # ...

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
            return render(request, 'details/blog.html')
            # ...
    else:
        form = ServiceForm()
        form = SubscriptionForm()

    context ={
        "is_about" : True,
        'form': form,
    }
    return render(request, 'details/about.html' , context)

def index2(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
        
            # You can add success messages or redirection logic here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/index-2.html')
            # ...
    else:
        form = SubscriptionForm()

    return render(request, 'details/index-2.html' , {'form': form})




def project(request):
    # Your view logic here
    return render(request, 'details/project.html')

def blog(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
         
            return render(request, 'details/blog.html')
            # ...

    else:
        form = SubscriptionForm()


    query = request.GET.get("q")
    categories = Category.objects.all()
    posts = BlogPost.objects.all()
    tags = Tag.objects.all()
    Rposts =ReceptPost.objects.all()[:3] # Assuming you want to retrieve the latest 3 posts

    if query:
        posts = BlogPost.objects.filter(title__icontains=query) | BlogPost.objects.filter(name__icontains=query)
    else:
        posts = BlogPost.objects.all()

    # Filter Recept objects based on the search query
    if query:
        Rposts =ReceptPost.objects.filter(title__icontains=query) | ReceptPost.objects.filter(name__icontains=query)
    else:
        Rposts =ReceptPost.objects.all()[:3]

        # Paginate both posts and Recept
    # post_paginator = Paginator(posts, 1)  # Show 10 posts per page
    # recept_paginator = Paginator(Rposts, 1)  # Show 10 Recept objects per page

    # post_page = request.GET.get('post_page')
    # recept_page = request.GET.get('recept_page')

    # try:
    #     posts = post_paginator.page(post_page)
    # except PageNotAnInteger:
    #     posts = post_paginator.page(1)
    # except EmptyPage:
    #     posts = post_paginator.page(post_paginator.num_pages)

    # try:
    #     Rposts = recept_paginator.page(recept_page)
    # except PageNotAnInteger:
    #     Rposts = recept_paginator.page(1)
    # except EmptyPage:
    #     Rposts = recept_paginator.page(recept_paginator.num_pages)


    context={
        'posts': posts,
        'tags': tags,
        'Rposts': Rposts,
        "is_blogs" : True,
        'categories': categories
   
    }
    
    # Your view logic here
    return render(request, 'details/blog.html',context)

from django.shortcuts import render, get_object_or_404

def blog_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = BlogPost.objects.filter(categories=category)
    categories = Category.objects.all()
    return render(request, 'details/blog.html', {'posts': posts, 'categories': categories})



# def contact(request):

#     if request.method == 'POST':
#         if "con" in request.POST:
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # You can add success message or redirection here
#                 messages.success(request, 'Thank you for your message!')
#                 return redirect(request, 'details/contact.html', {'form': ContactForm()})
#                 # ...

#         elif "mail" in request.POST:
#             formemail = MailForm(request.POST)
#             if formemail.is_valid():
#                 formemail.save()
#                 # You can add success message or redirection here
#                 messages.success(request, 'Thank you for your message!')
#                 return redirect(request, 'details/contact.html', {'form': MailForm()})
#                 # ...

#         else:
#             form = ContactForm()
#             formemail=MailForm()

#     context = {
#         'form': form,
#         "is_contacts" : True
        
#         }
#     return render(request, 'details/contact.html', context)




# def contact(request):
#     contact_form = ContactForm()
#     subscription_form = SubscriptionForm()

#     if request.method == 'POST':
#         if 'con' in request.POST:
#             contact_form = ContactForm(request.POST)
#             if contact_form.is_valid():
#                 contact_form.save()
#                 messages.success(request, 'Thank you for your message!')
#                 return redirect(request, 'details/contact.html')
#         elif 'mail' in request.POST:
#             subscription_form = SubscriptionForm(request.POST)
#             if subscription_form.is_valid():
#                 subscription_form.save()
#                 messages.success(request, 'Thank you for subscribing!')
#                 return redirect(request, 'details/contact.html')

#     context = {
#         'contact_form': contact_form,
#         'subscription_form': subscription_form,
#         'is_contacts': True,
#     }
#     return render(request, 'details/contact.html', context)


# def contact(request):
#     contact_form = ContactForm()
#     subscription_form = SubscriptionForm()
#     if request.method == 'POST':
#         if 'con' in request.POST:
#             contact_form = ContactForm(request.POST)
#             if contact_form.is_valid():
#                 contact_form.save()
#                 messages.success(request, 'Thank you for your message!')
#                 return redirect('details:contact')  # Use the correct syntax for redirecting to a URL name
        
#         elif 'mail' in request.POST:
#             subscription_form = SubscriptionForm(request.POST)
#             if subscription_form.is_valid():
#                 subscription_form.save()
#                 messages.success(request, 'Thank you for subscribing!')
#                 return redirect('details:contact')  # Use the correct syntax for redirecting to a URL name


#     context = {
#         'contact_form': contact_form,
#         'subscription_form': subscription_form,
#         'is_contacts': True,
#     }
#     return render(request, 'details/contact.html', context)

# def contact(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             response_data = {
#                 "status": "true",
#                 "title": "Successfully Submitted",
#                 "message": "Message successfully updated",
#             }
#         else:
#             print(form.errors)
#             response_data = {
#                 "status": "false",
#                 "title": "Form validation error",
#             }
#         return HttpResponse(
#             json.dumps(response_data), content_type="application/javascript"
#         )
#     else:
#         context = {
#             "is_contacts": True,
#             "form": form,
#         }
#     return render(request, "details/contact.html", context)

# def contact(request):
#     form = ContactForm(request.POST or None)
#     subscribe = SubscribeForm(request.POST or None)

#     if request.method == "POST":
#         if subscribe.is_valid():
#             subscribe.save()
#             messages.success(request, "Successfully saved")
#             return redirect('/')

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         messages.success(request,"succsessfully saved")
#         return redirect('/contact')
#     else:
#         context = {
#             "is_contact": True,
#             "form": form,
#             "subscribe": subscribe,

#         }
#     return render(request, "details/contact.html", context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm  # Import the SubscribeForm from your forms.py

def contact(request):
    
    subscribe = SubscribeForm(request.POST or None)
    form = ContactForm(request.POST)

    if request.method == "POST":
        
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully saved")
            return redirect('/contact')

    if request.method == "POST":
        if subscribe.is_valid():
            subscribe.save()
       
            return redirect('/')



    context = {
        "is_contacts": True,
        "form": form,
        "subscribe": subscribe,
    }

    return render(request, "details/contact.html", context)


# def contact(request):
#     form = ContactForm()
#     formemail = MailForm()

#     if request.method == 'POST':
#         if "con" in request.POST:
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Thank you for your message!')
#                 return redirect(reverse('contact'))
#         elif "mail" in request.POST:
#             formemail = MailForm(request.POST)
#             if formemail.is_valid():
#                 formemail.save()
#                 messages.success(request, 'Thank you for subscribing!')
#                 return redirect(reverse('contact'))

#     context = {
#         'form': form,
#         'formemail': formemail,
#         "is_contacts": True
#     }
#     return render(request, 'details/contact.html', context)


def project_details(request):
    # Your view logic here
    
    return render(request, 'details/project-details.html')

def blog_details(request):
    # Your view logic here
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_details')  # Redirect to a view that displays the list of comments
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
            return render(request, 'details/blog-details.html')
            # ...

    else:
        form = SubscriptionForm()  
        form = CommentForm()
    return render(request, 'details/blog-details.html',{'form': form})

def index3(request):
    # Your view logic here
    return render(request, 'details/index-3.html')

def index4(request):
    # Your view logic here
    return render(request, 'details/index-4.html')

def faq(request):
    # Your view logic here
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
            return render(request, 'details/blog.html')
            # ...
    else:
        form = SubscriptionForm()
    context ={
        "is_faqs" : True
    }
    return render(request, 'details/faq.html' , context)

def found(request):
    # Your view logic here
    return render(request, 'details/not-found.html')
def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success message or redirection here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/service.html', {'form': ServiceForm()})
            # ...
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success messages or redirection logic here
            return render(request, 'details/blog.html')
            # ...
  
    else:
        form = SubscriptionForm()
        form = ServiceForm()
    box = boxform.objects.all()
    
    context = {
        'form': form,
        'box' : box,
        "is_services": True
        }
   
    return render(request, 'details/service.html',context)

def service_details(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success message or redirection here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/service.html', {'form': ServiceForm()})
            # ...
    else:
        form = ServiceForm()

    context = {
        'form': form,
        
        }

   
    return render(request, 'details/service-details.html', context)

def team(request):
    # Your view logic here
    return render(request, 'details/team.html')

def dollar(request):
    # Your view logic here
    return render(request, 'details/$.html')

def gallery(request):
    # Your view logic here
    photo = gallery_photo.objects.all()
    context={
        'photo':photo,
        "is_gallerys": True
    }
    return render(request, 'details/gallery.html',context)

def tag(request):
    # Your view logic here
    return render(request, 'blog/tags.html')

def search(request):
    # Your view logic here
    return render(request, 'blog/search.html')

def paginations(request):
    # Your view logic here
    return render(request, 'blog/paginations.html')



def form_fields(request):
    # Your view logic here
    return render(request, 'details/form_fields.html')

def success(request):
    return render(request, 'sucess.html')