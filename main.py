from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506"

all_books = []

@app.route('/')
def home():
    return render_template("index.html", mylibrary=all_books)


@app.route("/add", methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        if not title:
            flash('Title is required')
        elif not author:
            flash('Author is required')
        elif not rating:
            flash('Rating is required')
        else:
            all_books.append( { "title" : title , "author" : author, "rating" : rating })
            return redirect(url_for("home", my_library=all_books))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

