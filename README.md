SOC Threat Dashboard
====================

A cybersecurity project that analyzes web server log files and detects threats
in real time through a professional web-based dashboard.

Built by Arsalan Anwer as part of my cybersecurity portfolio, inspired by
real SOC analyst workflows and OWASP Top 10 threat categories.


What is a SOC?
--------------
A Security Operations Center (SOC) is a team of security analysts who monitor
systems and detect threats in real time. One of their main tasks is analyzing
log files to find suspicious activity before it causes damage.

This tool automates that process.


What This Tool Detects
----------------------
SQL Injection        - Attempts to manipulate database queries
XSS Attacks         - Cross site scripting attempts in requests
Directory Traversal - Attempts to access restricted system files
Brute Force         - Multiple failed login attempts from same IP
Admin Panel Scan    - Attempts to find hidden admin pages


What the Dashboard Shows
------------------------
- Total log lines analyzed
- Total threats detected
- Number of suspicious IP addresses
- Number of threat categories found
- Bar chart showing threats by category
- Doughnut chart showing threats by severity
- Full threats table with severity badges
- List of all suspicious IP addresses


How to Run This Tool
--------------------
Step 1 - Clone the repository

  git clone https://github.com/YOUR_USERNAME/soc-threat-dashboard
  cd soc-threat-dashboard

Step 2 - Install required libraries

  pip install flask

Step 3 - Run the tool

  python app.py

Step 4 - Open your browser and go to

  http://127.0.0.1:5000

Step 5 - Upload a log file and click Analyze Threats


Project Structure
-----------------
soc-threat-dashboard/
  app.py             Flask web server, handles file upload and routing
  analyzer.py        Threat detection logic, pattern matching engine
  templates/
    index.html       Dashboard UI with charts and threat tables
  static/            For future CSS and JS files
  sample_log.txt     Sample log file for testing
  README.md          Project documentation


How the Analyzer Works
----------------------
The analyzer reads each line of the log file and checks it against known
attack patterns using regular expressions. Here is what it looks for:

SQL Injection patterns:
  union select, or 1=1, drop table, insert into

XSS patterns:
  script tags, javascript:, alert(), document.cookie

Directory Traversal patterns:
  ../, /etc/passwd, /etc/shadow, boot.ini

Brute Force detection:
  If the same IP address gets 3 or more 401 responses it is flagged
  as a brute force attempt

Admin Panel Scan:
  Requests to /admin, /phpmyadmin, /wp-admin, /administrator


Severity Levels
---------------
CRITICAL   SQL Injection attempts
HIGH       XSS attacks, Directory Traversal, Brute Force
MEDIUM     Admin Panel Scanning


Skills Demonstrated
-------------------
- Python programming and Flask web framework
- Log analysis and pattern detection using regex
- Threat detection aligned with OWASP Top 10
- SOC analyst workflows and methodology
- Data visualization with Chart.js
- File upload and processing
- Professional dashboard UI design


Why I Built This
----------------
During my cybersecurity internship I performed penetration testing on OWASP
Juice Shop and Zero Bank. I also conducted digital forensic investigations
and network scanning using Nmap. This project brings those skills together
into a tool that a SOC analyst would actually use day to day.


Disclaimer
----------
This tool is for educational purposes only. Use it only on log files from
systems you own or have permission to analyze.


Author
------
Arsalan Anwer
Cybersecurity Student
GitHub: github.com/Unworthy-Thor