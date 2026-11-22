"""
Student Course API - standalone Flask backend for Render.
Laboratory Activity 3A / 3B - System Integration and Architecture.

Local run:
    pip install -r requirements.txt
    python app.py

Production run (Render start command):
    gunicorn app:app
"""

import os

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Classroom demonstration only: any origin may call the API.
CORS(app)

# ---------------------------------------------------------------------------
# Fictional sample data. No database, no real student records.
# ---------------------------------------------------------------------------
COURSES = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to web and mobile applications using modern frameworks and responsive design.",
    },
    {
        "id": 2,
        "code": "ITAS 3201",
        "name": "System Integration and Architecture",
        "description": "Patterns for connecting distributed systems, services, and enterprise APIs.",
    },
    {
        "id": 3,
        "code": "ITAS 3210",
        "name": "Database Management Systems",
        "description": "Relational modelling, SQL, normalization, and transaction fundamentals.",
    },
    {
        "id": 4,
        "code": "ITAS 3222",
        "name": "Network Administration",
        "description": "IP addressing, routing, switching, and troubleshooting local networks.",
    },
    {
        "id": 5,
        "code": "ITAS 3231",
        "name": "Cloud Computing Fundamentals",
        "description": "Virtualization, service models, and deploying applications to cloud providers.",
    },
    {
        "id": 6,
        "code": "ITAS 3240",
        "name": "Secure Software Engineering",
        "description": "Authentication, authorization, input validation, and secure deployment practices.",
    },
]


@app.get("/api/health")
def health():
    """Health check: proves the service is up and answering JSON."""
    return jsonify({"status": "success", "message": "Student Course API is running"}), 200


@app.get("/api/courses")
def list_courses():
    """Course list: every fictional course as a JSON array."""
    return jsonify(COURSES), 200


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    """Single course: the matching record, or HTTP 404 when the ID is unknown."""
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Course with ID " + str(course_id) + " was not found",
                }
            ),
            404,
        )
    return jsonify(course), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
