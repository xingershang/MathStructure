# file: checker/evaluation_checker.py
# Description: Checks if a given text is a valid Judge evaluation JSON.

import json
from typing import Optional
from pydantic import ValidationError

# Import the model for the Judge's output
from structure_def.evaluation_def import EvaluationResult

class EvaluationChecker:
    
    @staticmethod
    def validate_evaluation_json(json_text: str) -> Optional[EvaluationResult]:
        """
        Parses and validates a JSON string against the EvaluationResult Pydantic model.

        Args:
            json_text (str): The JSON string output from the Judge LLM.

        Returns:
            Optional[EvaluationResult]: A Pydantic object if validation is successful, otherwise None.
        """
        try:
            print("[Checker] Parsing and Validating Evaluation JSON with Pydantic...")
            # Use the EvaluationResult model for validation
            parsed_evaluation = EvaluationResult.model_validate_json(json_text)
            print("[Checker] Evaluation JSON Parsing Succeeded")
            return parsed_evaluation
            
        except json.JSONDecodeError as e:
            print(f"\n--- ERROR: Failed to decode JSON. The text was not a valid JSON object. ---")
            print(f"Error: {e}")
            print("Invalid JSON string received:", json_text)
            return None
        except ValidationError as e:
            print(f"\n--- ERROR: Pydantic validation failed. The JSON does not match the evaluation schema. ---")
            print(e)
            return None
        except Exception as e:
            print(f"\n--- An unexpected error occurred: {e} ---")
            return None