import pytest
import os

xml_path = './allure_results'
report_path = './allure_reports'

args = ['-s', '-v', f'{xml_path}', '--clean-alluredir']

pytest.main(args)

cmd = f'allure generate {xml_path} -o {report_path} --clean'

try:
    os.popen(cmd)
except Exception as e:
    print(e)
