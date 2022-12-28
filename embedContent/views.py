from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import EmbedContent
from django.db.models import Q
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        content_type = ContentType.objects.get_for_model(EmbedContent)
        id = content_type.id
        user_permissions_list = list(Permission.objects.values_list('codename',  flat=True).filter(Q(user=request.user), content_type_id=id))
        p1 = EmbedContent.objects.filter(Q(slug__in=user_permissions_list))
        #p1 = Permission.objects.filter(content_type_id=id)
        #p3=list(user.get_user_permissions())
        #p2=p3[1]
        #p4=user.has_perm('embedContent.test22')

        return render(request, 'index.html', {'todos' : p1})
    else:
        return redirect(to='login')


def detail(request , todo_id):
    todo = EmbedContent.objects.get(id = todo_id)
    return render(request , 'detail.html',{'todo' :todo})