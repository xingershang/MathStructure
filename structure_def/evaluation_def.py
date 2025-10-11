# file: evaluation_structure_def.py
# Description: Defines the Pydantic models for the LLM Judge's evaluation output.

from typing import Literal
from pydantic import BaseModel, Field

class PrincipleEvaluation(BaseModel):
    """
    Represents the evaluation for a single principle.
    """
    issues: str = Field(
        ..., 
        description="A detailed, step-by-step reasoning for the score, listing all found violations."
    )
    score: Literal[1, 2, 3, 4, 5] = Field(
        ..., 
        description="The final holistic score for this principle, from 1 to 5."
    )

class EvaluationSummary(BaseModel):
    """
    Contains the evaluation results for all six core principles.
    """
    # We use 'alias' to allow Python-style snake_case variable names
    # while parsing the exact PascalCase keys from the LLM's JSON output.
    information_equivalency: PrincipleEvaluation = Field(..., alias="InformationEquivalency")
    no_free_variables: PrincipleEvaluation = Field(..., alias="NoFreeVariables")
    concrete_reference: PrincipleEvaluation = Field(..., alias="ConcreteReference")
    accurate_node_type: PrincipleEvaluation = Field(..., alias="AccurateNodeType")
    accurate_scoping: PrincipleEvaluation = Field(..., alias="AccurateScoping")
    logical_clarification: PrincipleEvaluation = Field(..., alias="LogicalClarification")

class EvaluationResult(BaseModel):
    """
    The root model for the entire JSON output from the Judge agent.
    """
    evaluation: EvaluationSummary