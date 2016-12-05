from . import main
from flask import render_template
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from flask_wtf import Form as FlaskForm

class PhotoForm(FlaskForm):
    photo = FileField('Your photo')


allowed_extensions = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])
folder_upload = '/Users/myusername/Documents/Project_Upload/'

#### Methods ####
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions


#### Routes ####


@main.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('uploads/' + filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)