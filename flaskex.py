from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    ''' this is showing the code for entering and storing form data, th first and last data would 
    go on the next page in the string  '''
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 