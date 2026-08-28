# Job Application Tracker

A Python + MySQL project for tracking job applications, updating application status, searching applications, and viewing basic job-search analytics.

## Features
- Add, view, search, update, and delete applications
- Status tracking: Applied, Interview, Rejected, Selected, On Hold
- Dashboard with application counts
- Interview and selection rates
- MySQL database
- Parameterized SQL queries

## Tech Stack
Python 3, MySQL, mysql-connector-python

## Run
1. Install MySQL and start the MySQL service.
2. Install dependencies: `pip install -r requirements.txt`
3. Open `config.py` and replace `YOUR_MYSQL_PASSWORD`.
4. Run: `python app.py`
5. The database and table are created automatically.

## Project Structure
```text
app.py
config.py
database.py
services.py
schema.sql
sample_data.sql
requirements.txt
README.md
.gitignore
```

## Interview Explanation
"I built a Job Application Tracker using Python and MySQL. Python handles the application logic and user interaction, while MySQL stores application records. The system supports CRUD operations, searching, status updates and dashboard analytics. I used parameterized SQL queries and separated database operations into a service layer for maintainability."

## Future Improvements
- Flask/Django web interface
- Authentication
- Follow-up reminders
- CSV export
- Charts
- REST API

Do not upload passwords, API keys, or other secrets to GitHub.
