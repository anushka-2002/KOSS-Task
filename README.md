# KOSS-Task
TOOLS USED:


Argparse:

-> It is a module from Python's standard library

-> Argparse allows you to build professional command line interfaces in an easy way

-> It has a very nice command line interface, including help messages, defined during setup 

PyGithub:

-> PyGithub is a Python library to use the Github API v3

-> PyGithub helps you GET specific information with limited lines of code

THE PROCESS:

Making a Command line program:

-> Using Argparse the default python module  for creating command lines programs

-> Creating a ArgumentParser object parser

-> The ArgumentParser object will hold all the information necessary to parse the command line into Python data types

-> The argparse.ArgumentParser lets you add a description to your programs

-> Using add_arguemnt to give information about two agruments namely, username and repository both of type string

-> The arguments are parsed with parse_args()

-> The parsed arguments are present as object attributes stored in the object args

-> Now we can access the arguments using args.username and args.repository

Getting user info using GitHub API:

-> Using PyGithub library

-> Creating a Github object g

-> Using get_user to GET user with specified username and assigning it to user

-> Writing a function called user_info that prints the details needed extracting it from user

Getting repository info using GitHub API:

-> Using PyGithub library

-> Using g.get_repo to GET repository of the user with specified username and repository name and assigning it to repo

-> Writing a function called print_repository that prints the details needed extracting it from repo
