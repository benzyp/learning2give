
"""
Definition of admin role views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Cause
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def admin_causes(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin/causes.html',
        {
            'title':'Cause Page',
            'year':datetime.now().year,
            'causes':Cause.nodes.all(),
        }
    )


    