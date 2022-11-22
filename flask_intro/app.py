from flask import Flask

app = Flask(__name__)

from controllers import controller # always do it after the instance above. "app"

if __name__ == '__main__':
    app.run(debug=True)


