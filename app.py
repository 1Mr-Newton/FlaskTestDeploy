from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
  return 'Hello world\nMy name is Newton.\nA Ghanaian Computer Science Student.'


