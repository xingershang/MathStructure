import os
import json
from utils.format import create_initial_structure
from utils.json_pretty_print import pretty_print_json_structure
from agent.structure_extractor import StructureExtractor
from checker.no_placeholder_checker import check_no_placeholder

api_key = os.getenv("OPENAI_API_KEY", "sk-roTlKyXXDUcOI3EsnNuniF41aoCF0czrHzHDfXUdsyT6tmLH")
base_url = os.getenv("OPENAI_BASE_URL", "https://gpt.api.zhangyichi.cn/v1")
model = os.getenv("MODEL_NAME", "gemini-2.5-pro")

MAX_PLACEHOLDER_ITERATIONS = 10

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    informal_md_path = os.path.join(current_dir, "informal.md")
    
    with open(informal_md_path, 'r', encoding='utf-8') as f:
        natural_language_text = f.read()
    
    final_result = None
    
    try:
        json_text = create_initial_structure(natural_language_text)
        print("INIT:\n")
        print(json_text)
        print("\n" + "="*50 + "\n")
        
        

        extractor = StructureExtractor(api_key=api_key, base_url=base_url, model=model, max_retries=5)
        system_prompt_path = os.path.join(current_dir, "prompts", "structure_system_prompt.md")
        
        current_iteration = 0
        current_input = json_text
        
        while current_iteration < MAX_PLACEHOLDER_ITERATIONS:
            current_iteration += 1
            print(f"[main_v1.py] Iteration {current_iteration}: Calling StructureExtractor...")
            
            structure_result = extractor.extract(current_input, system_prompt_path)
            
            if not structure_result:
                print(f"Iteration {current_iteration}: Structure extraction failed completely.")
                break
                
            structure_dict = structure_result.model_dump()
            has_placeholder = check_no_placeholder(structure_dict)
            
            next_input = structure_result.model_dump_json(exclude_none=True, exclude={'thinking'})
            
            print(f"Iteration {current_iteration}: PlaceHolder check result = {has_placeholder}")
            
            if has_placeholder == 0:
                print("SUCCESS: No place_holder nodes found after iteration", current_iteration)
                final_json = structure_result.model_dump_json(indent=2, exclude_none=True, exclude={'thinking'})
                final_result = structure_result
                print("FINAL RESULT:\n")
                print(final_json)
                break
            else:
                print(f"WARNING: Structure still contains place_holder nodes, continuing to iteration {current_iteration + 1}")
                current_input = next_input
                final_result = structure_result
                
                if current_iteration == MAX_PLACEHOLDER_ITERATIONS:
                    print(f"WARNING: Reached maximum iterations but still has placeholders. Saving current result.")
                    final_json = structure_result.model_dump_json(indent=2, exclude_none=True, exclude={'thinking'})
                    print("FINAL RESULT (with placeholders):\n")
                    print(final_json)
        
        else:
            print("Loop completed normally")
        
        if final_result:
            result_path = os.path.join(current_dir, "result.json")
            try:
                result_dict = final_result.model_dump(exclude={'thinking'})
                
                with open(result_path, 'w', encoding='utf-8') as f:
                    json.dump(result_dict, f, indent=2, ensure_ascii=False)
                
                # print(f"\nFinal result has been saved to: {result_path}")

                result_json_str = final_result.model_dump_json(indent=2, exclude_none=True, exclude={'thinking'})
                pretty_result = pretty_print_json_structure(result_json_str)
                result_pretty_path = os.path.join(current_dir, "result_pretty.md")
                with open(result_pretty_path, 'w', encoding='utf-8') as f:
                    f.write(pretty_result)
                
                print(f"Formatted JSON version saved to: {result_pretty_path}")
                
            except Exception as e:
                print(f"Error saving result to file: {e}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
