from flask import Flask, jsonify, request

app = Flask(__name__)

students = {
    "1": {"name": "Alice", "age": 20, "branch": "Computer Science"},
    "2": {"name": "Bob", "age": 21, "branch": "Mechanical Engineering"},
    "3": {"name": "Charlie", "age": 19, "branch": "Computer Science"},
}

@app.route('/update-student/<student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404
    
    data = request.get_json()
    
    if "name" in data:
        students[student_id]["name"] = data["name"]
    if "age" in data:
        students[student_id]["age"] = data["age"]
    if "branch" in data:
        students[student_id]["branch"] = data["branch"]
        
    return jsonify({
        "message": "Student updated successfully", 
        "student": students[student_id]
    }), 200

@app.route('/student-count', methods=['GET'])
def get_student_count():
    return jsonify({
        "total_students": len(students)
    }), 200

@app.route('/students/branch/<branch_name>', methods=['GET'])
def get_students_by_branch(branch_name):
    filtered_students = [
        {"id": sid, **info} for sid, info in students.items() 
        if info["branch"].lower() == branch_name.lower()
    ]
    return jsonify(filtered_students), 200

if __name__ == '__main__':
    app.run(debug=True)