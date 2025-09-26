# main.py
import os
from utils.format import create_initial_structure

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    informal_md_path = os.path.join(current_dir, "informal.md")
    
    with open(informal_md_path, 'r', encoding='utf-8') as f:
        natural_language_text = f.read()
    
    try:
        result_json = create_initial_structure(natural_language_text)
        print("inital structure:\n\n")
        print(result_json)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
