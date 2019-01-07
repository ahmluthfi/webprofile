from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse


def index(request):
    return render(request, 'home.html', {'nama': 'Ahmad Luthfi', 'songs': '', 'status': '' })
