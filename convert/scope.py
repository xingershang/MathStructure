# step 2. scope each sentence

from openai import OpenAI # type: ignore
import os
import re
from utils import extract_thinking_and_result

client = OpenAI(
    api_key="sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH",
    base_url="https://gpt.api.zhangyichi.cn/v1"
)

# model_name = "gemini-2.5-pro"
model_name = "deepseek-chat"

with open("../prompt/prompt_scope.md", "r", encoding="utf-8") as f:
    scope_prompt = f.read().strip()

file_input_content = "../display/node_type_result_whole.md"
file_scope_context_whole = "../display/scope_context_whole.md"
file_scope_result_whole = "../display/scope_result_whole.md"
file_scope_llm_response = "../display/scope_llm_response.md"
file_scope_current = "../display/scope_current.md"

# clear files
with open(file_scope_context_whole, "w", encoding="utf-8") as f:
    f.write("")
    print(f"Cleared {file_scope_context_whole}")
with open(file_scope_result_whole, "w", encoding="utf-8") as f:
    f.write("")
    print(f"Cleared {file_scope_result_whole}")

iteration = 0
max_iterations = 100

while iteration < max_iterations:
    iteration += 1
    print(f"iteration {iteration}:")
    
    with open(file_input_content, "r", encoding="utf-8") as f:
        input_content = f.read().strip()
    with open(file_scope_context_whole, "r", encoding="utf-8") as f:
        scope_context_whole = f.read().strip()
    with open(file_scope_result_whole, "r", encoding="utf-8") as f:
        scope_result_whole = f.read().strip()
    
    messages = [{"role": "system", "content": scope_prompt}]
    messages.append({"role": "user", "content": f"节点序列: \n{input_content}\n"})
    messages.append({"role": "user", "content": f"历史Round: \n{scope_context_whole}\n"})
    messages.append({"role": "user", "content": f"本轮之前的tag标记汇总: \n{scope_result_whole}\n"})
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
        )
        response_content = completion.choices[0].message.content

        with open(file_scope_llm_response, "w", encoding="utf-8") as f:
            f.write(response_content)

        thinking, result = extract_thinking_and_result(response_content)
        
        if thinking or result:
            with open(file_scope_context_whole, "a", encoding="utf-8") as f:
                f.write(f"<thinking>\n{thinking}\n</thinking>\n")
                f.write(f"<result>\n{result}\n</result>\n\n")
            
            with open(file_scope_result_whole, "a", encoding="utf-8") as f:
                f.write(result)
                f.write("\n")
            
            with open(file_scope_current, "w", encoding="utf-8") as f:
                f.write(result)
            
            print(f"Result: {result}\n---")
            
            if result.strip() == 'End.':
                break
        else:
            print("Error: Could not extract thinking and result from response")
            print(f"Response content: {response_content}")
            break
            
    except Exception as e:
        print(f"Error during API call or file processing: {e}")
        import traceback
        traceback.print_exc()
        break

print(f"\n\nProcess completed after {iteration} rounds.")
