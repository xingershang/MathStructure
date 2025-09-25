# this file is to check whether a given text(string) is a valid json node-structure (defined in node_def.py)

import json
from typing import Optional
from pydantic import ValidationError
from structure_def.node_def import Structure

class JsonStructureChecker:
    
    @staticmethod
    def validate_json(json_text: str) -> Optional[Structure]:
        try:
            print("[Checker] Parsing and Validating JSON with Pydantic...")
            parsed_structure = Structure.model_validate_json(json_text)
            print("[Checker] JSON Parsing Succeeded")
            return parsed_structure
            
        except json.JSONDecodeError as e:
            print(f"\n--- ERROR: Failed to decode JSON. The text was not a valid JSON object. ---")
            print(f"Error: {e}")
            print("Invalid JSON string received:", json_text)
            return None
        except ValidationError as e:
            print(f"\n--- ERROR: Pydantic validation failed. The JSON does not match the schema. ---")
            print(e)
            return None
        except Exception as e:
            print(f"\n--- An unexpected error occurred: {e} ---")
            return None
    
    @staticmethod
    def get_json_schema() -> str:
        schema = Structure.model_json_schema()
        return json.dumps(schema, indent=2, ensure_ascii=False)
