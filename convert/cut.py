# step 1. cut the initial informal math text into sentences

from openai import OpenAI #type:ignore
import os
import re
from utils import extract_output_content

print(f"\n=== Sentence-Cut ===\n")

client = OpenAI(
    api_key="sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH",
    base_url="https://gpt.api.zhangyichi.cn/v1"
)

# model_name = "gemini-2.5-pro"
model_name = "deepseek-chat"

with open("../prompt/prompt_cut_sentences.md", "r", encoding="utf-8") as f:
    cut_prompt = f.read().strip()

file_informal_proof = "../display/informal_proof.md"
file_cut_result = "../display/cut_result.md"

with open(file_cut_result, "w", encoding="utf-8") as f:
    f.write("")
    print(f"Cleared {file_cut_result}")
    
with open(file_informal_proof, "r", encoding="utf-8") as f:
    informal_proof = f.read().strip()
    
    messages = [{"role": "system", "content": cut_prompt}]
    messages.append({"role": "user", "content": f"自然语言文本: \n{informal_proof}\n"})
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
        )
        result = completion.choices[0].message.content
        with open(file_cut_result, "a", encoding="utf-8") as f:
            f.write(result)
            
    except Exception as e:
        print(f"Error during API call or file processing: {e}")
        import traceback
        traceback.print_exc()

print(f"\n=== Sentence-Cut Completed ===\n")
