from openai import OpenAI
import json
from collections import OrderedDict

def get_proof_structure_schema():
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "ProofStructure": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {"$ref": "#/$defs/Show"},
                        {"$ref": "#/$defs/Assume"},
                        {"$ref": "#/$defs/Have"},
                        {"$ref": "#/$defs/Fix"},
                        {"$ref": "#/$defs/SufficeToProve"},
                        {"$ref": "#/$defs/ToHave"},
                        {"$ref": "#/$defs/OnlyNeeds"},
                        {"$ref": "#/$defs/Find"},
                        {"$ref": "#/$defs/Define"},
                        {"$ref": "#/$defs/Hint"}
                    ]
                }
            }
        },
        "required": ["ProofStructure"],
        "additionalProperties": False,
        "$defs": {
            "Show": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Show"}),
                    ("proposition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "proposition"],
                "additionalProperties": False
            },
            "Assume": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Assume"}),
                    ("assumption", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "assumption"],
                "additionalProperties": False
            },
            "Have": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Have"}),
                    ("proposition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    }),
                    ("reasons", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "proposition", "reasons"],
                "additionalProperties": False
            },
            "Fix": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Fix"}),
                    ("var_list", {"type": "array", "items": {"type": "string"}}),
                    ("condition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "var_list", "condition"],
                "additionalProperties": False
            },
            "SufficeToProve": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "SufficeToProve"}),
                    ("proposition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    }),
                    ("reasons", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "proposition", "reasons"],
                "additionalProperties": False
            },
            "ToHave": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "ToHave"}),
                    ("proposition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    }),
                ]),
                "required": ["type", "proposition"],
                "additionalProperties": False
            },
            "OnlyNeeds": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "OnlyNeeds"}),
                    ("proposition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    }),
                    ("reasons", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "proposition", "reasons"],
                "additionalProperties": False
            },
            "Find": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Find"}),
                    ("var_list", {"type": "array", "items": {"type": "string"}}),
                    ("condition", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "var_list", "condition"],
                "additionalProperties": False
            },
            "Define": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Define"}),
                    ("symbol", {"type": "string"}),
                    ("meaning", {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    })
                ]),
                "required": ["type", "symbol", "meaning"],
                "additionalProperties": False
            },
            "Hint": {
                "type": "object",
                "properties": OrderedDict([
                    ("type", {"type": "string", "const": "Hint"}),
                    ("comment", {"type": "string"})
                ]),
                "required": ["type", "comment"],
                "additionalProperties": False
            }
        }
    }

def format_proof_structure_to_pretty(data, indent_level=0):
    indent = "    " * indent_level
    result = []
    
    if isinstance(data, dict):
        if "ProofStructure" in data:
            return format_proof_structure_to_pretty(data["ProofStructure"], indent_level)
        
        proof_type = data.get("type", "")
        
        def format_list(items):
            if not items:
                return ""
            if len(items) == 1:
                return f"\"{items[0]}\""
            return "{" + "; ".join(f"\"{item}\"" for item in items) + "}"
        
        if proof_type == "Show":
            prop = format_list(data.get("proposition", []))
            result.append(f"{indent}[Show: {prop}]")
                
        elif proof_type == "Assume":
            assumption = format_list(data.get("assumption", []))
            result.append(f"{indent}[Assume: {assumption}]")
                
        elif proof_type == "Have":
            prop = format_list(data.get("proposition", []))
            reasons = data.get("reasons", [])
            reason_str = " by " + format_list(reasons) if reasons else ""
            result.append(f"{indent}[Have: {prop}{reason_str}]")
            
        elif proof_type == "Fix":
            var_list = data.get("var_list", [])
            condition = format_list(data.get("condition", []))
            vars_str = ", ".join(var_list)
            result.append(f"{indent}[Fix: {{{vars_str}}} st {condition}]")
                
        elif proof_type == "SufficeToProve":
            prop = format_list(data.get("proposition", []))
            reasons = data.get("reasons", [])
            reason_str = " by " + format_list(reasons) if reasons else ""
            result.append(f"{indent}[SufficeToProve: {prop} by {reason_str}]")
            
        elif proof_type == "ToHave":
            prop = format_list(data.get("proposition", []))
            result.append(f"{indent}[ToHave: {prop}]")
            
        elif proof_type == "OnlyNeeds":
            prop = format_list(data.get("proposition", []))
            reasons = data.get("reasons", [])
            reason_str = " by " + format_list(reasons) if reasons else ""
            result.append(f"{indent}[OnlyNeeds: {prop} by {reason_str}]")
            
        elif proof_type == "Find":
            var_list = data.get("var_list", [])
            condition = format_list(data.get("condition", []))
            vars_str = ", ".join(var_list)
            result.append(f"{indent}[Find: {{{vars_str}}} st {condition}]")
            
        elif proof_type == "Define":
            symbol = data.get("symbol", "")
            meaning = format_list(data.get("meaning", []))
            result.append(f"{indent}[Define: \"{symbol}\" as \"{meaning}\"]")
            
        elif proof_type == "Hint":
            comment = data.get("comment", "")
            result.append(f"{indent}[Hint: \"{comment}\"]")
            
    elif isinstance(data, list):
        for item in data:
            formatted = format_proof_structure_to_pretty(item, indent_level)
            if formatted:
                result.append(formatted)
    
    return "\n".join(result)


with open("../prompt/prompt_node_type.md", "r", encoding="utf-8") as f:
    prompt = f.read()

with open("../display/informal_proof.md", "r", encoding="utf-8") as f:
    input_text = f.read()

client = OpenAI(
    api_key="sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH",
    base_url="https://gpt.api.zhangyichi.cn/v1"
)

schema = get_proof_structure_schema()

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "proof_structure",
        "schema": schema,
        "strict": True
    }
}

try:
    response = client.chat.completions.create(
        model="o3",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input_text}
        ],
        response_format=response_format,
    )

    msg = response.choices[0].message
    
    if hasattr(msg, "refusal") and msg.refusal:
        output = f"Refusal: {msg.refusal}"
    else:
        output_data = json.loads(msg.content)
        output = json.dumps(output_data, indent=2, ensure_ascii=False)
        
        pretty_output = format_proof_structure_to_pretty(output_data)

    with open("../display/node_type.json", "w", encoding="utf-8") as f:
        f.write(output)
    print("Generated: node_type.json")
        
    with open("../display/node_type.md", "w", encoding="utf-8") as f:
        f.write(pretty_output)
    print("Generated: node_type.md")


except Exception as e:
    print(f"\nError occurred: {str(e)}")
    import traceback
    traceback.print_exc()
