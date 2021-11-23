from flask import Flask,request
from werkzeug.utils import secure_filename
from deepface import DeepFace
from os import path

app = Flask(__name__)
BASE_FOLDER = '/home/kunderemp/Downloads/SampelGambar'
UPLOAD_FOLDER = BASE_FOLDER + '/upload'


def verification(img_file_path, dataset_path):
  recognition = DeepFace.find(img_path=img_file_path, db_path = dataset_path)
  if len(recognition) == 0:
  	return '[]'
  retVal = '['
  for index,row in recognition.iterrows():
  	if(index > 0) :
  		retVal += ','
  	retVal += "{ 'identity':'" + row['identity'] + "',"
  	retVal += "'cosine':" + str(row['VGG-Face_cosine']) + "}"
  retVal += ']'
  return retVal

@app.route('/')
def hello_world():
  message = "<p>Hello, World!</p>\n"
  message += "<p>Untuk menggunakan: curl -X POST -F 'image=@/path/to/gambar.jpg' -F 'foldername=Alpacino' http://localhost:5000/verifyPicture </p>\n"
  message += "<p>Pilihan foldername saat ini: Alpacino, Amitabh, AngelinaJolie, GemmaChan </p>\n"
  message += "<p>Hasil akan berupa JSON</p>"
  return message

@app.route('/verifyPicture',methods = ['POST'])
def verifyPicture():
  comparedFolder = request.form['foldername']
  f = request.files['image']
  f.save(UPLOAD_FOLDER + '/' + secure_filename( f.filename))
  comparedFolder = BASE_FOLDER + '/' + secure_filename(comparedFolder)
  if not path.exists(comparedFolder):
  	return "Compared Folder " + comparedFolder + " does not exists."
  res = verification(UPLOAD_FOLDER + '/' + secure_filename( f.filename), comparedFolder)
  return res


if __name__ == '__main__':
  #app.run('0.0.0.0',82,True)
  app.config['UPLOAD_FOLDER']='/home/kunderemp/Downloads/SampelGambar/upload'
  app.config['MAX_CONTENT_PATH']=61865984
  app.run(host='0.0.0.0')
