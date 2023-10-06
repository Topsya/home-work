
import os
from django.shortcuts import render, redirect
from .forms import AuthorsForm, QuotesForm
from django.contrib.auth.decorators import login_required
from .conect_to_mongodb import db
from django.core.paginator import Paginator

# Create your views here.

def main(request):
    return render(request, 'newapp/index.html')

def quotes (request, page=1):
#     db = uri.quotes_db
    quotes = db.quotes.find()
    # print (quotes)
#     per_page = 10
    # paginator = Paginator(list(quotes))#, per_page)
#     quotes_on_page = paginator.page(page)
    return render(request, 'quotes_app/index.html', context={'quotes': quotes })


def author (request, author_url):
#     db = uri.quotes_db
    author_name = author_url.replace('%20', ' ')
    author = db.author.find_one({'fullname': author_name})
    return render(request, 'quotes_app/author.html', context={'author': author})

@login_required
def author_add(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='newapp:quotes')
        else:
            return render(request, 'newapp/author_add.html', {'form': form})

    return render(request, 'newapp/author_add.html', {'form': AuthorsForm()})
 
@login_required
def quotes_add(request):
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()
            return redirect(to='newapp:quotes')
        else:
            return render(request, 'newanewpp/quote_add.html', {'form': form})
    return render(request, 'newapp/quote_add.html', {'form': QuotesForm()})




