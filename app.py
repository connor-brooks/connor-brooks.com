import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
BLOG_DIR = 'blog'
PROJECT_DIR = 'projects'
HOMEPAGE_MAX_PAGE = 4

app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_object(__name__)

def get_pages(dirName, orderBy, limit=None, isReversed=False):
    tmp = [p for p in flatpages if p.path.startswith(dirName)]
    if limit != None:
        tmp = tmp[:limit]
    tmp.sort(key=lambda item:item[orderBy], reverse=isReversed)
    return tmp

def get_page(dirName, postName):
    path = '{}/{}'.format(dirName, postName)
    post = flatpages.get_or_404(path)
    return post

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="404 Not Found")

@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', error="403 Forbidden")

@app.errorhandler(410)
def page_not_found(e):
    return render_template('error.html', error="410 Gone")

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error="410 Internal Server Error")

@app.route("/")
def index():
    blog_posts = get_pages(BLOG_DIR, orderBy='date', limit=4, isReversed=True)
    project_pages = get_pages(PROJECT_DIR, limit=4, orderBy='importance')
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
    project_pages = get_pages(PROJECT_DIR, orderBy='importance')
    return render_template('posts.html', posts_title=posts_title, posts=project_pages)

@app.route('/projects/<name>/')
def project(name):
    post = get_page(PROJECT_DIR, name)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=DEBUG)
