"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from app.forms import RecordForm
from app.models import Record


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    records = Record.objects.all()
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'records': records
        }
    )


def upload_file(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RecordForm()
    return render(request, 'load.html', {'form': form})