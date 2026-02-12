import os
from flask import Flask
from blueprints.public import public_bp

app = Flask(__name__)

# Basic config for local development
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key-for-local-use")

debug_mode = os.environ.get('FLASK_ENV') == 'development'

# Register the public blueprint
app.register_blueprint(public_bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=debug_mode)