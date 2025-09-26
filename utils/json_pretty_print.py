# this file is to define the function pretty_print_structure that with the input of a json string, output a human-readable structure pretty-print

import json
from typing import Any, Dict, List, Union

def pretty_print_structure(json_data: Union[Dict[str, Any], List[Dict[str, Any]], int], indent_level: int = 0) -> str:
    indent = "    " * indent_level
    
    if isinstance(json_data, list):
        result = []
        for item in json_data:
            result.append(pretty_print_structure(item, indent_level))
        return "\n".join(result)
    
    if not isinstance(json_data, dict):
        return f"{indent}{json_data}"
    
    node_type = json_data.get("type", "")
    result_lines = []
    
    if node_type == "show":
        content = _format_content(json_data.get("content", ""))
        using = json_data.get("using")
        scope = json_data.get("scope", [])
        
        line = f"{indent}[Show] {{{content}}}"
        if using:
            line += f" using {{{using}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "assume":
        content = _format_content(json_data.get("content", ""))
        scope = json_data.get("scope", [])
        
        result_lines.append(f"{indent}[Assume] {{{content}}}")
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "fix":
        var_list = json_data.get("var_list", [])
        such_that = _format_content(json_data.get("such_that", ""))
        scope = json_data.get("scope", [])
        
        vars_str = ", ".join(var_list)
        line = f"{indent}[Fix] {{{vars_str}}}"
        if such_that:
            line += f" such that {{{such_that}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "find":
        content = json_data.get("content", "")
        such_that = json_data.get("such_that", "")
        scope = json_data.get("scope", [])
        
        line = f"{indent}[Find] {{{content}}}"
        if such_that:
            line += f" such that {{{such_that}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "have":
        content = _format_content(json_data.get("content", ""))
        by_content = _format_content(json_data.get("by", ""))
        
        line = f"{indent}[Have] {{{content}}}"
        if by_content:
            line += f" by {{{by_content}}}"
        result_lines.append(line)
    
    elif node_type == "obtain":
        var_list = json_data.get("var_list", [])
        such_that = _format_content(json_data.get("such_that", ""))
        by_content = _format_content(json_data.get("by", ""))
        
        vars_str = ", ".join(var_list)
        line = f"{indent}[Obtain] {{{vars_str}}} such that {{{such_that}}}"
        if by_content:
            line += f" by {{{by_content}}}"
        result_lines.append(line)
    
    elif node_type == "suffice_to_prove":
        content = _format_content(json_data.get("content", ""))
        by_content = _format_content(json_data.get("by", ""))
        
        line = f"{indent}[SufficeToProve] {{{content}}}"
        if by_content:
            line += f" by {{{by_content}}}"
        result_lines.append(line)
    
    elif node_type == "logic_chain":
        initial_prop = json_data.get("initial_proposition", "")
        steps = json_data.get("steps", [])
        
        result_lines.append(f"{indent}[LogicChain] {{{initial_prop}}}")
        for step in steps:
            symbol = step.get("symbol", "")
            content = step.get("content", "")
            reason = step.get("reason", "")
            
            step_line = f"{indent}    {symbol} {{{content}}}"
            if reason:
                step_line += f" by {{{reason}}}"
            result_lines.append(step_line)
    
    elif node_type == "calculation_chain":
        initial_expr = json_data.get("initial_expression", "")
        steps = json_data.get("steps", [])
        
        result_lines.append(f"{indent}[CalculationChain] {{{initial_expr}}}")
        for step in steps:
            symbol = step.get("symbol", "")
            expression = step.get("expression", "")
            reason = step.get("reason", "")
            
            step_line = f"{indent}    {symbol} {{{expression}}}"
            if reason:
                step_line += f" by {{{reason}}}"
            result_lines.append(step_line)
    
    elif node_type == "define":
        name = json_data.get("name", "")
        as_content = json_data.get("as_content", "")
        
        result_lines.append(f"{indent}[Define] {{{name}}} as {{{as_content}}}")
    
    elif node_type == "hint":
        content = json_data.get("content", "")
        result_lines.append(f"{indent}[Hint] {{{content}}}")
    
    elif node_type == "place_holder":
        content = json_data.get("content", "")
        result_lines.append(f"{indent}[PlaceHolder] {{{content}}}")
    
    else:
        result_lines.append(f"{indent}{json.dumps(json_data, indent=2, ensure_ascii=False)}")
    
    return "\n".join(result_lines)

def _format_content(content: Any) -> str:
    if isinstance(content, list):
        return "; ".join(str(item) for item in content)
    return str(content)

def pretty_print_json_structure(json_input: str) -> str:
    try:
        data = json.loads(json_input)
    except json.JSONDecodeError:
        return "Invalid json format"
    
    if "thinking" in data and "structure" in data:
        result = ["Chain-of-Thought:"]
        result.append(data["thinking"])
        result.append("\nStructure:")
        result.append(pretty_print_structure(data["structure"]))
        return "\n".join(result)
    else:
        return pretty_print_structure(data)
