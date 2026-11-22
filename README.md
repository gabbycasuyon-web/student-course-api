# Student Course API (Flask)

A standalone, read-only backend for the System Integration and Architecture
laboratory. It returns fictional course data as JSON and does not depend on
Base44, a database, or any paid service.

## Files

- app.py - Flask application and the three API routes
- requirements.txt - Flask, Flask-CORS, Gunicorn
- README.md - this file

## Endpoints

| Method | Path | Success | Description |
| ------ | ---- | ------- | ----------- |
| GET | /api/health | 200 | Confirms the API is running |
| GET | /api/courses | 200 | JSON array of six fictional courses |
| GET | /api/courses/<int:course_id> | 200 | One course by integer ID |
| GET | /api/courses/9999 | 404 | Unknown ID returns a not-found JSON error |

## Run locally

1. Create and activate a virtual environment (optional but recommended).

       python -m venv venv
       source venv/bin/activate      (Windows: venv\Scripts\activate)

2. Install the dependencies.

       pip install -r requirements.txt

3. Start the development server.

       python app.py

4. Open the endpoints in a browser:

       http://127.0.0.1:5000/api/health
       http://127.0.0.1:5000/api/courses
       http://127.0.0.1:5000/api/courses/1
       http://127.0.0.1:5000/api/courses/9999

## Test with curl

    curl -i http://127.0.0.1:5000/api/health
    curl -i http://127.0.0.1:5000/api/courses
    curl -i http://127.0.0.1:5000/api/courses/1
    curl -i http://127.0.0.1:5000/api/courses/9999

The last request must answer with HTTP 404 and a JSON body.

## Deploy to Render

1. Push app.py, requirements.txt, and README.md to the root of a GitHub repository.
2. In Render choose New, then Web Service, and connect that repository.
3. Use these settings:

| Setting | Value |
| ------- | ----- |
| Environment | Python 3 |
| Build command | pip install -r requirements.txt |
| Start command | gunicorn app:app |
| Instance type | Free (if available) |

4. Render sets the PORT environment variable. The application listens on
   0.0.0.0 and reads that port, so no manual port configuration is needed.
5. After the deploy finishes, test:

       https://YOUR-SERVICE.onrender.com/api/health
       https://YOUR-SERVICE.onrender.com/api/courses
       https://YOUR-SERVICE.onrender.com/api/courses/1
       https://YOUR-SERVICE.onrender.com/api/courses/9999

## Limitations

- Data lives in memory only: a restart resets the list, and nothing is stored.
- There is no authentication, no database, and no write operation.
- Free Render services spin down when idle, so the first request can be slow.
- Never add real student records, passwords, or API keys to this repository.
