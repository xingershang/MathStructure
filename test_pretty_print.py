# test pretty_print

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.json_pretty_print import pretty_print_json_structure

def test_pretty_print():
    
    input_file_path = "input.json"
    
    with open(input_file_path, 'r', encoding='utf-8') as f:
        test_json = f.read()
    
    result = pretty_print_json_structure(test_json)
    print(result)

if __name__ == "__main__":
    test_pretty_print()
