# generate_policy_descriptions.py

import os
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from company_policies_list import get_policies_list
from utils_find_data_dir import find_data_directory

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

def generate_policy_description(policy_name):
    """Generate a detailed policy description using Claude API."""
    messages = [
        (
            "system",
            "You are a senior document control specialist tasked with drafting appropriate corporate documents. "
            "You have full authority to create these documents as there are no current existing procedures. "
            "Your task is to draft a detailed and professional corporate policy."
        ),
        (
            "human",
            f"Please draft an appropriate corporate policy for '{policy_name}' in about 500 words. "
            "The policy should be detailed, professional, and suitable for a modern corporation."
        ),
    ]
    
    response = llm.invoke(messages)
    return response.content

def main():
    try:
        data_dir = find_data_directory()
        policies = get_policies_list()

        for i, policy in enumerate(policies, 1):
            print(f"Generating policy {i}/{len(policies)}: {policy}")
            
            # Generate the policy description
            description = generate_policy_description(policy)
            
            # Create a file name (replace spaces with underscores and make lowercase)
            file_name = policy.replace(" ", "_").replace("/", "_").lower() + ".txt"
            file_path = os.path.join(data_dir, file_name)
            
            # Save the description to a file
            with open(file_path, 'w') as f:
                f.write(description)
            
            print(f"Saved policy description to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
