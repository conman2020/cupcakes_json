"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from models import db, connect_db, Cupcake
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
connect_db(app)

@app.route('/')
def show_cupcakes():

    return render_template('index.html')


# OLD WAY new way to use dict 
# @app.route('/api/todos/<int:id>')
# def get_todo(id):
#     """Returns JSON for one todo in particular"""
#     onecup = Cupcake.query.get_or_404(id)
#     return jsonify(cupcake=onecup.serialize())
@app.route('/api/todos')
def list_todos():
    """Returns JSON w/ all todos"""
    cupcake = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcake)


# @app.route('/api/todos/<int:id>')
# def get_todo(id):
#     """Returns JSON for one todo in particular"""
#     onecup = Cupcake.query.get_or_404(id)
#     return jsonify(cupcake=onecup.todict())


@app.route('/api/todos', methods=["POST"])
def create_todo():
    """Creates a new todo and returns JSON of that created todo"""
    # new_cup = Cupcake(flavor=request.json["flavor"],size=request.json["size"], rating=request.json["rating"],image_url=request.json["image_url"])
    data = request.json

    new_cup = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image_url=data['image_url'] or None)
    db.session.add(new_cup)
    db.session.commit()
    response_json = jsonify(cupcake=new_cup.to_dict())
    return (response_json, 201)



@app.route('/api/todos/<int:id>', methods=["PATCH"])
def update_todo(id):
    """Updates a particular todo and responds w/ JSON of that updated todo"""
    todo = Cupcake.query.get_or_404(id)
    todo.flavor = request.json.get('flavor', todo.flavor)
    todo.image_url = request.json.get('image_url',  todo.image_url)
    todo.rating = request.json.get('rating', todo.rating)
    todo.size = request.json.get('size',  todo.size)
    db.session.commit()
    return jsonify(todo=todo.todict())


@app.route('/api/todos/<int:id>', methods=["DELETE"])
def delete_todo(id):
    """Deletes a particular todo"""
    todo = Cupcake.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(message="deleted")