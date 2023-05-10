from app.config import app, db
from app.routes import bp

app.register_blueprint(bp, url_prefix='/tasks')

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)