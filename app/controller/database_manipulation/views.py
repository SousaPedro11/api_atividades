from app import app


@app.route('/db/')
def init():
    return "database_manipulation!"
