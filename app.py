from werkzeug.utils import secure_filename
from model_orm import DataSet
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask,render_template, request, flash, redirect, session,send_file,send_from_directory
import os
from Tasks.textclip import create_video_with_text
app = Flask(__name__)
app.secret_key = 'thisisaverysecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def opendb():
    engine = create_engine("sqlite:///model.sqlite")
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/')
def home():
    return render_template('home.html')

def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"mp4","mp4v"}

@app.route('/uploads', methods=['GET','POST'])
def uploadImage():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            flash('❎ No file uploaded','danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('❎ no file selected','danger')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            print(file.filename)
            db = opendb()
            filename = secure_filename(file.filename)
            path = os.path.join(os.getcwd(),"static/uploads", filename)
            print(path)
            file.save(path)
            upload = DataSet(filename=filename,filepath =f"/static/uploads/{filename}", datatype = os.path.splitext(file.filename)[1])
            db.add(upload)
            db.commit()
            flash('file uploaded and saved','success')
            session['uploaded_file'] = f"/static/uploads/{filename}"
            return redirect('/dashboard')
        else:
            flash('❎ Wrong file selected, only mp4 files allowed','danger')
            return redirect(request.url)
   
    return render_template('upload.html',title='upload file')


@app.route('/dashboard')
def filelisting():
    db = opendb()
    filelist = db.query(DataSet).all()
    db.close()
    return render_template('dashboard.html', filelist=filelist)

@app.route('/edit')
def edit():
    return render_template('edit.html')


@app.route('/path')
def path():
    return render_template('expression')

@app.route('/delete/<int:id>')
def delete(id):
    sess=opendb()
    try:
        sess.query(DataSet).filter(DataSet.id==id).delete()
        sess.commit()
        sess.close()
        return redirect('/dashboard')
        # return render_template('dashboard.html')
    except Exception as e:
        return f" ❎ There was a problem while deleting {e}"

    
@app.route('/edit/add_text_to_video/<int:id>', methods=['POST'])
def add_text_to_video(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        text = request.form['text']
        #
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit_stablize<int:id>', methods=['POST'])
def stablize(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/edittrim/<int:id>', methods=['POST'])
def edittrim(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/videoSpeed/<int:id>', methods=['POST'])
def videoSpeed(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/audio/<int:id>', methods=['POST'])
def audio(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/object/<int:id>', methods=['POST'])
def object(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/compress/<int:id>', methods=['POST'])
def compress(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

@app.route('/edit/background/<int:id>', methods=['POST'])
def background(request, id):
    db  = opendb()
    file = db.query(DataSet).filter(DataSet.id==id).first()
    db.close()
    if request.method == 'POST':
        # Remove the unused variable 'text'
        pass
    path = os.path.join(os.getcwd(),file.filepath)
    # create_video_with_text(video_path=path)
    return path

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)





 

