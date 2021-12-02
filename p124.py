from flask import Flask,jsonify, request

app = Flask(__name__)
tasks = [
     {
          'id':1,
          'tittle':u'Buy Stationary',
          'description':u'Pen, NoteBook, Book, Tape, Colors',
          'done':False
     },
     {
          'id':1,
          'tittle':u'Buy Clothes',
          'description':u'Pant, Jeans, Shirts, T-Shirts, Jackets, Coats ',
          'done':False
     }
]

@app.route("/add-data", methods=["POST"])

def add_task():
     if not request.json:
          return jsonify({
               "status":"error",
               "message":"Please provide the data!"
          },400)

contact={
     'id' : tasks[-1]['id'] + 1,
     'Name' : request.json['Name'],
     'Contact' : request.json.get('Contact',""),
     'done' : False
}