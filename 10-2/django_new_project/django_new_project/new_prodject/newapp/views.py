
import os
from django.shortcuts import render, redirect
from .forms import AuthorsForm, QuotesForm
from django.contrib.auth.decorators import login_required
from .conect_to_mongodb import db


# Create your views here.
quotes =  db.quotes 
author = db.author

def main(request):
    return render(request, 'newapp/index.html')


def author (request, author_url):
#     db = uri.quotes_db
    author_name = author_url.replace('%20', ' ')
    author = author.find_one({'fullname': author_name})
    return render(request, 'newapp/author.html', context={'author': author})

def quotes(request):
    quotes = quotes.objects.all()

    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            new_quotes = form.save()

            choice_quotes = quotes.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_quotes.iterator():
                new_quotes.quotes.add(quotes)

            return redirect(to='newapp:main')
        else:
            return render(request, 'newapp/quotes.html', {"quotes": quotes, 'form': form})

    return render(request, 'newapp/quotes.html', {"quotes": quotes, 'form': QuotesForm()})

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




