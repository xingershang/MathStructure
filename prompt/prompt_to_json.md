你需要把输入的内容转化为json格式输出。

## JSON格式的定义

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
            }),
            ("scope", {
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
                },
                "default": []
            })
        ]),
        "required": ["type", "proposition", "scope"],
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
            }),
            ("scope", {
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
                },
                "default": []
            })
        ]),
        "required": ["type", "assumption", "scope"],
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
            }),
            ("scope", {
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
                },
                "default": []
            })
        ]),
        "required": ["type", "var_list", "condition", "scope"],
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
            ("scope", {
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
                },
                "default": []
            })
        ]),
        "required": ["type", "proposition", "scope"],
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
            }),
            ("scope", {
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
                },
                "default": []
            })
        ]),
        "required": ["type", "var_list", "condition", "scope"],
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

## 注意事项

你不允许对原始文本做任何改动，只是按照json格式整理！