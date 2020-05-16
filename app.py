    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return 'Hey, we have Python Flask in a Docker container!'


    if __name == '__main__':
        app.run(debug=True, host='0.0.0.0')
