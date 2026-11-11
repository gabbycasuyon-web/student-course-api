from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

COURSES = [
    {"id": 1, "course_code": "IT101", "course_name": "Introduction to System Integration", "short_description": "Learn the fundamentals of connecting software systems, APIs, and services."},
    {"id": 2, "course_code": "IT102", "course_name": "Database Management Systems", "short_description": "Fundamentals of relational databases, SQL queries, and schema design."},
    {"id": 3, "course_code": "IT103", "course_name": "Mobile Application Development", "short_description": "Build responsive cross-platform mobile user interfaces and apps."},
    {"id": 4, "course_code": "IT104", "course_name": "Web Systems and Technologies", "short_description": "Explore client-server architecture, HTML/CSS/JS, and server-side scripting."},
    {"id": 5, "course_code": "IT105", "course_name": "Cloud Computing Fundamentals", "short_description": "Introduction to cloud infrastructure, web services, and automated deployments."}
]

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API is running successfully"}), 200

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(COURSES), 200

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course is None:
        return jsonify({"error": "Course not found", "status_code": 404}), 404
    return jsonify(course), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
