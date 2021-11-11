from django.shortcuts import render

from django.http import HttpResponse

from .models import MainMenu
from .forms import BookForm
from django.http import HttpResponseRedirect
from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    print(book.name)
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    print(book.name)
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  }
                  )

def aboutus(request):
    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def searchbooks(request):
    submitted = False
    books = Book.objects.all()
    search = request.POST.get('search')
    for b in books:
        b.pic_path = b.picture.url[14:]

    if request.method == 'POST':
        return HttpResponseRedirect('/searchbooks?submitted=True&search=' + search)
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/searchbooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'books': books,
                      'search': search,
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def wishlist(request):
    wish = Wishlist.objects.all()
    book = Book.objects.all()

    return render(request,
                  'bookMng/wishlist.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'wish': wish,
                      'book': book,

                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def wishlist_add(request, book_id):
    books = Book.objects.filter(username=request.user)
    print(book.name)
    return render(request,
                  'bookMng/wishlist_add.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def wishlist_remove(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/wishlist_remove.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )
