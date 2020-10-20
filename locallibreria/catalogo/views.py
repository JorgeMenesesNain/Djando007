from django.shortcuts import render
from . models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    num_Books = Book.objects.all().count()
    num_Instances = BookInstance.objects.all().count()

    num_Instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_Books, 'num_instances': num_Instances, 
        'num_instances_available': num_Instances_available, 'num_authors': num_authors},
    )




class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book
