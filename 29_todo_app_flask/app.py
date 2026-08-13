from flask import Flask, jsonify, request
from models import get_todo, init_db, insert_todo, get_todos, delete_todo_by_id, update_todo_by_id

app = Flask(__name__)

init_db()

todos = [
    {"id": 1, "title": "buy food", "completed": False },
    {"id": 2, "title": "buy shoes", "completed": False },
]

@app.route("/todos")
def get_all_todos():
    rows = get_todos()

    return jsonify([
        {
            "id": row[0],
            "title": row[1],
            "completed": False if row[2] == 0 else True
        }
        for row in rows
    ])


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    todo_id = insert_todo(data["title"])

    return jsonify({
        "id": todo_id,
        "title": data["title"]
    }), 201

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    deleted = delete_todo_by_id(id)

    if not deleted:
        return {"error": "Todo not found"}, 404

    return {"message": "Todo deleted successfully"}, 200

@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json()

    updated = update_todo_by_id(id, data)

    if updated:
        return jsonify({"message": "Todo updated successfully"}), 200

    return jsonify({"error": "Todo not found or no valid fields provided"}), 404
    
      
@app.route("/todos/<int:id>")
def get_todo_by_id(id):
    todo = get_todo(id)
    print(todo)
    if todo:
        todo_dict = dict(todo)
        todo_dict["completed"] = False if todo_dict["completed"] == 0 else True
        return jsonify(todo_dict)
        
    return jsonify({"error": "Todo not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5050)