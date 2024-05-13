import json
import glob
import re

def query_logs(level=None, log_string=None, timestamp=None, source=None):
    """Search for logs matching given criteria."""
    files = glob.glob('log*.log')
    results = []

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                try:
                    log_entry = json.loads(line)
                    if ((level is None or log_entry['level'].lower() == level.lower()) and
                        (log_string is None or re.search(log_string, log_entry['log_string'], re.IGNORECASE)) and
                        (timestamp is None or timestamp in log_entry['timestamp']) and
                        (source is None or source in log_entry['metadata']['source'])):
                        results.append(log_entry)
                except json.JSONDecodeError:
                    continue  
    return results

def main():
    # User inputs for querying logs
    level = input('Enter log level (info, error, success) or leave empty to ignore: ')
    log_string = input('Enter part of the log string or leave empty to ignore: ')
    timestamp = input('Enter timestamp date (YYYY-MM-DD) to filter or leave empty to ignore: ')
    source = input('Enter source file name or leave empty to ignore: ')

    results = query_logs(level=level if level else None, log_string=log_string if log_string else None, timestamp=timestamp if timestamp else None, source=source if source else None)
    
    # Displaying results
    if results:
        for result in results:
            print(json.dumps(result, indent=4))
    else:
        print('No logs found matching the criteria.')

if __name__ == '__main__':
    main()
