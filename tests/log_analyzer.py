import re


######## Code to refactor ########

def extract_errors_given(log_data: str) -> list:
    lines = log_data.split('\n')
    errors = [line for line in lines if 'ERROR' in line]
    return errors


######## Answer the point 1C ########

######## The code was modified based on the word ERROR and it was also made more robust so that other keywords can be validated ########

def extract_errors(log_data: str, keyword: str = 'ERROR') -> list:
    error_pattern = re.compile(fr'.*{keyword}.*', re.IGNORECASE | re.DOTALL)

    matches = error_pattern.findall(log_data)
    errors = [match.replace('\n', ' ').strip() for match in matches]

    return errors
