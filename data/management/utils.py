# management/utils.py (MODIFIED)

import json
from pathlib import Path
from typing import Any, Dict, List

# --- Configuration Constants ---
DATASET_FILE = "dataset.json"
WORKSPACE_DIR = "workspace"

# MODIFIED: Renamed source file constant
SOURCE_MD_FILE = "informal.md" 
STRUCTURE_JSON_FILE = "structure.json"
# MODIFIED: Renamed metadata file constant
METADATA_JSON_FILE = "info.json"


def get_proof_path(domain: str, proof_id_num: str) -> Path:
    """
    Constructs the standard directory path for a given proof.
    e.g., workspace/Set_Theory/1
    """
    path = Path(WORKSPACE_DIR) / domain / proof_id_num
    path.mkdir(parents=True, exist_ok=True)
    return path


def ask_for_confirmation(prompt: str) -> bool:
    """
    Displays a prompt to the user and asks for a yes/no confirmation.
    """
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")