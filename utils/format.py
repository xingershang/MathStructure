import os
import sys
from typing import List, Union

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

from structure_def.node_def import Structure, PlaceHolderNode

def create_initial_structure(natural_language_text: str) -> str:
    placeholder_node = PlaceHolderNode(
        type="place_holder",
        content=natural_language_text
    )
    
    structure = Structure(
        thinking=None,
        structure=[placeholder_node] 
    )
    
    return structure.model_dump_json(indent=2, exclude_none=True)

if __name__ == "__main__":
    test_text = "this is a test. this is a test. this is a test."
    result = create_initial_structure(test_text)
    print(result)
