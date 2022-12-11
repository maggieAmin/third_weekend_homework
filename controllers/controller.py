from flask import render_template, request, redirect
from app import app
from models.book_list import book_list
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html', books=enumerate(book_list))

@app.route('/book/<int:id>')
def show(id):
    return render_template('book.html', book=book_list[id])

@app.route('/new_book')
def show_new_book():
    return render_template('new_book.html')

@app.route('/new_book', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    book_list.append(new_book)
    return redirect('/')

@app.route('/book_list/delete/<int:index>')
def delete(index):
    del book_list[index]
    return redirect('/')

# if __name__ == "__main__":
#     app.run(debug=True ,port=8080,use_reloader=False) 
# @app.route('/register', methods=['POST'])
# def register():
#     query = request.form.get('query1')
#     selected = request.form.get('query')
#     if (not query or not selected):
#         return 'failure'
#     processed_text = query.upper()
#     return render_template('index.html')
