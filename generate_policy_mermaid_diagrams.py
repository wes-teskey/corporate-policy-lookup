# generate_policy_mermaid_diagrams.py

import os
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from utils_find_data_dir import find_data_directory

MAX_FILES = 50 # Limit the number of files to process in case of large data directories

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Get the API key
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if not ANTHROPIC_API_KEY:
    print("Error: ANTHROPIC_API_KEY not found in .env file")
    sys.exit(1)

# Initialize the ChatAnthropic model
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.7,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
)

def generate_mermaid_diagram(policy_content):
    """Generate a Mermaid diagram for a policy using Claude API."""
    messages = [
        (
            "system",
            "You are an expert in creating Mermaid diagrams to visualize corporate policies and procedures. "
            "Your task is to create a Mermaid diagram that effectively represents the key elements and flow of the given policy."
        ),
        (
            "human",
            f"Based on the following policy description, create a Mermaid diagram using the 'graph TD' syntax. "
            f"The diagram should clearly represent the main components, steps, or decision points of the policy. "
            f"Here's the policy description:\n\n{policy_content}\n\n"
            f"Please provide only the Mermaid code, starting with 'graph TD' and nothing else."
        ),
    ]
    
    response = llm.invoke(messages)
    return response.content

def main():
    try:
        data_dir = find_data_directory()
        
        # Get all .txt files in the data directory
        txt_files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
        
        # Limit to 50 files
        txt_files = txt_files[:MAX_FILES]
        
        for i, txt_file in enumerate(txt_files, 1):
            print(f"Generating Mermaid diagram {i}/{len(txt_files)}: {txt_file}")
            
            # Read the policy content
            with open(os.path.join(data_dir, txt_file), 'r') as f:
                policy_content = f.read()
            
            # Generate the Mermaid diagram
            mermaid_code = generate_mermaid_diagram(policy_content)
            
            # Create a file name for the Mermaid diagram
            mermaid_file = txt_file.replace('.txt', '_mermaid.txt')
            mermaid_path = os.path.join(data_dir, mermaid_file)
            
            # Save the Mermaid code to a file
            with open(mermaid_path, 'w') as f:
                f.write(mermaid_code)
            
            print(f"Saved Mermaid diagram to {mermaid_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
