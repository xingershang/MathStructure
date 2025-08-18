import os

def create_informal_files():
    # Range of numbers we want (3 to 8 inclusive)
    start_num = 24
    end_num = 32
    
    created_count = 0
    
    for num in range(start_num, end_num + 1):
        # Format the number with leading zeros (003, 004, etc.)
        num_str = f"{num:03d}"
        filename = f"node_type_{num_str}.md"
        
        try:
            # Create empty file
            with open(filename, 'w', encoding='utf-8') as f:
                pass  # Just create an empty file
            
            print(f"Created: {filename}")
            created_count += 1
        except OSError as e:
            print(f"Error creating {filename}: {e}")
    
    print(f"\nTotal files created: {created_count}")

if __name__ == '__main__':
    create_informal_files()
