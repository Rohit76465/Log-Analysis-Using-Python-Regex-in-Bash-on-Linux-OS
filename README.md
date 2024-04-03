# Log Analysis with Python Regular Expressions in Bash on Linux-OS

This project automates the analysis of system logs to generate insightful reports using Python, regular expressions, and Bash scripting. It extracts data from log files, creates CSV reports, and facilitates visualization through HTML conversion.

**Features:**

Error Ranking: Lists error messages and their frequencies, sorted from most to least common.
User Usage Statistics: Provides user-wise usage statistics, including INFO and ERROR message counts.

**Usage:**

Run ticky_check.py to generate reports.
Convert reports to HTML using csv_to_html.py.
Access HTML pages via browser with [External IP address]/[html-filename].html. External IP address was provided to me by Qwiklabs on Coursera.

**Requirements:**

Python 3.x
Bash (Linux OS)
Libraries: re, csv, operator
