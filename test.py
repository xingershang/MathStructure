from pydantic import BaseModel, Field, ConfigDict
from typing import List, Union
from openai import OpenAI
import json

client = OpenAI(api_key="sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH", base_url="https://gpt.api.zhangyichi.cn/v1")

# 定义Proof结构 - 使用ConfigDict控制字段顺序
class ProofNode(BaseModel):
    model_config = ConfigDict(extra='forbid')

class AssumeNode(ProofNode):
    content: str = Field(..., description="假设的内容")
    scope: 'Proof' = Field(..., description="假设的证明范围")
    type: str = Field("assume", description="节点类型")
    thinking: str = Field(..., description="思考过程")

class ShowNode(ProofNode):
    content: str = Field(..., description="要证明的命题")
    scope: 'Proof' = Field(..., description="证明过程")
    type: str = Field("show", description="节点类型")
    thinking: str = Field(..., description="思考过程")

class HaveNode(ProofNode):
    content: str = Field(..., description="已有的命题或推导")
    type: str = Field("have", description="节点类型")
    thinking: str = Field(..., description="思考过程")

class Proof(BaseModel):
    nodes: List[Union[AssumeNode, ShowNode, HaveNode]]

# 解析前向引用
AssumeNode.model_rebuild()
ShowNode.model_rebuild()

# 构建包含thinking字段的JSON Schema示例
schema_example = {
    "nodes": [
        {
            "thinking": "用户假设P成立，我需要分析这个假设",
            "content": "P成立",
            "scope": {
                "nodes": [
                    {
                        "thinking": "从假设P可以推导出Q",
                        "content": "可以得到Q",
                        "type": "have"
                    }
                ]
            },
            "type": "assume"
        },
        {
            "thinking": "需要证明R，基于前面的假设和推导",
            "content": "R",
            "scope": {
                "nodes": [
                    {
                        "thinking": "结合P和Q可以推导出R",
                        "content": "由P和Q可得R",
                        "type": "have"
                    }
                ]
            },
            "type": "show"
        },
        {
            "thinking": "这是最终的结论",
            "content": "最后我们有S",
            "type": "have"
        }
    ]
}

# 使用API提取Proof结构
completion = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {
            "role": "system", 
            "content": f"""你是一个数学证明解析器。请将用户输入的证明文本解析为结构化的Proof格式。

必须严格按照以下JSON格式返回：

{json.dumps(schema_example, indent=2, ensure_ascii=False)}

重要规则：
assume和show节点必须有"scope"字段
have节点不能有"scope"字段
每个节点都必须有"thinking"字段，用于记录思考过程
不要返回任何其他文本"""
        },
        {
            "role": "user", 
            "content": "假设P成立，那么我们可以得到Q。证明R：由P和Q可得R。最后我们有S。"
        },
    ],
    response_format={"type": "json_object"},
)

try:
    json_response = json.loads(completion.choices[0].message.content)
    print("原始响应:", json.dumps(json_response, indent=2, ensure_ascii=False))
    
    # 转换为Pydantic模型
    proof = Proof(**json_response)
    print("\nProof解析成功！")
    print(json.dumps(proof.model_dump(), indent=2, ensure_ascii=False))
    
except Exception as e:
    print(f"解析错误: {e}")
    print("原始响应:", completion.choices[0].message.content)
