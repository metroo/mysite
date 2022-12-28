from django.shortcuts import render, redirect , get_object_or_404
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
        user_permissions_list = list(Permission.values_list('id', 'headline').objects.filter(Q(user=request.user) , content_type_id=id))
        p1 = Permission.objects.filter(content_type_id=id)
        p3=list(user.get_user_permissions())
        p2=p3[1]
        p4=user.has_perm('embedContent.test22')
        return render(request, 'index.html', {'todos' : p1})
    else:
        return redirect(to='login')