# this file is to test JsonStructureChecker in checker/json_structure_checker.py

import os
import sys
from pathlib import Path

current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from checker.json_structure_checker import JsonStructureChecker

def main():
    input_file_path = "input.json"
    
    with open(input_file_path, 'r', encoding='utf-8') as f:
        json_text = f.read()
    
    validator = JsonStructureChecker()
    
    result = validator.validate_json(json_text)
    
    if result:
        print("SUCCEED: JSON validation passed!")
            
    else:
        print("FAIL: JSON validation failed!")

if __name__ == "__main__":
    main()
