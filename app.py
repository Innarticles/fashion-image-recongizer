#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request, render_template
from flask_bootstrap import Bootstrap



from werkzeug import secure_filename



app = Flask(__name__)
bootstrap = Bootstrap(app)


tasks = {
  "predictions": {
    "bags": 0.990086019039154,
    "clothes": 0.008228730410337448,
    "shoes": 0.0016851801192387938
  }
}


@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template('upload.html', results=tasks)
    else:
      return render_template("upload.html")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)
