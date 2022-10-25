from flask import Flask, request, render_template, redirect, send_file , url_for, session
import json
from keyword_extraction_and_lexical_simplification_final import full_function_in_one_package, Doc_generator, Business_User_Point_Extraction, ff_Business_User
import os 
import codecs
from werkzeug.utils import secure_filename
app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def Front_Page():
    return render_template('index.html')
@app.route('/Free', methods =["GET" ,"POST"])
def Free_User():
    if request.method == "POST":
       text = request.form.get("textb")
       if request.files:
        global User
        User = 1 
        file = request.files["txt_file"] 
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["File_Uploads"], filename))
            with open ("{}{}".format(app.config['File_Uploads'],filename),encoding='cp437') as f:
                text = f.read()
            User, Free_Output = full_function_in_one_package(1, text)    
            Doc_generator(User, Free_Output, "{}".format(app.config['File_Uploads']))   
            return render_template('Free.html', Sample_Input=text,  Sample_Output=Free_Output)
       try:
        User, Free_Output = full_function_in_one_package(1, text)
        Doc_generator(User, Free_Output, "{}".format(app.config['File_Uploads']))
       except:
        return render_template('Free.html')
       else:
        return render_template('Free.html', Sample_Input=text, Sample_Output=Free_Output), send_file("{}Free_User.txt".format(app.config['File_Uploads'], as_attachment = True))
    elif request.method == 'GET':
        return render_template('Free.html')
@app.route('/Business', methods =["GET", "POST"])
def Business_User():
    global phrases
    global rel_text
    global text
    if request.method == "POST":
       text = request.form.get("textb")
       if request.files:
        global User
        User = 3
        file = request.files["txt_file"] 
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["File_Uploads"], filename))
            with open ("{}{}".format(app.config['File_Uploads'],filename),encoding='cp437') as f:
                text = f.read()
            
            phrases, rel_text = Business_User_Point_Extraction(text)    
            #Doc_generator(User, Premium_Output, "{}".format(app.config['File_Uploads']))   
            
       try:
        
        phrases, rel_text = Business_User_Point_Extraction(text)
        #Doc_generator(User, Premium_Output, "{}".format(app.config['File_Uploads']))
       except:
        return render_template('Business.html')
       else:
        session['my_var'] = phrases
        return render_template('Business.html', Sample_Input=text,  phrases=phrases, Sample_Output = phrases)
    elif request.method == 'GET':
        return render_template('Business.html')
@app.route('/Premium', methods =["GET", "POST"])
def Premium_User():
    if request.method == "POST":
       text = request.form.get("textb")
       if request.files:
        global User
        User = 2
        file = request.files["txt_file"] 
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["File_Uploads"], filename))
            with open ("{}{}".format(app.config['File_Uploads'],filename),encoding='cp437') as f:
                text = f.read()
            User, Premium_Output = full_function_in_one_package(1, text)    
            Doc_generator(User, Premium_Output, "{}".format(app.config['File_Uploads']))   
            return render_template('Premium.html', Sample_Input=text,  Sample_Output=Premium_Output)
       try:
        User, Premium_Output = full_function_in_one_package(2, text)
        Doc_generator(User, Premium_Output, "{}".format(app.config['File_Uploads']))
       except:
        return render_template('Premium.html')
       else:
        return render_template('Premium.html', Sample_Input=text, Sample_Output=Premium_Output), send_file("{}Premium.txt".format(app.config['File_Uploads'], as_attachment = True))
    elif request.method == 'GET':
        return render_template('Premium.html')

@app.route('/Download', methods =["GET", "POST"])
def download_file():
    global User
    print(0)
    if (User == 1):
        print(1)
        path = "{}Free_User.txt".format(app.config["File_Uploads"])
        return send_file(path, as_attachment = True)
    if (User == 2):
        path = "{}Premium_User.txt".format(app.config["File_Uploads"])
        return send_file(path, as_attachment = True)
    if (User == 3):
        path = "{}Business_User.txt".format(app.config["File_Uploads"])
        return send_file(path, as_attachment = True)

@app.route('/Business_Phrases', methods =["GET", "POST"])
def Business_phrases():
    global phrases
    global rel_text
    global User 
    global text
    if request.method == "POST":    
        output = request.form.getlist("mycheckboxes")
        print(output)
        print (phrases)
        indices = [phrases.index(item) for item in output]
        User, Output = ff_Business_User(indices, rel_text)
        Doc_generator(User, Output, "{}".format(app.config['File_Uploads']))
        return render_template('Business.html', Sample_Input=text, Sample_Output=Output)
    return render_template('Business_Phrases.html', yeti = phrases)
app.config["File_Uploads"] = "C:/Users/sharm/Documents/YSO Flask/File_Uploads/"

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
