# Architecture

```text
User
  |
  v
app.py
  |
  v
services.py
  |
  v
database.py
  |
  v
MySQL: job_tracker.applications
```

`app.py` handles input/output, `services.py` contains application/database operations, and `database.py` manages MySQL connections and initialization.
