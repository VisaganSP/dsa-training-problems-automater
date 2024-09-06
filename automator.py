import os
import json
import base64
import requests
from datetime import datetime

#######################################################################################
#################################### Configuration ####################################
#######################################################################################
REPO_PATH = '.'
REPO_URL = 'https://github.com/VisaganSP/placement-dsa-training.git'
# Fetch token from environment variables
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
DATA_DIRECTORY_PATH = 'data'  # Directory containing JSON files
#######################################################################################
#######################################################################################

# Function to read data from a specific JSON file with specified encoding


def read_json(file_path):
    """
    Reads a JSON file from the specified file path and returns its contents as a Python object.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The contents of the JSON file as a Python object.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to fetch today's data by constructing the filename based on the current date


def fetch_today_data(directory_path):
    """
    Fetches today's data from a JSON file in the specified directory.

    Parameters:
        directory_path (str): The path to the directory containing the JSON files.

    Returns:
        dict or None: The contents of today's JSON file as a Python object, or None if the file does not exist.
    """
    today = datetime.now().strftime("%d-%m-%Y")
    file_path = os.path.join(directory_path, f"{today}.json")
    if os.path.exists(file_path):
        return read_json(file_path)
    else:
        return None

# Function to generate README content based on the data


def generate_readme_content(data):
    def generate_advantages_section(advantages):
        sections = []
        for key, advantage in advantages.items():
            title = advantage['title']
            points = advantage['points']
            formatted_advantage = f"- **_{title}_**:\n"
            formatted_points = "\n".join([f"  - {point}" for point in points])
            sections.append(formatted_advantage + formatted_points)
        return "\n".join(sections)

    def generate_use_cases_section(use_cases):
        sections = []
        for key, case in use_cases.items():
            title = case['title']
            points = case['points']
            formatted_case = f"- **_{title}_**:\n"
            formatted_points = "\n".join([f"  - {point}" for point in points])
            sections.append(formatted_case + formatted_points)
        return "\n".join(sections)

    def generate_problems_section(problems):
        sections = []
        for problem in problems:
            examples = "\n".join([
                f"**_Example {i+1}_**:\n\n```java\nInput: {example['input']}\nOutput: {example['output']}\nExplanation: {example['explanation']}\n```\n"
                for i, example in enumerate(problem['examples'])
            ])
            formatted_problem = (
                f"**_{problem['title']}_**\n\n"
                f"{problem['description']}\n\n"
                f"**_Constraints_**:\n\n" +
                "\n".join([f"- {constraint}" for constraint in problem['constraints']]) +
                f"\n\n**_Examples_**:\n\n{examples}" +
                f"\n**_Solve Here to Get Credits_**: [{problem['title']}]({problem['link']})\n"
            )
            sections.append(formatted_problem)
        return "\n".join(sections)

    def generate_suggested_reading_section(readings):
        return "\n".join([f"- [{reading['title']}]({reading['link']})" for reading in readings])

    def generate_practice_problems(problems):
        practice_problems = []
        for i, problem in enumerate(problems, start=1):
            title = problem['title']
            objective = problem.get('objective', 'Objective not provided.')
            key_concept = problem.get(
                'key_concept', 'Key concept not provided.')
            practice_problems.append(
                f"{i}. **_{title}_**:\n   - **_Objective_**: {objective}\n   - **_Key Concept_**: {key_concept}\n"
            )
        return "\n".join(practice_problems)

    readme_template = f"""
## Introduction to {data['topic1']} and {data['topic2']} 🚀

#### {data['day']} - {data['date']}

#### **📖 Concepts of {data['topic1']} and {data['topic2']}**

### {data['topic1']}
{data['topic1_intro']}

#### 🔍 Real-time Example
{data['topic1_example']}

### {data['topic2']}
{data['topic2_intro']}

#### 🔍 Real-time Example
{data['topic2_example']}

#### **✨ Advantages of {data['topic1']} and {data['topic2']}**

{generate_advantages_section(data['advantages'])}

#### **🌟 Use Cases**

{generate_use_cases_section(data['use_cases'])}

#### **🛠️ Implementing {data['topic1']} and {data['topic2']}**

{generate_problems_section(data['problems'])}

#### **❓ Practice Problems**

{generate_practice_problems(data['problems'])}

#### **📚 Suggested Reading**

{generate_suggested_reading_section(data['suggested_reading'])}

---
"""
    return readme_template


# Function to save README content to a file with utf-8 encoding
def save_readme(content, folder_name, filename):
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"README file generated: {file_path}")

# Function to push README to GitHub using the GitHub API


def create_github_folder_and_upload_readme(folder_name, file_path, commit_message):
    headers = {
        'Authorization': f'token {SECRET_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    repo_name = REPO_URL.split('/')[-1].replace('.git', '')
    api_url = f'https://api.github.com/repos/VisaganSP/{repo_name}/contents/{folder_name}/{os.path.basename(file_path)}'

    # Read the file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if the file already exists on GitHub
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # File exists, get the sha for updating
        file_info = response.json()
        sha = file_info['sha']
        data = {
            'message': commit_message,
            'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
            'sha': sha
        }
        response = requests.put(api_url, headers=headers, json=data)
    elif response.status_code == 404:
        # File does not exist, create it
        data = {
            'message': commit_message,
            'content': base64.b64encode(content.encode('utf-8')).decode('utf-8')
        }
        response = requests.put(api_url, headers=headers, json=data)
    else:
        print(f'Error checking file existence: {response.json()}')
        return

    if response.status_code in [201, 200]:
        print(
            f'Folder and README file created/updated in GitHub repo: {folder_name}/{os.path.basename(file_path)}')
    else:
        print(f'Error: {response.json()}')

# Main function to execute the script


def main():
    today_data = fetch_today_data(DATA_DIRECTORY_PATH)

    if today_data:
        # Generate README content
        readme_content = generate_readme_content(today_data)

        # Define folder name and file name based on the day's data
        day_number = today_data['day'].split()[-1]
        folder_name = f"Day {day_number}"
        filename = f"day_{day_number}.md"
        file_path = os.path.join(REPO_PATH, folder_name, filename)
        commit_message = f"Day {day_number} - {today_data['date']} updated"

        # Save the README content to the file
        save_readme(readme_content, folder_name, filename)

        # Upload the README file to GitHub
        create_github_folder_and_upload_readme(
            folder_name, file_path, commit_message)
    else:
        print("No data found for today.")


if __name__ == "__main__":
    main()
