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
    
    if node_type == "Show":
        proposition = json_data.get("proposition", [])
        method = json_data.get("method")
        scope = json_data.get("scope", [])
        
        content = _format_content(proposition)
        line = f"{indent}[Show] {{{content}}}"
        if method:
            line += f" using {{{_format_content(method)}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "Assume":
        assumption = json_data.get("assumption", [])
        scope = json_data.get("scope", [])
        
        content = _format_content(assumption)
        result_lines.append(f"{indent}[Assume] {{{content}}}")
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "Fix":
        variable = json_data.get("variable", [])
        condition = json_data.get("condition")
        scope = json_data.get("scope", [])
        
        vars_str = _format_content(variable)
        line = f"{indent}[Fix] {{{vars_str}}}"
        if condition:
            line += f" such that {{{_format_content(condition)}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "Find":
        target = json_data.get("target", [])
        condition = json_data.get("condition")
        scope = json_data.get("scope", [])
        
        content = _format_content(target)
        line = f"{indent}[Find] {{{content}}}"
        if condition:
            line += f" such that {{{_format_content(condition)}}}"
        result_lines.append(line)
        
        if scope:
            result_lines.append(f"{indent}{{")
            result_lines.append(pretty_print_structure(scope, indent_level + 1))
            result_lines.append(f"{indent}}}")
    
    elif node_type == "Have":
        claim = json_data.get("claim", [])
        reason = json_data.get("reason")
        
        content = _format_content(claim)
        line = f"{indent}[Have] {{{content}}}"
        if reason:
            line += f" by {{{_format_content(reason)}}}"
        result_lines.append(line)
    
    elif node_type == "Obtain":
        obtained_variable = json_data.get("obtained_variable", [])
        condition = json_data.get("condition", [])
        reason = json_data.get("reason")
        
        vars_str = _format_content(obtained_variable)
        line = f"{indent}[Obtain] {{{vars_str}}} such that {{{_format_content(condition)}}}"
        if reason:
            line += f" by {{{_format_content(reason)}}}"
        result_lines.append(line)
    
    elif node_type == "SufficesToProve":
        sufficient_proposition = json_data.get("sufficient_proposition", [])
        reason = json_data.get("reason")
        
        content = _format_content(sufficient_proposition)
        line = f"{indent}[SufficesToProve] {{{content}}}"
        if reason:
            line += f" by {{{_format_content(reason)}}}"
        result_lines.append(line)
    
    elif node_type == "LogicChain":
        initial_proposition = json_data.get("initial_proposition", []) 
        steps = json_data.get("steps", [])                    
        
        result_lines.append(f"{indent}[LogicChain] {{{_format_content(initial_proposition)}}}")
        
        for s in steps:
            operator = s.get("operator", "")
            proposition = s.get("proposition", [])
            reason = s.get("reason")             
            
            step_line = f"{indent}    {operator} {{{_format_content(proposition)}}}"
            if reason:
                step_line += f" by {{{_format_content(reason)}}}"
            result_lines.append(step_line)

    elif node_type == "CalculationChain":
        initial_expression = json_data.get("initial_expression", [])
        steps = json_data.get("steps", [])
        
        result_lines.append(f"{indent}[CalculationChain] {{{_format_content(initial_expression)}}}")
        
        for s in steps:
            operator = s.get("operator", "")
            expression = s.get("expression", [])
            reason = s.get("reason")
            
            step_line = f"{indent}    {operator} {{{_format_content(expression)}}}"
            if reason:
                step_line += f" by {{{_format_content(reason)}}}"
            result_lines.append(step_line)

    elif node_type == "Define":
        term = json_data.get("term", "")
        definition = json_data.get("definition", "")
        
        result_lines.append(f"{indent}[Define] {{{term}}} as {{{definition}}}")
    
    elif node_type == "Hint":
        text = json_data.get("text", "")
        result_lines.append(f"{indent}[Hint] {{{text}}}")
    
    elif node_type == "PlaceHolder":
        text = json_data.get("text", "")
        result_lines.append(f"{indent}[PlaceHolder] {{{text}}}")
    
    else:
        result_lines.append(f"{indent}Unhandled Node Type: {json.dumps(json_data, indent=2, ensure_ascii=False)}")
    
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
    
    if "structure" in data:
        result = pretty_print_structure(data["structure"])
        return result
    else:
        return pretty_print_structure(data)