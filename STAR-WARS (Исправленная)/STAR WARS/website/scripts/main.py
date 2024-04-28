from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MIND YOUR OWN BUSSINES'
    
from .views import views
from .auth import auth
    
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)
    
    
