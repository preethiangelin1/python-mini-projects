from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "title": "buy food", "completed": False },
    {"id": 2, "title": "buy shoes", "completed": False },
]

@app.route("/todos")
def get_all_todos():
    return todos


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_todo = {
        "id": len(todos) + 1,   # simple ID generation
        "title": data["title"],
        "completed": False
    }

    todos.append(new_todo)

    return jsonify(new_todo), 201

@app.route("/todos/<id>")
def get_todo_by_id(id):
    print(type(id))
    for todo in todos:
        if todo["id"] == int(id):
            return jsonify(todo)
        
    return jsonify({"error": "Todo not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5050)