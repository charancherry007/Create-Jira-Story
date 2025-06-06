import json
from jira import JIRA
import pandas as pd

def connectToJira(configPath):
    try:
        with open(configPath,'r') as file:
            config = json.load(file)
            url = config.get('jira_url')
            email = config.get('username')
            key = config.get('api_token')
            if not all([url, email, key]):
                print('Please Check url, email, api_key in config json!!')
                raise ValueError("Please Check url, email, api_key in config json!!")
            jira = JIRA(server=url, basic_auth=(email,key))
            print('Connected to Jira!!')
            return jira
    except FileNotFoundError:
        print("Config File Not Found!")

def createStory(jiraConnection,excelFile):
    try:
        df = pd.read_excel(excelFile, dtype={'ID':str})
        if 'ID' not in df.columns:
            df['ID'] = None
            df['ID'] = df['ID'].astype(str)
            
        for index, row in df.iterrows():
            if pd.notna(row.get('ID')):    
                continue
            storyData = {
                'project':{'key':row.get('Project Key')},
                'summary':row.get('Summary'),
                'description': row.get('Description'),
                'issuetype':{'name':row.get('Issue Type')},
                'assignee':{'name':row.get('Assignee')},
                'environment':row.get('Environment',None),
                'customfield_10016': row.get('Story Points',None),
                #Add other fields and row_Id's here
             }
            storyData = {k:v for k,v in storyData.items() if v is not None}
            newStory = jiraConnection.create_issue(fields=storyData)
            df.at[index,'ID'] = str(newStory.key)
            df.to_excel(excelFile, index=False)
            print(row.get('Issue Type')+" is Created with ID: "+ newStory.key)
    except Exception as e:
        print("There was an error while creating issue please check the logs Probabiliy missing/incorrect key "+{str(e)})

excel_Path = 'StoriesData.xlsx'
config_Path = 'jiraConfig.json'
jira_connect = connectToJira(config_Path)
if jira_connect:
    createStory(jira_connect,excel_Path)
    print('Thanks! Namasthe!! Jai Hind!!!')
else:
    print("Jira Connection not found!!")