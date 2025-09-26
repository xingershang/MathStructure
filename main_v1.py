import os
from utils.format import create_initial_structure
from agent.structure_extractor import StructureExtractor

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    informal_md_path = os.path.join(current_dir, "informal.md")
    
    with open(informal_md_path, 'r', encoding='utf-8') as f:
        natural_language_text = f.read()
    
    try:
        json_text = create_initial_structure(natural_language_text)
        print("INIT:\n")
        print(json_text)
        print("\n" + "="*50 + "\n")
        
        api_key = os.getenv("OPENAI_API_KEY", "sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH")
        base_url = os.getenv("OPENAI_BASE_URL", "https://gpt.api.zhangyichi.cn/v1")
        model = os.getenv("MODEL_NAME", "gemini-2.5-flash")
        
        extractor = StructureExtractor(api_key=api_key, base_url=base_url, model=model)
        
        system_prompt_path = os.path.join(current_dir, "prompts", "structure_system_prompt.md")
        
        print("[main_v1.py] Calling StructureExtractor...")
        structure_result = extractor.extract(json_text, system_prompt_path)
        
        if structure_result:
            structure_result.thinking = None
            final_json = structure_result.model_dump_json(indent=2, exclude_none=True)
            
            print("FINAL RESULT:\n")
            print(final_json)
        else:
            print("Structure extraction failed.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
