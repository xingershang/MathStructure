import re

file_input_content = "../display/scope_result_whole.md"
file_fill_braces_result = "../display/fill_braces_result.md"

def process_indented_text(input_content):
    lines = input_content.strip().split('\n')
    
    if lines and lines[-1] == "End.":
        lines = lines[:-1]
    
    parsed_lines = []
    for line in lines:
        match = re.search(r'\[@tag: (\d+)\]$', line)
        if match:
            indent_level = int(match.group(1))
            content = re.sub(r'\[@tag: \d+\]$', '', line).rstrip()
            parsed_lines.append((content, indent_level))
        else:
            parsed_lines.append((line, 0))
    
    if not parsed_lines:
        return ""
    
    result = []
    stack = []
    
    for i, (content, indent_level) in enumerate(parsed_lines):
        # 关闭需要关闭的块
        while stack and stack[-1] >= indent_level:
            # 闭大括号的缩进应该是上一级的缩进
            close_indent = stack[-1] - 1
            result.append("    " * close_indent + "}")
            stack.pop()
        
        # 添加当前行（使用正确的缩进）
        current_indent = stack[-1] if stack else 0
        result.append("    " * current_indent + content)
        
        # 检查是否需要开始新块
        next_indent = parsed_lines[i + 1][1] if i + 1 < len(parsed_lines) else 0
        if next_indent > indent_level:
            # 开大括号的缩进应该是当前行的缩进
            result.append("    " * current_indent + "{")
            stack.append(indent_level)
    
    # 关闭所有剩余的块
    while stack:
        close_indent = stack[-1] - 1
        result.append("    " * close_indent + "}")
        stack.pop()
    
    return "\n".join(result)

with open(file_input_content, "r", encoding="utf-8") as f:
    input_content = f.read()

output_content = process_indented_text(input_content)

with open(file_fill_braces_result, "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"Fill-Braces completed. Result saved to {file_fill_braces_result}")
