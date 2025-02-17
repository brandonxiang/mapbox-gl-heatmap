from flask import Flask, request, send_from_directory, url_for
from flask.ext.cors import CORS
app = Flask(__name__, static_url_path='/static/geojson')
CORS(app)



@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)



if __name__ == "__main__":
    app.run(debug=True, port=8888)

