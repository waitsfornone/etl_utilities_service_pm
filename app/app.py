from flask import (
    Flask,
    render_template,
    url_for,
    request,
    flash,
    redirect,
    send_from_directory
)
from flask_uploads import UploadSet, configure_uploads
from file_funcs import list_files
import os

app = Flask(__name__)
app.secret_key = 'asdfkjqwg[q89ei4yut;oqeirhg[03w4higr'

rules = UploadSet('rules', extensions='xml')
app.config['UPLOADED_RULES_DEST'] = 'static/rules'
configure_uploads(app, rules)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api_key')
def api_key():
    return render_template(
        'api_key.html',
    )


@app.route('/api_checker', methods=['POST'])
def api_checker():
    if len(request.form.get('api_key', None)) == 53:
        return render_template('api_results.html', results="API Key is good!")
    else:
        return render_template(
            'api_results.html',
            results="API Key is bad, please generate a new key."
        )


@app.route('/rules', methods=['GET', 'POST'])
def upload_rules():
    if request.method == 'POST' and 'rules' in request.files:
        rules.save(request.files['rules'])
        flash("Rule template saved.")
        return redirect(url_for('show_rules'))
    return render_template('rules.html')


@app.route('/show_rules')
def show_rules():
    files = list_files(app.root_path, app.config['UPLOADED_RULES_DEST'])
    return render_template(
        'show_rules.html',
        files=files
    )


@app.route('/<path:path>')
def serve_rules(path):
    filename = path.split('/')[-1]
    dirpath = os.path.join(app.root_path, app.config['UPLOADED_RULES_DEST'])
    return send_from_directory(dirpath, filename, as_attachement=True)

# For downloading files, a url per file and use send_from_directory()
# Listing the files and creating the URL will have to be done manually.
# I still need to figure out how to have the links REALLY work. But I think it
# is passing the filepath correctly to send_from_directory()
