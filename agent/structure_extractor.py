import os
import json
from typing import Optional
from openai import OpenAI
from structure_def.node_def import Structure
from checker.json_structure_checker import JsonStructureChecker

class StructureExtractor:
    def __init__(self, api_key: str, base_url: str, model: str):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.validator = JsonStructureChecker()

    def load_prompt_template(self, filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def extract(self, user_text: str, system_prompt_path: str) -> Optional[Structure]:
        system_template = self.load_prompt_template(system_prompt_path)
        json_schema = self.validator.get_json_schema()
        system_prompt = system_template.format(fill_in_json_schema=json_schema)
        
        print(f"[Agent: StructurePlanner-structure_extractor] Calling LLM API (model: {self.model})...")
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text},
                ],
                temperature=0.0,
                response_format={"type": "json_object"},
            )
            response_text = completion.choices[0].message.content
            print("[Agent: StructurePlanner-structure_extractor] LLM responded")
            print(f"reponse_text: \n {response_text}\n\n")
            
            return self.validator.validate_json(response_text)

        except Exception as e:
            print(f"\n--- An unexpected error occurred during API call: {e} ---")
            return None
