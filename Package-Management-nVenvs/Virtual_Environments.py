'''
This is a test project hightlighting the features of the virtualenv module on python. It creates a virtual environment within the direcrory that the termianl is currently pointing to when executed. NOTE The code below should be run in the terminal
'''

# STEP1: Istallation of the Virtualenv package
'''
The code below installs the Virtualenv package using the pip package mangement tool for python. If the package is already installed on your desktop then the code can be left commented otherwise remove the # charater to run the code and install the package first
'''
    # pip install virtualenv

# STEP2: creating a virtual environment 
'''
Navigate to the project directory where you want to create a virtual environment and run the code below to create the virual environment
'''
    # virtualenv my_env

# STEP3: Activate the virtual environment
'''
The virtual environment can be activated using the script below on windows 11 the source command has to be prefixed however for previous windows versions the source prefix is not necessary
'''
    # source my_env/Scripts/activate

# STEP4: List all the directories that are installed in the given directoty
'''
This command lists all the virtual environments that are available in a given directory storing virtual environments
'''
    # ls -d */

# STEP5: Print path to a virtual environment
'''
The code below displays the path to an active virtual environment and can be used from any available directory in the termianl.
'''
    # echo $VIRTUAL_ENV

# STEP6: List installed packages
'''
This code lists all the packages that are installed in a virtual environment that is currently active
'''
    # pip list 

# STEP7: Deactivating a virtual environment
'''
This code deactivates a virtual environment but does not delete it from the directory it was created in. 
'''
    # deactivate

# STEP8: Delete a virtual environment
'''
This code shows how to delete a virtual environment from a directory that it was created in
'''
    # rm -rf my_env

# Installing packages using the requirements.txt file 
'''
The code below allows for packages stores in a request.txt file to be installed into a virtual environmet 
'''
    # pip install -r /path/to/requirements.txt

# Copying packages within a virtual environment onto a requirements.txt file for easy replication on another desktop environment
'''
The code below allows for packages already installed in a virtual environment to be copied onto a request.txt file for easy replication
'''
    # pip freeze >> /path/to/requirements.txt