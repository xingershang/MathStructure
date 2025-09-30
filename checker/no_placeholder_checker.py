import json
from typing import Dict, Any, List

def check_no_placeholder(structure_data: Dict[str, Any]) -> int:
    def search_placeholder(obj: Any) -> bool:
        if isinstance(obj, dict):
            if obj.get("type") == "PlaceHolder":
                return True
            for value in obj.values():
                if search_placeholder(value):
                    return True
        elif isinstance(obj, list):
            for item in obj:
                if search_placeholder(item):
                    return True
        return False
    
    if isinstance(structure_data, str):
        try:
            structure_data = json.loads(structure_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided")
    
    if search_placeholder(structure_data):
        return 1
    else:
        return 0 