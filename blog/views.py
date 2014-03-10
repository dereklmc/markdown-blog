from flask import render_template
from blog import app, pages

POST_DIR = "posts"

"""
Routes
"""

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    posts = [p for p in pages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item : item['date'], reverse=True)
    return render_template('blog.html', posts=posts)

@app.route("/archive")
def archive():
    posts = [p for p in pages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item : item['date'], reverse=False)
    return render_template('archive.html', posts=posts)

@app.route("/posts/<name>")
def post(name=None):
    path = '{}/{}'.format(POST_DIR, name)
    post = pages.get_or_404(path)
    return render_template('post.html', post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")