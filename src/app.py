from flask import Flask, jsonify, request
app = Flask(__name__)


todos  = [
        {"label": "Sample Todo 1","done": True},
        {"label": "Sample Todo 2","done": True,}
    ]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= len(todos):
        return 'Tarea no encontrada', 404
    
    del todos[position]
    return jsonify(todos), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)



