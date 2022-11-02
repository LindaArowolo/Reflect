# import os
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from PIL import Image
#
# UPLOAD_FOLDER = '/static/'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'M4A', 'MP4'}
#
# app = Flask(__name__)
# app.config['/static/'] = UPLOAD_FOLDER
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# def upload_file(file):
#     # if request.method == 'POST':
#     #
#     #     if file_request_name not in request.files:
#     #         flash('No file found')
#     #         return redirect(request.url)
#     #     else:
#     #         file_request_name = request.files[file_request_name]
#     #
#     #     if request.files[file_request_name] == '':
#     #         flash('No selected file')
#     #         return redirect(request.url)
#     if file and allowed_file(file):
#         filename = secure_filename(file)
#         filename.save(os.path.join(app.config['/static/'], filename))
#         return redirect(url_for('download_file', name=filename))
