# management/packer.py (MODIFIED)

import json
import sys
from pathlib import Path

from . import utils

def pack_data():
    """
    Scans the workspace (with informal.md, info.json), reassembles proofs, 
    and overwrites dataset.json with the new schema.
    """
    print("Starting pack process...")

    workspace_path = Path(utils.WORKSPACE_DIR)
    dataset_path = Path(utils.DATASET_FILE)

    if not workspace_path.is_dir():
        print(f"Error: Workspace directory '{utils.WORKSPACE_DIR}' not found. Nothing to pack.")
        sys.exit(1)

    all_proofs_data = []
    proof_count = 0
    print("Scanning workspace and assembling proofs...")

    for domain_path in workspace_path.iterdir():
        if not domain_path.is_dir():
            continue
        domain_name = domain_path.name

        for proof_path in domain_path.iterdir():
            if not proof_path.is_dir():
                continue
            
            current_id_str = proof_path.name
            
            try:
                # --- MODIFIED BLOCK START ---
                # Define paths to the renamed files
                metadata_file = proof_path / utils.METADATA_JSON_FILE # info.json
                source_file = proof_path / utils.SOURCE_MD_FILE   # informal.md
                structure_file = proof_path / utils.STRUCTURE_JSON_FILE

                if not all([metadata_file.is_file(), source_file.is_file(), structure_file.is_file()]):
                    print(f"Warning: Skipping directory '{proof_path}' due to missing files.")
                    continue

                # Start by loading the metadata from info.json
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    proof_data = json.load(f)
                
                # Read informal.md and add it to the 'informal' key
                with open(source_file, 'r', encoding='utf-8') as f:
                    proof_data["informal"] = f.read()
                # --- MODIFIED BLOCK END ---

                with open(structure_file, 'r', encoding='utf-8') as f:
                    proof_data["structure"] = json.load(f)
                
                # Ensure the id is an integer for correct sorting
                if 'id' in proof_data:
                    proof_data['id'] = int(proof_data['id'])
                
                all_proofs_data.append(proof_data)
                proof_count += 1
                print(f"  -> Assembled '{domain_name}/{current_id_str}'")

            except (json.JSONDecodeError, ValueError) as e:
                print(f"Warning: Skipping '{domain_name}/{current_id_str}' due to invalid JSON or ID. Error: {e}")
            except Exception as e:
                print(f"Error processing proof '{domain_name}/{current_id_str}': {e}")
    
    if not all_proofs_data:
        print("No valid proofs found. Packer finished without changes.")
        return
        
    # --- MODIFIED BLOCK START ---
    # Sort by the numeric 'id' field to ensure 2 comes before 10.
    all_proofs_data.sort(key=lambda p: p.get('id', 0))
    # --- MODIFIED BLOCK END ---
    
    print(f"\nWriting {proof_count} proofs to '{utils.DATASET_FILE}'...")
    with open(dataset_path, 'w', encoding='utf-8') as f:
        json.dump(all_proofs_data, f, indent=4, ensure_ascii=False)

    print("Pack process completed successfully.")

def main():
    pack_data()

if __name__ == "__main__":
    main()