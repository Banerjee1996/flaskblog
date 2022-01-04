from flask import Blueprint , request , render_template
from flaskblog.models import Post

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home/")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.objects.order_by('-date_posted').paginate(page=page , per_page=2)
    #posts = Post.query.all()
    return render_template('home.html',posts = posts)
    
@main.route("/about")
def about():
    return render_template('about.html',title='About Me')