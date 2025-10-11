# file: get_structure_with_revise_iteration.py
# Description: Main orchestrator for the generate-evaluate-revise loop with logging.

import os
import json
from typing import Optional
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# Agent imports
from agent.structure_extractor import StructureExtractor
from agent.structure_eval import StructureEvaluator
from agent.revise import StructureReviser

# Pydantic model imports
from structure_def.node_def import Structure
from structure_def.evaluation_def import EvaluationResult

# Utility imports
from utils.format import create_initial_structure
from checker.no_placeholder_checker import check_no_placeholder
from utils.json_pretty_print import pretty_print_json_structure


# --- Configuration ---
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
if not API_KEY:
    raise ValueError("API key not found.")

MAX_PLACEHOLDER_ITERATIONS = 15
MAX_REVISION_CYCLES = 15

# --- File Paths ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INFORMAL_MD_PATH = os.path.join(CURRENT_DIR, "informal.md")
RESULT_JSON_PATH = os.path.join(CURRENT_DIR, "result.json")
EVALUATION_JSON_PATH = os.path.join(CURRENT_DIR, "evaluation.json")
GUIDE_PROMPT_PATH = os.path.join(CURRENT_DIR, "prompts", "structure_system_prompt.md")
JUDGE_PROMPT_PATH = os.path.join(CURRENT_DIR, "prompts", "judge_prompt.md")
REVISE_PROMPT_PATH = os.path.join(CURRENT_DIR, "prompts", "revise_prompt.md")


def run_initial_extraction(extractor: StructureExtractor, source_text: str) -> Optional[Structure]:
    print("--- STEP 1: Starting Initial Structure Extraction ---")
    current_input_json_str = create_initial_structure(source_text)
    last_successful_structure = None
    for i in range(MAX_PLACEHOLDER_ITERATIONS):
        print(f"\n[Extraction Iteration {i + 1}/{MAX_PLACEHOLDER_ITERATIONS}]")
        structure_result = extractor.extract(current_input_json_str, GUIDE_PROMPT_PATH)
        if not structure_result:
            print(f"ERROR: Structure extraction failed completely in iteration {i + 1}.")
            return last_successful_structure
        last_successful_structure = structure_result
        structure_dict = structure_result.model_dump()
        if check_no_placeholder(structure_dict) == 0:
            print("SUCCESS: No placeholders remain. Initial extraction complete.")
            return structure_result
        current_input_json_str = structure_result.model_dump_json(exclude_none=True, exclude={'thinking'})
        print("INFO: Placeholders found, continuing to next extraction iteration...")
    print(f"WARNING: Reached max extraction iterations ({MAX_PLACEHOLDER_ITERATIONS}). "
          f"Proceeding with placeholders remaining in the structure.")
    return last_successful_structure


def check_if_perfect(evaluation: EvaluationResult) -> bool:
    summary = evaluation.evaluation
    all_scores = [
        summary.information_equivalency.score,
        summary.no_free_variables.score,
        summary.concrete_reference.score,
        summary.accurate_node_type.score,
        summary.accurate_scoping.score,
        summary.logical_clarification.score
    ]
    print(f"Current scores: {all_scores}")
    return all(score == 5 for score in all_scores)


