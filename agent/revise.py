# file: agent/revise.py
# Description: Defines the StructureReviser agent, which corrects a flawed structure based on an evaluation.

import os
import json
from typing import Optional

from openai import OpenAI

# Import the model for a valid structure and the checker to validate it.
from structure_def.node_def import Structure
from checker.json_structure_checker import JsonStructureChecker

class StructureReviser:
    """
    An agent that uses an LLM to revise a generated mathematical structure
    based on a critique from a Judge agent.
    """
    def __init__(self, api_key: str, base_url: str, model: str, max_retries: int = 3):
        """
        Initializes the StructureReviser agent.

        Args:
            api_key (str): The API key for the LLM service.
            base_url (str): The base URL for the LLM API endpoint.
            model (str): The name of the model to use.
            max_retries (int): The maximum number of times to retry on failure.
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.max_retries = max_retries
        # This agent's OUTPUT is a revised structure, so it uses the Structure checker.
        self.validator = JsonStructureChecker()

    def _load_file_content(self, filepath: str) -> str:
        """Helper function to load content from a file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return ""

    def revise_structure(
        self,
        guide_prompt_path: str,
        revise_prompt_path: str,
        natural_language_text: str,
        structure_to_revise_json: str,
        evaluation_json: str
    ) -> Optional[Structure]:
        """
        Revises a structure by calling the LLM with the text, the flawed structure, and the evaluation.

        Args:
            guide_prompt_path (str): Path to the main guide markdown file.
            revise_prompt_path (str): Path to the reviser's specific user prompt template.
            natural_language_text (str): The original source math text.
            structure_to_revise_json (str): The flawed JSON structure string to be corrected.
            evaluation_json (str): The JSON string of the Judge's evaluation report.

        Returns:
            Optional[Structure]: A Pydantic object of the newly revised and validated structure, or None if failed.
        """
        
        # --- 1. Assemble the System Prompt ---
        # The system prompt is the main guide that defines the rules.
        system_prompt = self._load_file_content(guide_prompt_path)

        # --- 2. Assemble the User Prompt ---
        # The user prompt contains the specific task instructions and all necessary data.
        user_prompt_template = self._load_file_content(revise_prompt_path)
        
        user_prompt = user_prompt_template.replace("{Natural_Language_Text}", natural_language_text)
        user_prompt = user_prompt.replace("{Json_Structure_to_Revise}", structure_to_revise_json)
        user_prompt = user_prompt.replace("{Evaluation_Structure}", evaluation_json)

        if not all([system_prompt, user_prompt_template, natural_language_text, structure_to_revise_json, evaluation_json]):
            print("Error: Could not proceed due to one or more missing input files or texts.")
            return None

        retry_count = 0
        while retry_count < self.max_retries:
            print(f"[Agent: StructureReviser] Calling LLM API for revision (model: {self.model}, attempt {retry_count + 1}/{self.max_retries})...")
            
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
                print("[Agent: StructureReviser] LLM responded.")
                
                # --- 3. Validate the REVISED Structure ---
                # We use the JsonStructureChecker to ensure the new structure is valid.
                validated_structure = self.validator.validate_json(response_text)
                
                if validated_structure is not None:
                    print(f"[Agent: StructureReviser] Revised JSON validation succeeded on attempt {retry_count + 1}")
                    return validated_structure
                else:
                    print(f"[Agent: StructureReviser] Validation of the revised JSON failed on attempt {retry_count + 1}.")

            except Exception as e:
                print(f"[Agent: StructureReviser] API call failed: {e}")
            
            retry_count += 1
            if retry_count < self.max_retries:
                print(f"Retrying... ({retry_count}/{self.max_retries})")
        
        print(f"\n--- ERROR: Failed to get a valid revised structure after {self.max_retries} attempts. ---")
        return None