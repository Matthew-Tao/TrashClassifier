from flask import Flask, request
from lobe import ImageModel

app = Flask('app')

model = ImageModel.load('model')

@app.route('/', methods=["POST"])
def index():
    if request.method == "POST":
        image = request.files['image']
        image.save("temp/123.jpg")
        result = model.predict_from_file('path/to/file.jpg')
        return(result.prediction)

if __name__ == '__main__':
    app.run()