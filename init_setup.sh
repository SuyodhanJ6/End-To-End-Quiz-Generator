echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "activating the environment" 
conda activate ./venv

# Initialize Conda in bash
conda init bash

# Close and restart your shell or open a new terminal window here

echo [$(date)]: "installing the requirements" 
pip install -r requirements.txt
echo [$(date)]: "END" 
