from flask import Flask

app = Flask(__name__)

@app.route('/getFlag')
def get_flag():
    return 'CyberXbytes{1234_random_flag_5678}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
