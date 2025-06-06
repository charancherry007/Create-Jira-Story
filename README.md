# Create-Jira-Story
Automate creating jira issues using excel as data input and Jira APi's

# 🛠️Jira Issue Automation with Python

This Python project automates the creation of Jira issues using the Jira REST API. It reads configuration details from a JSON file and issue data from an Excel spreadsheet, then creates issues in Jira and updates the Excel file with the generated issue IDs

# 📌 Features

Connects to Jira using API credentials

Reads issue data from an Excel file

Automatically creates issues in Jira

Writes the created issue IDs back to the Excel file

# 🐍 Tech Stack
Language: Python

Libraries:

- **pandas** – for reading and writing Excel files

- **jira** – for interacting with the Jira API

# 📁 Project Structure
.

├── app.py

├── storiesData.xlsx

├── jiraConfig.json

└── README.md

# 🚀 How to Run
Install dependencies:

    pip install pandas jira

Add Configuration details in Config json

    {
      "url": "https://your-domain.atlassian.net",
      "username": "your-email@example.com",
      "api_key": "your-api-token"
    }


Run the script:

    python app.py

# 📬 Contact

For questions or suggestions, feel free to open an issue or reach out! to chandu.charan007@gmail.com
