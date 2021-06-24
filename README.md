# KOSS-Task

## TOOLS USED:


#### Argparse:

- It is a module from Python's standard library
- Argparse allows you to build professional command line interfaces in an easy way
- It has a very nice command line interface, including help messages, defined during setup 

#### PyGithub:

- PyGithub is a Python library to use the Github API v3
- PyGithub helps you GET specific information with limited lines of code

## THE PROCESS:

I started the task by learning what an API really is. Once I was had gained some idea on this I started reading about GET requests method. Python was a popular back-end language that I was a little familiar with. I decided to use python when I found the PyGithub library which was very straightforward and let you access the Github REST API.
First I started searching for an easy way to make a command line program with python. I went with Argparse as it was in the standard library and pretty easy to learn and use in simple program line codes. Then I tried to understand what parsering was.
For making this command line program as I did not require a lot of knowledge about the Argparse library so I stuck to the basics and learned how to make ArgumentParser objects and use them to add arguments and use those arguments in the code.
Once I was done with the basic command line program I went on to read more about PyGithub. I learnt how to make a Github object and then found out how to GET a user with a username and get any repository of the user with the repository name using get_user and get_repo. Then I continued to learn more about PyGithub to access user details and repository details.

#### Making a Command line program:

- Using Argparse the default python module  for creating command lines programs
- Creating a ArgumentParser object parser. The ArgumentParser object will hold all the information necessary to parse the command line into Python data types
- The argparse.ArgumentParser lets you add a description to your programs
- Using add_arguemnt to give information about two agruments namely, username and repository both of type string
- The arguments are parsed with parse_args()
- The parsed arguments are present as object attributes stored in the object args
- Now we can access the arguments using args.username and args.repository

#### Getting user info using GitHub API:

- Using PyGithub library
- Creating a Github object g
- Using get_user to GET user with specified username and assigning it to user
- Writing a function called user_info that prints the details needed extracting it from user

#### Getting repository info using GitHub API:

- Using PyGithub library
- Using g.get_repo to GET repository of the user with specified username and repository name and assigning it to repo
- Writing a function called print_repository that prints the details needed extracting it from repo
