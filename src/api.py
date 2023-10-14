from app import app
from models.entities.user import Usuario

def diz_oi():
    return 'oi'

if __name__ == '__main__':
    app.run(debug=True, port=5007, host="0.0.0.0")