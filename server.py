from flask_app import app
import flask_app.controllers.characters


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
