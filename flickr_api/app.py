from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home_page():
    return render_template("upload.html")


@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    pass
    # TODO Finish this
    # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    # def allowed_file(filename):
    #     return '.' in filename and \
    #         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    #
    # # check if the post request has the file part
    # if 'files' not in request.files:
    #     return jsonify("error: no file part")
    # files = request.files['files']
    #
    # # If the user does not select a file, the browser submits an
    # # empty file without a filename.
    # for file in files:
    #     if file.filename == '' and len(files) == 1:
    #         return jsonify("error: no file selected")
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('download_file', name=filename))
