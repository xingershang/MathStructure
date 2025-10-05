# management/unpacker.py (MODIFIED)

import json
import shutil
import sys
from pathlib import Path

from . import utils

def unpack_data():
    """
    Reads the dataset.json file and creates a human-readable workspace 
    with the new file naming convention (informal.md, info.json).
    """
    print("Starting unpack process...")

    workspace_path = Path(utils.WORKSPACE_DIR)
    dataset_path = Path(utils.DATASET_FILE)

    # ... (Safety check and workspace deletion logic remains the same) ...
    if workspace_path.exists():
        prompt = (f"WARNING: The '{utils.WORKSPACE_DIR}' directory already exists.\n"
                  f"         All un-packed changes will be lost!\n"
                  f"         Do you want to proceed with deleting and recreating it?")
        
        if not utils.ask_for_confirmation(prompt):
            print("Unpack process cancelled by user.")
            sys.exit()

        print(f"Deleting existing '{utils.WORKSPACE_DIR}' directory...")
        try:
            shutil.rmtree(workspace_path)
        except OSError as e:
            print(f"Error: Failed to delete directory {workspace_path}. Reason: {e}")
            sys.exit(1)

    if not dataset_path.is_file():
        print(f"Error: Dataset file '{utils.DATASET_FILE}' not found. Nothing to unpack.")
        print("Creating an empty dataset.json for you.")
        with open(dataset_path, 'w', encoding='utf-8') as f:
            json.dump([], f)
        sys.exit()
    
    print(f"Reading '{utils.DATASET_FILE}' and creating workspace...")
    
    try:
        with open(utils.DATASET_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            all_proofs_data = [] if not content else json.loads(content)
        if not isinstance(all_proofs_data, list):
            print(f"Error: '{utils.DATASET_FILE}' is not a valid JSON array.")
            sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Malformed JSON in '{utils.DATASET_FILE}'.")
        sys.exit(1)

    proof_count = 0
    for data in all_proofs_data:
        proof_id = data.get("id")
        domain = data.get("domain")
        informal_text = data.get("informal")
        structure = data.get("structure")

        # --- MODIFIED LINE START ---
        # The check for 'structure' is now `is not None`, which correctly handles empty lists [].
        if not all([proof_id is not None, domain, informal_text, structure is not None]):
        # --- MODIFIED LINE END ---
            print(f"Warning: Skipping an entry due to missing 'id', 'domain', "
                  f"'informal', or 'structure' field.")
            continue
        
        proof_id_str = str(proof_id)
        
        try:
            # ... (the rest of the file writing logic is unchanged) ...
            target_dir = utils.get_proof_path(domain, proof_id_str)
            with open(target_dir / utils.SOURCE_MD_FILE, 'w', encoding='utf-8') as md_file:
                md_file.write(informal_text)
            with open(target_dir / utils.STRUCTURE_JSON_FILE, 'w', encoding='utf-8') as struct_file:
                json.dump(structure, struct_file, indent=4, ensure_ascii=False)
            metadata = {key: value for key, value in data.items() if key not in ["informal", "structure"]}
            with open(target_dir / utils.METADATA_JSON_FILE, 'w', encoding='utf-8') as meta_file:
                json.dump(metadata, meta_file, indent=4, ensure_ascii=False)
            proof_count += 1
            print(f"  -> Unpacked '{domain}/{proof_id_str}'")
        except Exception as e:
            print(f"Error processing proof id '{proof_id}': {e}")

    print(f"\nUnpack process completed successfully. Total proofs unpacked: {proof_count}.")

def main():
    unpack_data()

if __name__ == "__main__":
    main()