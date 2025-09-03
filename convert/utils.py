import re

# Extract thinking content and result content from "response_text"
def extract_thinking_and_result(response_text):

    thinking_match = re.search(r'<thinking>(.*?)</thinking>', response_text, re.DOTALL)
    thinking = thinking_match.group(1).strip() if thinking_match else ""
    
    result_match = re.search(r'<result>(.*?)</result>', response_text, re.DOTALL)
    result = result_match.group(1).strip() if result_match else ""
    
    return thinking, result

# Extract output_content from "response_text"
def extract_output_content(response_text):
    
    result_match = re.search(r'<output_content>(.*?)</output_content>', response_text, re.DOTALL)
    result = result_match.group(1).strip() if result_match else ""
    
    return result
