# Pytest Project

***

# Requirements

- [Python 3.11 installed](https://www.python.org/)
- PyTest framework installed (version 7.3.1)

## Setup
This repository contains automated tests implemented using the PyTest framework. The tests aim to validate the functionality and ensure the quality of the software application.


### Clone the repository:

```bash
git clone 
```


### Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
.\venv\Scripts\activate 
```

### Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests
To execute the automated tests, use the following command:

```bash
pytest
```
another way to execute it is by marks

```bash
pytest -m test
```
### Reporting
PyTest generates detailed reports after running tests, including information about passed, failed, and skipped tests. These reports are saved in the reports directory.


