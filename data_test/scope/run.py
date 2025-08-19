import os
import shutil
import subprocess

def process_files():
    # 基础路径
    input_dir = '../node_type/'
    display_dir = '../../display/'
    api_call_dir = '../../convert/'
    
    S = 19
    T = 40
    for i in range(S, T+1):
        # 格式化文件名，确保两位数的编号
        num = f"{i:03d}"
        
        # 输入文件路径
        input_file = os.path.join(input_dir, f'node_type_{num}.md')
        
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"Warning: Input file {input_file} not found, skipping...")
            continue
        
        # 1. 拷贝到 display/node_type.md
        display_file = os.path.join(display_dir, 'node_type.md')
        shutil.copy2(input_file, display_file)
        print(f"Copied {input_file} to {display_file}")
        
        # 2. 运行 api_call/scope.py
        script_path = os.path.join(api_call_dir, 'scope.py')
        
        # 保存当前工作目录
        original_dir = os.getcwd()
        try:
            # 临时切换到 api_call 目录
            os.chdir(api_call_dir)
            
            # 执行脚本（现在使用相对路径时基准目录正确）
            subprocess.run(['python', 'scope.py'], check=True)
            print("Successfully executed scope.py")
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing scope.py: {e}")
            # 恢复原始目录
            os.chdir(original_dir)
            continue
        finally:
            # 确保总是恢复原始目录
            os.chdir(original_dir)
        
        # 3. 拷贝 pretty_output_node_type.md 到 node_type_xxx.md
        pretty_output = os.path.join(display_dir, 'scope.md')
        output_file = f'scope_{num}.md'
        
        if os.path.exists(pretty_output):
            shutil.copy2(pretty_output, output_file)
            print(f"Copied {pretty_output} to {output_file}")
        else:
            print(f"Warning: {pretty_output} not found, skipping...")

        json_output = os.path.join(display_dir, 'scope.json')
        output_file = f'scope_{num}.json'
        
        if os.path.exists(json_output):
            shutil.copy2(json_output, output_file)
            print(f"Copied {json_output} to {output_file}")
        else:
            print(f"Warning: {json_output} not found, skipping...")

if __name__ == "__main__":
    process_files()
    print("All files processed.")
