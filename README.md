# TD5_Python_Linux_similarities

## Exercice 1 : Working Directory

### 1. Create an empty working directory called “td4”

`mkdir TD_Linux_Git_Python_Esilv`

### 2. Initialize a Git repository in it

`cd TD_Linux_Git_Python_Esilv`
`git init`

### 3. Install the Linux python3-pip package using your Linux package manager

`sudo apt-get install python3-pip`

### 4. Install the VirtualEnv Python package using pip3

`virtualenv .env`

### 5. Create a Python virtual environment called “.env”. Do you see the change in your working directory ?

`virtualenv .env`
`ls -all`

Un dossier .env a été crée.

### 6. Activate your virtual environment. Do you see the change in your prompt ?

`source .env/bin/activate`

(.env) apparaît devant le prompt.

### 7. List the Python packages installed in your virtual environment

`pip list --local`

### 8. Does Git want you to commit something ? Do you think it is a good thing ?

`git status`

Non Git ne demande pas de commit.

### 9. Create a .gitignore file to tell Git which files should be untracked

`touch .gitignore`
`nano .gitignore`

On ajoute .env/ dans le fichier.

### 10. Does Git want you to commit something ? Do you think it is a good thing this time ?

Git demande de commit le fichier .gitignore. Oui c'est une bonne idée.

`git add .gitignore`

### 11. Do your first commit and check that Git is happy now.

`git commit -m "Exercice1"`

## Exercice2 : Python Script

### 1. Install the Python package Requests using pip

`pip install Requests`

### 2. Create a Python script that returns the list of all place ids in Derbyshire.

`touch script.py`
Voir script.py

### 3. Commit your changes in Git

`git commit -m "Exercice2`

## Exercice 3 : Python Module

### 1. Create a Python module with a get_manor_ids function that takes a place id as parameter and returns the list of manors

`touch script1.py`
Voir script1.py (sans if __name__ == ’__main__’ :)

### 2. Check that calling your module does not produce any output

`.env/bin/python3 script1.py`

Aucun output en sortie losrque j'appelle le module.

### 3. To test your module, open a python interpreter and call your function with the first place id from Derbyshire

`.env/bin/python3`
`import script1`
`script1.get_manor_ids(1036)`
On obtient l'output suivant : [{'id': 13038}]
`exit()`

### 4. Add a if __name__ == ’__main__’ : block with your previous test, at the end of your module, to make it usable as a script

`if __name__ == '__main__' :
	print(get_manor_ids(1036))`

### 5. Check that calling your module now does produce an output

`.env/bin/python3 script1.py`
Ob obtient le même outuput : [{'id': 13038}]

### 6. Commit your changes in Git

`git add script1.py`
`git commit -m "Exercice3`
