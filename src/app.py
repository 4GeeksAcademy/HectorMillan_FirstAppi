from flask import Flask, jsonify, request
app = Flask(__name__)


#  Definicion de ruta para el metodo GET.
#  Route definition for the GET method.
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    
    return json_text


#  Definicion de ruta para el metodo POST.
#  Route definition for the POST method.
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Request Body: ", request_body)
    todos.append(request_body)

    return todos


#  Definicion de ruta para el metodo DELETE.
#  Route definition for the DELETE method.
@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    print("Position to DELETE: ", position)
    del todos[position]

    return "something"


#  Datos de ejemplo para la prueba.
# Example data for testing.
some_data = {"name": "Hector", "lastname":"Millan" }
todos = [
    {"label": "Task 1", "done": False},
    {"label": "Task 2", "done": False}
    ]


if __name__== '__main__':
    app.run(host='0.0.0.0', port =3245, debug=True)