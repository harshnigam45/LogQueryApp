from flask import Flask, request, render_template_string
import json
import glob
import re
from datetime import datetime

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Quality Log Control</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-4">
    <h1 class="mb-10">Log Search</h1>
    <form method="post" class="mb-4">
      <div class="mb-3">
        <label for="level" class="form-label">Log Level:</label>
        <input type="text" class="form-control" id="level" name="level">
      </div>
      <div class="mb-3">
        <label for="log_string" class="form-label">Log String:</label>
        <input type="text" class="form-control" id="log_string" name="log_string">
      </div>
      <div class="mb-3">
        <label for="start_date" class="form-label">Start Date (YYYY-MM-DDTHH:MM:SSZ):</label>
        <input type="text" class="form-control" id="start_date" name="start_date">
      </div>
      <div class="mb-3">
        <label for="end_date" class="form-label">End Date (YYYY-MM-DDTHH:MM:SSZ):</label>
        <input type="text" class="form-control" id="end_date" name="end_date">
      </div>
      <div class="mb-3">
        <label for="source" class="form-label">Source File:</label>
        <input type="text" class="form-control" id="source" name="source">
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
    {% if results %}
      <h2>Results:</h2>
      <ul class="list-group">
      {% for result in results %}
        <li class="list-group-item">{{ result }}</li>
      {% endfor %}
      </ul>
    {% endif %}
  </div>
</body>
</html>
'''

def query_logs(level=None, log_string=None, start_date=None, end_date=None, source=None):
    files = glob.glob('log*.log')
    results = []

    start_datetime = datetime.fromisoformat(start_date.replace('Z', '+00:00')) if start_date else None
    end_datetime = datetime.fromisoformat(end_date.replace('Z', '+00:00')) if end_date else None

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                log_entry = json.loads(line)
                log_datetime = datetime.fromisoformat(log_entry['timestamp'].replace('Z', '+00:00'))
                
                if ((level is None or log_entry['level'].lower() == level.lower()) and
                    (log_string is None or re.search(log_string, log_entry['log_string'], re.IGNORECASE)) and
                    (start_datetime is None or log_datetime >= start_datetime) and
                    (end_datetime is None or log_datetime <= end_datetime) and
                    (source is None or source in log_entry['metadata']['source'])):
                    results.append(log_entry)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        level = request.form.get('level')
        log_string = request.form.get('log_string')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        source = request.form.get('source')
        results = query_logs(level, log_string, start_date, end_date, source)
    return render_template_string(HTML, results=results)

if __name__ == '__main__':
    app.run(debug=True)
