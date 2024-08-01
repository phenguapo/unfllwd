from flask import Flask, request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'html'}
app.secret_key = 'supersecretkey'  # Required for flash messages

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_usernames_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        contents = file.read()
    
    soup = BeautifulSoup(contents, 'lxml')
    usernames = [username.text.strip() for username in soup.select('div a')]
    return usernames

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        followers_file = request.files.get('followers_file')
        followings_file = request.files.get('followings_file')
        
        if not (followers_file and followings_file):
            flash("Both files are required", 'danger')
            return redirect(request.url)
        
        if not (allowed_file(followers_file.filename) and allowed_file(followings_file.filename)):
            flash("Only .html files are allowed", 'danger')
            return redirect(request.url)
        
        if followers_file.filename == '' or followings_file.filename == '':
            flash("No selected file", 'danger')
            return redirect(request.url)
        
        # Save files
        followers_filename = secure_filename(followers_file.filename)
        followings_filename = secure_filename(followings_file.filename)
        followers_file_path = os.path.join(app.config['UPLOAD_FOLDER'], followers_filename)
        followings_file_path = os.path.join(app.config['UPLOAD_FOLDER'], followings_filename)
        followers_file.save(followers_file_path)
        followings_file.save(followings_file_path)
        
        # Process files
        followers = get_usernames_from_html(followers_file_path)
        followings = get_usernames_from_html(followings_file_path)
        
        not_following_back = [user for user in followings if user not in followers]

        return render_template('results.html', not_following_back=not_following_back, count=len(not_following_back))

    return render_template('upload.html')

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
