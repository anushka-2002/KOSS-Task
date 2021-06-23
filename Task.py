import argparse
import base64
from github import Github

parser = argparse.ArgumentParser(description='Find Info on Users and their Repos')

# To add two arguements username and repository

parser.add_argument("username", type = str, help = "Enter username")
parser.add_argument("repository", type = str, help = "Enter repo name")
args = parser.parse_args()

def print_repository(x):                     #Function to print repo details
    print("REPOSITORY DETAILS:")
    print("Repository Name : ", x.full_name)
    print("Forks count : ", x.forks)
    print("Stargazers count : ", x.stargazers_count)
    print("Watchers count : ", x.watchers_count)
    print("Topics of the repository : ")
    for i in x.get_topics():
        print(i)
    print("License: ", base64.b64decode(x.get_license().content.encode()).decode())
    print("\n") 

def user_info(x):                            #Function to print user details
    print("USER DETAILS: ")    
    print("Username: ",user.login) 
    print("Name: ",x.name)
    print("Avatar URL: ",user.avatar_url)
    print("URL to the github handle: ",user.html_url)
    print("Email: ",user.email)
    print("Biodata: ",user.bio)
    print("Followers: ",user.followers)
    print("Following: ",user.following)
    print("\n")     

# To get user using github object g

g = Github()      
user = g.get_user(args.username)

# To print user info

user_info(user)

# To get a repository of a specified user

repo = g.get_repo(f"{args.username}/{args.repository}")

# To print repo info

print_repository(repo)

#python3 Task.py x4nth055 pythoncode-tutorials


    
