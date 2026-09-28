from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create Database 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studentlist.db"

# Database 
db = SQLAlchemy(app)

# Create a class for each student
class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    gpa = db.Column(db.Float, nullable=False)

    # Create a function to convert into JSON format
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "school" : self.school,
            "gpa": self.gpa
        }

with app.app_context():
    db.create_all()


# Create routes
# Default route
@app.route("/")
def home():
    return jsonify({"Message":"This is a Student List API"})

# Get List of students
@app.route("/students", methods=["GET"])
def get_studentlist():
    students = student.query.all()

    return jsonify([stu.to_dict() for stu in students])


# Get a specific student based on ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    Student = student.query.get(student_id)

    # Checking if it exists
    if Student:
        return jsonify(Student.to_dict())
    else: 
        # Return an error if it does not exist
        return jsonify({"Error":"Student not found"}), 404
    
# POST a new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = student(name = data["name"],
                          school = data["school"],
                          gpa = data["gpa"])
    
    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()), 201

# PUT, update a student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    Student = student.query.get(student_id)
    if Student:
        Student.name = data.get("name", Student.name)
        Student.school = data.get("school", Student.school)
        Student.gpa = data.get("gpa", Student.gpa)

        db.session.commit()

        return jsonify(Student.to_dict())
    
    else:
        return jsonify({"Error":"Student not found"}), 404
    

# DELETE a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    Student = student.query.get(student_id)
    if Student:
        db.session.delete(Student)
        db.session.commit()

        return jsonify({"message":"Student has been successfully removed"})
    
    else:
        return jsonify({"Error":"Student is not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)