from flask import Flask
APP = Flask(__name__)

@app.route('/', methods=['GET'])
def get_health():
    return 'Healthy'

@app.route('/auth', methods['POST'])
def get_jwt(email, password):
    # encryot based off of email, password combination
    return 'Success'

@app.route('/contents', methods['GET'])
def decrypt_jwt(jwt):
    #based off of jwt being a valid JWT



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
