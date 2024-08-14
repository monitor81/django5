from django.shortcuts import render, redirect
from django.conf import settings
from .forms import BookForm
import os
import json

# def save_book_data(data):
#     # Определяем путь к папке и файлу
#     books_dir = os.path.join(settings.BASE_DIR, 'Books')
#     if not os.path.exists(books_dir):
#         os.makedirs(books_dir)
#     file_path = os.path.join(books_dir, 'books.xml')

#     # Если файл существует, добавляем данные, иначе создаем новый файл
#     if os.path.exists(file_path):
#         tree = ET.parse(file_path)
#         root = tree.getroot()
#     else:
#         root = ET.Element('Books')
#         tree = ET.ElementTree(root)

#     book = ET.Element('Book')
#     ET.SubElement(book, 'Author').text = data['author']
#     ET.SubElement(book, 'Title').text = data['title']
#     ET.SubElement(book, 'Pages').text = str(data['pages'])
#     ET.SubElement(book, 'Year').text = str(data['year'])
#     root.append(book)

#     tree.write(file_path, encoding='utf-8', xml_declaration=True)

# def book_form(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             save_book_data(form.cleaned_data)
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'books/book_form.html', {'form': form})

# def book_list(request):
#     books_dir = os.path.join(settings.BASE_DIR, 'Books')
#     file_path = os.path.join(books_dir, 'books.xml')
#     books = []

#     if os.path.exists(file_path):
#         tree = ET.parse(file_path)
#         root = tree.getroot()
#         for book in root.findall('Book'):
#             books.append({
#                 'author': book.find('Author').text,
#                 'title': book.find('Title').text,
#                 'pages': book.find('Pages').text,
#                 'year': book.find('Year').text
#             })

#     return render(request, 'books/book_list.html', {'books': books})

def save_book_data(data):
    folder_path = os.path.join(settings.BASE_DIR, 'Books')
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'books.json')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)

    with open(file_path, 'r+') as f:
        books = json.load(f)
        books.append(data)
        f.seek(0)
        json.dump(books, f, ensure_ascii=False, indent=4)

def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            save_book_data(form.cleaned_data)
            return render(request, 'books/success.html')
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})

def book_list(request):
    file_path = os.path.join(settings.BASE_DIR, 'Books', 'books.json')
    books = []

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            books = json.load(f)

    return render(request, 'books/book_list.html', {'books': books})