# SETUP

-The following commands were used to set up the environment:

    sudo pacman -S python-virtualenv
    <!-- installed the python virtual tool -->

    source venv/bin/activate
    <!-- running the shell activation script -->

    virtualenv venv
    <!-- generate a new isolated virtual environment -->

    pip install jupyterlab numpy matplotlib pandas
    <!-- installing the needed packages
    These are installed for every project, as the whole point of a virtual environment is that each is
    an isolated bubble.-->

    echo "venv/" >> .gitignore
    echo ".ipynb_checkpoints/" >> .gitignore
    echo "__pycache__/" >> .gitignore

    <!-- the block of code below is run via the terminal and it ensures that the virtual env. checkpoints are not committed -->

-AFter this, open the Jupyterlab desktop app and point it to the same folder.

    pip freeze > requirements.txt
    <!-- the command below dumps all the packages into a file such that in a new project we avoid the repetition of typing out the packages -->

-In the new projects run the lines of code below:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt