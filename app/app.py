from flask import Flask, render_template, url_for, request
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)

rules = UploadSet('rules', extensions='xml')
app.config['UPLOADED_RULES_DEST'] = '../rules'
configure_uploads(app, rules)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api_key')
def api_key():
    return render_template(
        'api_key.html',
    )

@app.route('/api_checker', methods = ['POST'])
def api_checker():
    if len(request.form.get('api_key',None)) == 53:
        return render_template('api_results.html', results="API Key is good!")
    else:
        return render_template('api_results.html', results="API Key is bad, please generate a new key.")

@app.route('/rules', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'rules' in request.files:
        filename = photos.save(request.files['rules'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Rule template saved.")
        return redirect(url_for('show_rules', id=rec.id))
    return render_template('rules.html')

@app.route('/show_rules')
def show_rules():
    return render_template(
        'show_rules.html',
    )
