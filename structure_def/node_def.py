# this file is to define the nodes of the structure using pydantic

from typing import List, Union, Literal, Optional, Dict, Any
from pydantic import BaseModel, Field, ValidationError

AnyNode = Union[
    'ShowNode', 'AssumeNode', 'FixNode', 'FindNode',
    'HaveNode', 'ObtainNode', 'SufficeToProveNode', 'LogicChainNode',
    'CalculationChainNode', 'DefineNode', 'HintNode', 'PlaceHolderNode'
]

# [Show] {P} using {Q} { ...scope... }
class ShowNode(BaseModel):
    type: Literal["show"] = "show"
    content: Union[str, List[str]] = Field(..., description="the statement to show")
    using: Optional[str] = Field(None, description="the hint for the method of showing")
    scope: List[AnyNode] = Field(..., description="the Structure for the statement")

# [Assume] {P} { ...scope... }
class AssumeNode(BaseModel):
    type: Literal["assume"] = "assume"
    content: Union[str, List[str]] = Field(..., description="the statement that has been assumed")
    scope: List[AnyNode] = Field(..., description="the part of Structure in the scope of that assumed statement")

# [Fix] {var_list} such that {P} { ...scope... }
class FixNode(BaseModel):
    type: Literal["fix"] = "fix"
    var_list: List[str] = Field(..., description="the list of variables that have been fixed")
    such_that: Optional[Union[str, List[str]]] = Field(None, description="the condition that the fixed variables must satisfy")
    scope: List[AnyNode] = Field(..., description="the part of Structure in the scope of that fixed list of variables")

# [Find] {P} such that {Q} { ...scope... }
class FindNode(BaseModel):
    type: Literal["find"] = "find"
    content: str = Field(..., description="the list of variables to find")
    such_that: Optional[str] = Field(None, description="the condition that must meet")
    scope: List[AnyNode] = Field(..., description="the finding process")

# [Have] {P} by {Q}
class HaveNode(BaseModel):
    type: Literal["have"] = "have"
    content: Union[str, List[str]] = Field(..., description="claim")
    by: Optional[Union[str, List[str]]] = Field(None, description="the reason for the claim(optional)")

# [Obtain] {var_list} such that {P} by {Q}
class ObtainNode(BaseModel):
    type: Literal["obtain"] = "obtain"
    var_list: List[str] = Field(..., description="the list of variables obtained")
    such_that: Union[str, List[str]] = Field(..., description="the condition that the obtained variables must satisfy")
    by: Optional[Union[str, List[str]]] = Field(None, description="the reason for the claim(optional)")

# [SufficeToProve] {P} by {Q}
class SufficeToProveNode(BaseModel):
    type: Literal["suffice_to_prove"] = "suffice_to_prove"
    content: Union[str, List[str]] = Field(..., description="the statement that suffices to prove")
    by: Optional[Union[str, List[str]]] = Field(None, description="the reason for the claim(optional)")

class LogicChainStep(BaseModel):
    symbol: str = Field(..., description="logic symbol, e.g., <=>")
    content: str = Field(..., description="the statement after this step")
    reason: Optional[str] = Field(None, description="the reason for this step(optional)")

# [LogicChain] {P1} {symbol1} {reason1} {P2} {symbol2} {reason2} {P3} ... {Pn}
class LogicChainNode(BaseModel):
    type: Literal["logic_chain"] = "logic_chain"
    initial_proposition: str = Field(..., description="the given proposition")
    steps: List[LogicChainStep] = Field(..., description="the list of steps")

class CalculationChainStep(BaseModel):
    symbol: str = Field(..., description="calculation symbol, e.g., =")
    expression: str = Field(..., description="the statement after this step")
    reason: Optional[str] = Field(None, description="the reason for this step(optional)")

# [CalculationChain] {E1} {symbol1} {reason1} ... {En}
class CalculationChainNode(BaseModel):
    type: Literal["calculation_chain"] = "calculation_chain"
    initial_expression: str = Field(..., description="the given expression")
    steps: List[CalculationChainStep] = Field(..., description="the list of steps")

# [Define] {A} as {B}
class DefineNode(BaseModel):
    type: Literal["define"] = "define"
    name: str = Field(..., description="the variable/symbol/concept to be defined")
    as_content: str = Field(..., description="the definition of that variable/symbol/concept")

# [Hint] {P}
class HintNode(BaseModel):
    type: Literal["hint"] = "hint"
    content: str = Field(..., description="a natural-language-hint")

class PlaceHolderNode(BaseModel):
    type: Literal["place_holder"] = "place_holder"
    content: str = Field(..., description="the corresponding natural-language text")

class Structure(BaseModel):
    thinking: Optional[str] = Field(None, description="The Chain-of-Thought process")
    structure: List[AnyNode] = Field(..., description="The Structure.")