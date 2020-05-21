import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from werkzeug.exceptions import HTTPException

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
BLOG_DIR = 'blog'
PROJECT_DIR = 'projects'
HOME_ENTRY_LIMIT = 4

app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)

def get_pages(dir_name, order_by, limit=None, is_reversed=False):
    tmp = [p for p in flatpages if p.path.startswith(dir_name)]
    tmp.sort(key=lambda item:item[order_by], reverse=is_reversed)
    if limit != None:
        tmp = tmp[:limit]
    return tmp

def get_page(dir_name, post_name):
    path = '{}/{}'.format(dir_name, post_name)
    post = flatpages.get_or_404(path)
    return post

@app.errorhandler(Exception)
def error(e):
    code = 500
    errors = {
            404 : "Not Found",
            403 : "Forbidden",
            410 : "Gone",
            500 : "Internal Server Error"
            }
    msg = errors[code]
    error_string = "" 

    if isinstance(e, HTTPException):
        code = e.code
    if code in errors.keys():
        msg = errors[code]

    error_string = '{} {}'.format(str(code), errors[code])
    return render_template('error.html', error=error_string), code


@app.route("/")
def index():
    blog_posts = get_pages(BLOG_DIR, order_by='date', limit=HOME_ENTRY_LIMIT, is_reversed=True)
    project_pages = get_pages(PROJECT_DIR, limit=HOME_ENTRY_LIMIT, order_by='importance')
    return render_template('index.html', posts=blog_posts, projects=project_pages)

@app.route("/blog/")
def blogs():
    posts_title = "Blog Posts"
    blog_posts = get_pages(BLOG_DIR, 'date');
    return render_template('posts.html', posts_title=posts_title, posts=blog_posts)

@app.route('/blog/<name>/')
def blog(name):
    post = get_page(BLOG_DIR, name)
    return render_template('post.html', post=post, with_date=True)

@app.route("/projects/")
def projects():
    posts_title = "Projects"
    project_pages = get_pages(PROJECT_DIR, order_by='importance')
    return render_template('posts.html', posts_title=posts_title, posts=project_pages)

@app.route('/projects/<name>/')
def project(name):
    post = get_page(PROJECT_DIR, name)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=DEBUG)
