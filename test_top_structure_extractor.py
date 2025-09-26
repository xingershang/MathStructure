# this file is to test TopStructureExtractor agent

import os
from pathlib import Path
from agent.top_structure_extractor import TopStructureExtractor

current_dir = Path(__file__).parent

# API url & key
BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://gpt.api.zhangyichi.cn/v1")
API_KEY = os.environ.get("OPENAI_API_KEY", "sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH")
MODEL_NAME = os.environ.get("MODEL_NAME", "gemini-2.5-flash")

# Path
SYSTEM_PROMPT_PATH = current_dir / "prompts" / "sys_top_structure_extractor.md"
INPUT_TEXT_PATH = current_dir / "display" / "top_structure_extractor_input.md"

def main():
    agent = TopStructureExtractor(api_key=API_KEY, base_url=BASE_URL, model=MODEL_NAME)

    with open(INPUT_TEXT_PATH, 'r', encoding='utf-8') as f:
        input_text = f.read()

    result_structure = agent.extract(
        user_text=input_text,
        system_prompt_path=str(SYSTEM_PROMPT_PATH)  # 转换为字符串
    )

    if result_structure:
        print("\n--- Final Parsed Structure (JSON) ---")
        print(result_structure.model_dump_json(indent=2, exclude={'thinking'}))

if __name__ == "__main__":
    main()
