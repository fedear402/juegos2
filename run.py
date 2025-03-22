from app import create_app

from app import app as application
app = application

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)