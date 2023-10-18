from app import app
from routes.routes_bp import usuario_bp

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5007, host="0.0.0.0")