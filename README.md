# Placement DSA Training Automator

## Overview

Welcome to the **Placement DSA Training Automator** repository! This project automates the process of updating your placement DSA (Data Structures and Algorithms) training materials on GitHub. The automation script ensures that your repository is updated daily with the latest problems and content, keeping your training materials current and relevant.

## Features

- **Daily Updates:** Automatically updates the repository with the latest problems and content every day.
- **Automated README Generation:** Generates a well-formatted README file based on JSON data containing the day's problems, advantages, use cases, and suggested readings.
- **Seamless Integration:** Utilizes GitHub Actions to handle updates and commits directly to the repository.

## How It Works

1. **Data Fetching:** The script fetches JSON data from the `data` directory, which includes the day's training content and problems.
2. **README Generation:** The script generates a README file that includes:
   - Introduction to the topics.
   - Advantages and use cases.
   - Detailed problem statements with examples and constraints.
   - Suggested readings and practice problems.
3. **Automation:** A GitHub Actions workflow runs daily to execute the script, ensuring the repository is updated with the latest information.

## Setup Instructions

1. **Add the Script:**

   - Place the `generate_readme.py` script in the root directory of your repository.

2. **Configure GitHub Secrets:**

   - Go to your GitHub repository settings.
   - Navigate to **Settings** > **Secrets and variables** > **Actions**.
   - Add a new secret named `GITHUB_TOKEN` with your GitHub Personal Access Token.

3. **Prepare Data Files:**

   - Ensure your `data` directory contains JSON files formatted according to your needs, with filenames reflecting the current date (e.g., `06-09-2024.json`).

4. **Add a Workflow:**
   - Create a GitHub Actions workflow file in `.github/workflows` to automate the script execution.

## Usage

Once set up, the workflow will automatically generate and update README files daily. You can manually trigger the workflow from the GitHub Actions tab if needed.

## Contributing

Feel free to fork the repository and make contributions. If you have suggestions or issues, please open an issue or submit a pull request.

---

#### **Author: Visagan S**

---

Thank you for using the Placement DSA Training Automator! If you have any questions or need assistance, please reach out.
