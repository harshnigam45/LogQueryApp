# LogQueryApp
->Description

The Log Query App is a Flask-based web application designed to facilitate the searching of log files based on multiple criteria. It allows users to filter logs by level, message content, time range, and source file.

->System Design

The application utilizes a simple MVC architecture:

  Model: Handles data operations, fetching, and filtering log data based on user inputs.
  
  View: Presents data to the user and provides an interface to interact with the application.
  
  Controller: Manages communication between the Model and View, processing user requests and application responses.
  
->Features

 Full-text Search: Users can search logs based on text content using regular expressions.
 
 Filter by Date Range: Logs can be filtered between specific start and end dates.
 
 Multiple Filters Combination: Supports combining various filters (level, date, source) to narrow down search results.
 
 Simple User Interface: Provides a web interface accessible through any standard web browser without the need for authentication.

->Known Issues

  The application may experience slowdowns when processing very large log files.
  
  The system does not currently support real-time log updating; it requires a manual refresh to load new log entries.
  
