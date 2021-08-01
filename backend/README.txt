Setup:
1. Open terminal
2. Navigate to the project directory
3. Activate/Source the python virtual environment using command: source ../venv/bin/activate
4. Run tests using command: python3 -m pytest --html report.html
    6.1 Testing framework 'pytest' is being used
    6.2 pytest-html is being used to generate html results

Disclaimer: The API responses are very inconsistent. Get request sometimes returns correct response and sometimes returns 'pet not found' error. So if a failure is seen then try rerunning the tests.