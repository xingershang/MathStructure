# file: structure_nodes.py
# Description: Defines the Pydantic models for a structured mathematical text.

from typing import List, Union, Literal, Optional
from pydantic import BaseModel, Field

# Forward references are necessary because the types are not yet fully defined.
# We use strings here, and Pydantic will resolve them later.
AnyNode = Union[
    'ShowNode', 'AssumeNode', 'FixNode', 'FindNode',
    'HaveNode', 'ObtainNode', 'SufficesToProveNode', 'LogicChainNode',
    'CalculationChainNode', 'DefineNode', 'HintNode', 'PlaceHolderNode'
]

class ShowNode(BaseModel):
    type: Literal["Show"] = "Show"
    proposition: List[str] = Field(..., description="A list of propositions to be proven.")
    method: Optional[List[str]] = Field(None, description="A list of methods, theorems, or hints for the proof (e.g., ['induction', 'theorem 3.1']).")
    scope: List['AnyNode'] = Field(..., description="The sequence of steps that constitutes the proof for these propositions.")

class AssumeNode(BaseModel):
    type: Literal["Assume"] = "Assume"
    assumption: List[str] = Field(..., description="A list of statements that are assumed to be true.")
    scope: List['AnyNode'] = Field(..., description="The part of the proof that falls under the scope of these assumptions.")

class FixNode(BaseModel):
    type: Literal["Fix"] = "Fix"
    variable: List[str] = Field(..., description="A list of variables that are being fixed (e.g., ['x', 'y in R']).")
    condition: Optional[List[str]] = Field(None, description="A list of conditions or properties that the fixed variables must satisfy.")
    scope: List['AnyNode'] = Field(..., description="The part of the proof that falls under the scope of these fixed variables.")

class HaveNode(BaseModel):
    type: Literal["Have"] = "Have"
    claim: List[str] = Field(..., description="A list of asserted claims or intermediate results.")
    reason: Optional[List[str]] = Field(None, description="The reasoning, theorem, or calculation that supports the claims.")

class SufficesToProveNode(BaseModel):
    type: Literal["SufficesToProve"] = "SufficesToProve"
    sufficient_proposition: List[str] = Field(..., description="A list of propositions that, if proven, would suffice to prove the main goal.")
    reason: Optional[List[str]] = Field(None, description="The reasoning for why proving these propositions is sufficient.")

class ObtainNode(BaseModel):
    type: Literal["Obtain"] = "Obtain"
    obtained_variable: List[str] = Field(..., description="A list of variables that have been obtained or constructed.")
    condition: List[str] = Field(..., description="The properties or conditions that these variables satisfy.")
    reason: Optional[List[str]] = Field(None, description="The reasoning or theorem used to obtain these variables.")

class FindNode(BaseModel):
    type: Literal["Find"] = "Find"
    target: List[str] = Field(..., description="A list of variables or objects to find.")
    condition: Optional[List[str]] = Field(None, description="The list of conditions the targets must satisfy.")
    scope: List['AnyNode'] = Field(..., description="The process or steps for finding the targets.")

class LogicChainStep(BaseModel):
    operator: str = Field(..., description="The logical operator connecting to the next step (e.g., '<=>', '=>').")
    proposition: List[str] = Field(..., description="The resulting proposition of this step.")
    reason: Optional[List[str]] = Field(None, description="The reasons for this specific logical step.")

class LogicChainNode(BaseModel):
    type: Literal["LogicChain"] = "LogicChain"
    initial_proposition: List[str] = Field(..., description="The starting proposition of the chain.")
    step: List[LogicChainStep] = Field(..., description="The sequence of logical steps.")

class CalculationChainStep(BaseModel):
    operator: str = Field(..., description="The mathematical operator connecting to the next step (e.g., '=', '<=', '>').")
    expression: List[str] = Field(..., description="The resulting expression of this step.")
    reason: Optional[List[str]] = Field(None, description="The reasons for this specific calculation step.")

class CalculationChainNode(BaseModel):
    type: Literal["CalculationChain"] = "CalculationChain"
    initial_expression: List[str] = Field(..., description="The starting expression of the chain.")
    step: List[CalculationChainStep] = Field(..., description="The sequence of calculation steps.")

class DefineNode(BaseModel):
    type: Literal["Define"] = "Define"
    term: str = Field(..., description="The variable, symbol, or concept to be defined.")
    definition: str = Field(..., description="The definition of the term.")

class HintNode(BaseModel):
    type: Literal["Hint"] = "Hint"
    text: str = Field(..., description="A natural-language hint or explanatory comment.")

class PlaceHolderNode(BaseModel):
    type: Literal["PlaceHolder"] = "PlaceHolder"
    text: str = Field(..., description="The corresponding natural-language text that could not be formally structured.")


# --- Root Model ---

class Structure(BaseModel):
    thinking: Optional[str] = Field(None, description="think before outputting the structure")
    structure: List[AnyNode] = Field(..., description="the structure")

# This is crucial for Pydantic to handle the forward references in the Union type.
# We are updating the forward reference to the actual model class.
for model in [
    ShowNode, AssumeNode, FixNode, FindNode, HaveNode, ObtainNode,
    SufficesToProveNode, LogicChainNode, CalculationChainNode, DefineNode,
    HintNode, PlaceHolderNode
]:
    model.update_forward_refs()

