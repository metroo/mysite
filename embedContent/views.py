from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import EmbedContent
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def home(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user.is_authenticated:
        content_type = ContentType.objects.get_for_model(EmbedContent)
        id = content_type.id
        p1 = Permission.objects.filter(content_type_id=id)

        return render(request, 'index.html', {'todos' : p1})
    else:
        return redirect(to='login')