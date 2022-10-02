
from concurrent.futures import process
from apps.home import blueprint
from flask import render_template, request, send_file, redirect, url_for, flash
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
import os
from apps.home.summarize_txt import generateTxt
from apps.home.pdfEx import process_pdf
import json


# UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/')
def route_default():
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/index', methods=['GET', 'POST'])
def index():
    sumtxt = 'Your summary will appear here'
    keyword = ['keywords','will','be','listed','here']

    if request.method == 'POST':
        # check if request if from local file
        name = ""
        if "localFile" in request.form:
            name = request.form['localFile']
        if name != "":
            sumtxt, keyword = generateTxt(name)
            return render_template('home/index.html', segment='index', sumtxt = sumtxt, keyword = keyword, keylen = len(keyword))
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('apps/static/assets/pdfs', filename))
            sumtxt, keyword = generateTxt(filename)
            # sumtxt = "Hello from the other side"
            # keyword = ['1','2','3']
            return render_template('home/index.html', segment='index', sumtxt = sumtxt, keyword = keyword, keylen = len(keyword))
            # process_pdf(filename)

            # return redirect(url_for('upload_file', name=filename))
    
    return render_template('home/index.html', segment='index', sumtxt = sumtxt, keyword = keyword, keylen = len(keyword))

@blueprint.route('/<template>')
# @login_required
def route_template(template):
    print(template)


    try:

        if not template.endswith('.html'):
            if template.endswith('.pdf'):
                print("id detected")
                text = process_pdf(template)
                return render_template("home/page-blank.html", content = text)
        else:
            pass

        # Detect the current page
        segment = get_segment(request)
        
        # Serve the file (if exists) from app/templates/home/FILE.html
        if template =="ui-tables.html":
            # names = ['pop']
            names = os.listdir('apps/static/assets/pdfs')
            # return render_template("home/" + template, segment=segment)
            return render_template("home/" + template, segment=segment, names = names, nlen = len(names))
        else:
            return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500



# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
