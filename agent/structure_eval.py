# file: agent/structure_eval.py (REFACTORED)

import os
import json
from typing import Optional
from openai import OpenAI

# Import the Pydantic model and the new Checker
from structure_def.evaluation_def import EvaluationResult
from checker.evaluation_checker import EvaluationChecker

class StructureEvaluator:
    """
    An agent that uses an LLM to evaluate a generated mathematical structure.
    It delegates JSON validation to a dedicated checker.
    """
    def __init__(self, api_key: str, base_url: str, model: str, max_retries: int = 3):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.max_retries = max_retries
        # Instantiate the checker for use by this agent
        self.validator = EvaluationChecker()

    def _load_file_content(self, filepath: str) -> str:
        """Helper function to load content from a file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return ""

    def evaluate_structure(
        self,
        guide_prompt_path: str,
        judge_prompt_path: str,
        natural_language_path: str,
        json_structure_path: str
    ) -> Optional[EvaluationResult]:
        """
        Evaluates a structure by calling the LLM with a combined system and user prompt.

        Args:
            guide_prompt_path (str): Path to the main guide markdown file.
            judge_prompt_path (str): Path to the judge's specific system prompt.
            natural_language_path (str): Path to the informal.md file.
            json_structure_path (str): Path to the result.json file.

        Returns:
            Optional[EvaluationResult]: A Pydantic object of the parsed evaluation, or None if failed.
        """
        
        # --- 1. Assemble the full System Prompt ---
        # Concatenate the main guide with the specific judge instructions.
        guide_prompt = self._load_file_content(guide_prompt_path)
        judge_prompt = self._load_file_content(judge_prompt_path)
        system_prompt = f"{guide_prompt}\n\n---\n\n{judge_prompt}"

        # --- 2. Load the content for the User Prompt ---
        natural_language_text = self._load_file_content(natural_language_path)
        json_structure_text = self._load_file_content(json_structure_path)

        if not natural_language_text or not json_structure_text:
            print("Error: Could not proceed due to missing natural language or structure file.")
            return None

        # --- 3. Assemble the User Prompt ---
        # Based on your prompt, the user message is just the text and the structure.
        # The 'Your Task' section is part of the judge prompt itself.
        user_prompt = (
            "## Your Task\n\n"
            "**Natural language text:**\n"
            "\"\"\"\n"
            f"{natural_language_text}\n"
            "\"\"\"\n\n"
            "**Structure:**\n"
            "```json\n"
            f"{json_structure_text}\n"
            "```\n\n"
            "**Evaluation:**\n"
        )
        
        
        retry_count = 0
        while retry_count < self.max_retries:
            print(f"[Agent: StructureEvaluator] Calling LLM API for evaluation (model: {self.model}, attempt {retry_count + 1}/{self.max_retries})...")
            
            try:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.0,
                    response_format={"type": "json_object"},
                )
                response_text = completion.choices[0].message.content
                print("[Agent: StructureEvaluator] LLM responded.")
                
                # --- MODIFIED BLOCK START ---
                # Delegate the validation task to the checker.
                validated_evaluation = self.validator.validate_evaluation_json(response_text)
                
                if validated_evaluation is not None:
                    return validated_evaluation
                else:
                    # If validation fails, the checker has already printed the error.
                    # We just need to handle the retry logic.
                    print(f"[Agent: StructureEvaluator] Validation failed on attempt {retry_count + 1}.")
                # --- MODIFIED BLOCK END ---

            except Exception as e:
                print(f"[Agent: StructureEvaluator] API call failed: {e}")
            
            retry_count += 1
            if retry_count < self.max_retries:
                print(f"Retrying... ({retry_count}/{self.max_retries})")
        
        print(f"\n--- ERROR: Failed to get a valid evaluation after {self.max_retries} attempts. ---")
        return None

if __name__ == '__main__':
    # This is an example of how you would use the class.
    # You would typically call this from your main orchestrator script.

    # Load API credentials from environment variables for security.
    API_KEY = os.environ.get("OPENAI_API_KEY", "your_default_key_here")
    BASE_URL = os.environ.get("OPENAI_BASE_URL", "your_default_url_here")
    MODEL_NAME = os.environ.get("MODEL_NAME", "your_default_model_here")

    # --- Define file paths ---
    # Note: These paths are relative to the project root where you run the script.
    GUIDE_PROMPT = "prompts/structure_system_prompt.md"
    JUDGE_PROMPT = "prompts/judge_prompt.md"
    INFORMAL_MD = "informal.md" # In the root directory
    RESULT_JSON = "result.json"   # In the root directory

    # --- Create dummy files for testing ---
    print("Creating dummy files for demonstration...")
    # This is the guide for the generator, which the judge also needs to know.
    if not os.path.exists("prompts"): os.makedirs("prompts")
    with open(GUIDE_PROMPT, "w") as f:
        f.write("# Guide: The Structure of Mathematical Natural Language Texts\n...")
    # This is the specific instruction set for the judge.
    with open(JUDGE_PROMPT, "w") as f:
        f.write("## Six Evaluation Standards\n...")
    # The source text to be evaluated.
    with open(INFORMAL_MD, "w") as f:
        f.write("Prove that $A \\subseteq A$.")
    # The generated structure to be evaluated.
    with open(RESULT_JSON, "w") as f:
        f.write('{\n  "structure": [\n    {\n      "type": "Show",\n      "proposition": ["$A \\subseteq A$"]\n    }\n  ]\n}')

    # --- Initialize and run the evaluator ---
    evaluator = StructureEvaluator(api_key=API_KEY, base_url=BASE_URL, model=MODEL_NAME)
    
    evaluation_result = evaluator.evaluate_structure(
        guide_prompt_path=GUIDE_PROMPT,
        judge_prompt_path=JUDGE_PROMPT,
        natural_language_path=INFORMAL_MD,
        json_structure_path=RESULT_JSON
    )

    if evaluation_result:
        print("\n--- Successfully Parsed Evaluation Result ---")
        # .model_dump_json() is the Pydantic v2 equivalent of .json()
        print(evaluation_result.model_dump_json(indent=2))