def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"log_{timestamp}.md"
    log_filepath = os.path.join(CURRENT_DIR, "logs", log_filename)
    os.makedirs(os.path.dirname(log_filepath), exist_ok=True)
    
    print(f"Logging run to: {log_filepath}")

    with open(log_filepath, 'w', encoding='utf-8') as log_file:
        extractor = StructureExtractor(api_key=API_KEY, base_url=BASE_URL, model=MODEL_NAME)
        evaluator = StructureEvaluator(api_key=API_KEY, base_url=BASE_URL, model=MODEL_NAME)
        reviser = StructureReviser(api_key=API_KEY, base_url=BASE_URL, model=MODEL_NAME)

        try:
            with open(INFORMAL_MD_PATH, 'r', encoding='utf-8') as f:
                natural_language_text = f.read()
        except FileNotFoundError:
            error_msg = f"FATAL ERROR: Source file not found at '{INFORMAL_MD_PATH}'. Aborting."
            print(error_msg)
            log_file.write(f"# Structure Generation Log\n\n{error_msg}")
            return

        log_file.write(f"# Structure Generation Log\n\n")
        log_file.write(f"- **Run Started:** {timestamp}\n")
        log_file.write(f"- **Source File:** `{os.path.basename(INFORMAL_MD_PATH)}`\n\n")
        log_file.write("---\n\n")

        initial_structure = run_initial_extraction(extractor, natural_language_text)
        
        if not initial_structure:
            error_msg = "FATAL ERROR: Initial structure extraction failed. Aborting."
            print(error_msg)
            log_file.write(f"## Initial Structure Extraction\n\n{error_msg}")
            return

        initial_structure_json = initial_structure.model_dump_json(indent=2, exclude={'thinking'})
        with open(RESULT_JSON_PATH, 'w', encoding='utf-8') as f:
            f.write(initial_structure_json)
        print(f"\nInitial structure saved to '{RESULT_JSON_PATH}'.")

        # --- LOGGING (MODIFIED): Write both pretty and raw JSON for initial structure ---
        log_file.write("## Initial Structure (Before Revisions)\n\n")
        log_file.write("### Pretty-Printed View\n\n")
        log_file.write("```\n")
        pretty_initial_structure = pretty_print_json_structure(initial_structure_json)
        log_file.write(pretty_initial_structure)
        log_file.write("\n```\n\n")
        log_file.write("<details>\n")
        log_file.write("<summary>Click to view Raw JSON</summary>\n\n")
        log_file.write("```json\n")
        log_file.write(initial_structure_json)
        log_file.write("\n```\n")
        log_file.write("</details>\n")

        print("\n--- STEP 2: Starting Evaluation and Revision Loop ---")
        
        for cycle in range(MAX_REVISION_CYCLES):
            log_file.write(f"\n---\n\n## Revision Cycle {cycle + 1}\n\n")
            print(f"\n[Revision Cycle {cycle + 1}/{MAX_REVISION_CYCLES}]")

            print("Evaluating current structure...")
            evaluation_result = evaluator.evaluate_structure(
                guide_prompt_path=GUIDE_PROMPT_PATH,
                judge_prompt_path=JUDGE_PROMPT_PATH,
                natural_language_path=INFORMAL_MD_PATH,
                json_structure_path=RESULT_JSON_PATH
            )

            if not evaluation_result:
                error_msg = "FATAL ERROR: Evaluation failed. Aborting revision loop."
                print(error_msg)
                log_file.write(f"### Evaluation Report\n\n{error_msg}\n")
                break
            
            evaluation_json = evaluation_result.model_dump_json(indent=2)
            with open(EVALUATION_JSON_PATH, 'w', encoding='utf-8') as f:
                f.write(evaluation_json)
            print(f"Evaluation report saved to '{EVALUATION_JSON_PATH}'.")

            log_file.write("### Evaluation Report\n\n")
            log_file.write("```json\n")
            log_file.write(evaluation_json)
            log_file.write("\n```\n\n")

            if check_if_perfect(evaluation_result):
                success_msg = "\nSUCCESS: All principles scored 5/5. Final structure is approved!"
                print(success_msg)
                log_file.write(f"**Result:** Approved. All scores are 5/5. Halting revision loop.\n")
                break
            else:
                print("INFO: Structure needs revision. Calling reviser agent...")
                log_file.write("**Result:** Needs Revision. Proceeding to revise structure.\n")

            current_structure_str = Path(RESULT_JSON_PATH).read_text(encoding='utf-8')
            
            revised_structure = reviser.revise_structure(
                guide_prompt_path=GUIDE_PROMPT_PATH,
                revise_prompt_path=REVISE_PROMPT_PATH,
                natural_language_text=natural_language_text,
                structure_to_revise_json=current_structure_str,
                evaluation_json=evaluation_json
            )

            if not revised_structure:
                error_msg = "FATAL ERROR: Revision failed. Aborting revision loop."
                print(error_msg)
                log_file.write(f"### Revised Structure\n\n{error_msg}\n")
                break
            
            revised_structure_json = revised_structure.model_dump_json(indent=2, exclude={'thinking'})
            with open(RESULT_JSON_PATH, 'w', encoding='utf-8') as f:
                f.write(revised_structure_json)
            print(f"Revised structure has been saved to '{RESULT_JSON_PATH}' for the next cycle.")

            # --- LOGGING (MODIFIED): Write both pretty and raw JSON for revised structure ---
            log_file.write("\n### Revised Structure (Input for next cycle)\n\n")
            log_file.write("#### Pretty-Printed View\n\n")
            log_file.write("```\n")
            pretty_revised_structure = pretty_print_json_structure(revised_structure_json)
            log_file.write(pretty_revised_structure)
            log_file.write("\n```\n\n")
            log_file.write("<details>\n")
            log_file.write("<summary>Click to view Raw JSON</summary>\n\n")
            log_file.write("```json\n")
            log_file.write(revised_structure_json)
            log_file.write("\n```\n")
            log_file.write("</details>\n")

        else:
            warn_msg = f"\nWARNING: Reached maximum revision cycles ({MAX_REVISION_CYCLES}). The structure may still not be perfect."
            print(warn_msg)
            log_file.write(f"\n---\n\n**HALT:** {warn_msg}\n")

        print("\nOrchestration process finished.")
        log_file.write("\n---\n\nOrchestration process finished.\n")

    # --- (The final pretty-print saving block remains the same) ---
    print("\n--- STEP 3: Saving Final Pretty-Print Version ---")
    if os.path.exists(RESULT_JSON_PATH):
        try:
            with open(RESULT_JSON_PATH, 'r', encoding='utf-8') as f:
                final_json_str = f.read()
            
            pretty_result = pretty_print_json_structure(final_json_str)
            result_pretty_path = os.path.join(CURRENT_DIR, "result_pretty.md")
            
            with open(result_pretty_path, 'w', encoding='utf-8') as f:
                f.write(pretty_result)
            
            print(f"SUCCESS: Final pretty-printed structure saved to: {result_pretty_path}")

        except Exception as e:
            print(f"Error saving pretty-printed result: {e}")
    else:
        print(f"WARNING: Final '{RESULT_JSON_PATH}' not found. Cannot generate pretty-print version.")


if __name__ == "__main__":
    main()

