# pytest-playwright-tests

## Project Description

`pytest-playwright-tests` is a project for automated web application testing using Python, `pytest`, and `playwright`. 
The project involves writing tests to verify the functionality of web applications and generating reports using Allure.
GitHub Actions is set up for continuous integration and deployment of test reports.
It also provides for sending notifications with test results after the run is completed in GitHub Actions to the Slack channel. 

## Requirements

- Python 3.11
- `pipenv` for dependency management
- `playwright` for browser automation
- `pytest` for running tests
- `allure-pytest` for generating Allure reports

## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pytest-playwright-tests.git
   cd pytest-playwright-tests
   ```
2. **Install dependencies:**
   ```bash
   python -m pip install --upgrade pip
   pip install pipenv
   pipenv install --system
   playwright install chromium
   ```
   
## Running tests:

1. **Run all tests:**
   ```bash
   pytest
   ```
2. **Run all tests with generating allure report:**
   ```bash
   pytest --alluredir=./reports --clean-alluredir
   ```
3. **Run one particular test file:**
   ```bash
   pytest tests/<test_file_name>
   ```
   <test_file_name> - the name of the test file from the tests directory in the project.

4. **Run one particular test:**
   ```bash
   pytest -k <test_name>
   ```
   <test_file_name> - the name of the test from the tes file.

## Generate allure report:

The report will be generated automatically after the tests are run.
To open the report use next command:
   ```bash
   allure serve reports
   ```

## GitHub Actions:

GitHub Actions is configured to run tests on every push and pull request to the main branch or workflow can be run manually on the Actions tab. The test results are uploaded as artifacts, and the Allure report is deployed to GitHub Pages.
   
