# step 2. rewrite each sentence

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

with open("../prompt/prompt_rewrite.md", "r", encoding="utf-8") as f:
    rewrite_prompt = f.read().strip()

file_input_content = "../display/cut_result.md"
file_rewrite_context_whole = "../display/rewrite_context_whole.md"
file_rewrite_result_whole = "../display/rewrite_result_whole.md"
file_rewrite_llm_response = "../display/rewrite_llm_response.md"
file_rewrite_current = "../display/rewrite_current.md"

# clear files
with open(file_rewrite_context_whole, "w", encoding="utf-8") as f:
    f.write("")
    print(f"Cleared {file_rewrite_context_whole}")
with open(file_rewrite_result_whole, "w", encoding="utf-8") as f:
    f.write("")
    print(f"Cleared {file_rewrite_result_whole}")

iteration = 0
max_iterations = 100

while iteration < max_iterations:
    iteration += 1
    print(f"iteration {iteration}:")
    
    with open(file_input_content, "r", encoding="utf-8") as f:
        input_content = f.read().strip()
    with open(file_rewrite_context_whole, "r", encoding="utf-8") as f:
        rewrite_context_whole = f.read().strip()
    with open(file_rewrite_result_whole, "r", encoding="utf-8") as f:
        rewrite_result_whole = f.read().strip()
    
    messages = [{"role": "system", "content": rewrite_prompt}]
    messages.append({"role": "user", "content": f"自然语言文本: \n{input_content}\n"})
    messages.append({"role": "user", "content": f"历史Round: \n{rewrite_context_whole}\n"})
    messages.append({"role": "user", "content": f"本轮之前所做的修改汇总: \n{rewrite_result_whole}\n"})
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
        )
        response_content = completion.choices[0].message.content

        with open(file_rewrite_llm_response, "w", encoding="utf-8") as f:
            f.write(response_content)

        thinking, result = extract_thinking_and_result(response_content)
        
        if thinking or result:
            with open(file_rewrite_context_whole, "a", encoding="utf-8") as f:
                # f.write(f"\n\nRound {iteration}:\n")
                f.write(f"\n<thinking>\n{thinking}\n</thinking>\n")
                f.write(f"<result>\n{result}\n</result>\n")
            
            with open(file_rewrite_result_whole, "a", encoding="utf-8") as f:
                f.write(result)
                f.write("\n")
            
            with open(file_rewrite_current, "w", encoding="utf-8") as f:
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
