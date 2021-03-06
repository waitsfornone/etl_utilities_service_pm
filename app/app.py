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
from api_check import validate_api

app = Flask(__name__)
app.secret_key = 'asdfkjqwg[q89ei4yut;oqeirhg[03w4higr'

rules = UploadSet('rules', extensions='xml')
funcspec = UploadSet('funcspec', extensions='pdf')
app.config['UPLOADED_RULES_DEST'] = 'static/rules'
app.config['UPLOADED_FUNCSPEC_DEST'] = 'static/func_specs'
configure_uploads(app, (rules, funcspec))


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
    api_key = request.form.get('api_key', None)
    if validate_api(api_key):
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


@app.route('/<path:path>', methods=['GET'])
def serve_rules(path):
    filename = path.split('/')[-1]
    return send_from_directory(
        app.config['UPLOADED_RULES_DEST'],
        filename,
        as_attachment=True
    )


@app.route('/func_specs', methods=['GET', 'POST'])
def upload_func_specs():
    if request.method == 'POST' and 'funcspec' in request.files:
        funcspec.save(request.files['funcspec'])
        flash("Functional Specifications saved.")
        return redirect(url_for('show_func_specs'))
    return render_template('func_specs.html')


@app.route('/show_func_specs')
def show_func_specs():
    files = list_files(app.root_path, app.config['UPLOADED_FUNCSPEC_DEST'])
    return render_template(
        'show_func_specs.html',
        files=files
    )


@app.route('/<path:path>', methods=['GET'])
def serve_func_specs(path):
    filename = path.split('/')[-1]
    return send_from_directory(
        app.config['UPLOADED_FUNCSPEC_DEST'],
        filename,
        as_attachment=True
    )
