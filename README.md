# TD5_Python_Linux_similarities

## Exercice 1 : Working Directory

###1. Create an empty working directory called “td4”

`mkdir TD_Linux_Git_Python_Esilv`

###2. Initialize a Git repository in it

`cd TD_Linux_Git_Python_Esilv`
`git init`

###3. Install the Linux python3-pip package using your Linux package manager

`sudo apt-get install python3-pip`

###4. Install the VirtualEnv Python package using pip3

`virtualenv .env`

###5. Create a Python virtual environment called “.env”. Do you see the change in your working directory ?

`virtualenv .env`
`ls -all`

Un dossier .env a été crée.

###6. Activate your virtual environment. Do you see the change in your prompt ?

`source .env/bin/activate`

(.env) apparaît devant le prompt.

###7. List the Python packages installed in your virtual environment

`pip list --local`

###8. Does Git want you to commit something ? Do you think it is a good thing ?

`git status`

Non Git ne demande pas de commit.

###9. Create a .gitignore file to tell Git which files should be untracked

`touch .gitignore`
`nano .gitignore`

On ajoute .env/ dans le fichier.

###10. Does Git want you to commit something ? Do you think it is a good thing this time ?

Git demande de commit le fichier .gitignore. Oui c'est une bonne idée.

`git add .gitignore`

###11. Do your first commit and check that Git is happy now.

`git commit -m "Exercice1"`

##Exercice2 : Python Script

###1. Install the Python package Requests using pip

`pip install Requests`

###2. Create a Python script that returns the list of all place ids in Derbyshire.

`touch `
