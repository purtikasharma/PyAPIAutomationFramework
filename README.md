# Python Automation Framework

### Intergration Test cases for Restful Booker

URL - https://restful-booker.herokuapp.com/apidoc/index.html
1. Verify GET, POST, PUT, PATCH, DELETE
2. Response Body, Header, Status Code
2. Authentication - Basic Auth, Cookie Based Auth.
3. JSON Schema validation

### Tech Stack (Python Packages Used)

1. Python, Request Module
2. Pytest, Pytest-html
3. Allure Report
4. Faker, CSV, JSON, YAML
5. Run via Commandline - Jenkins

### P.S - DB Connection (in future)
## install packages 
 - ' pip install requests pytest pytest-html faker allure-pytest jsonschema 
 - pip freeze > requirement.txt

### How to locally and See the Report ?
'' pytest test_create_booking.py -s -v --alluredir=./reports --html=report.html''
### How to Run via Jenkins ?