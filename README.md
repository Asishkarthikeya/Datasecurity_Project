Cloning the Repository
Clone the Repository: Open your terminal and navigate to the directory where you want to clone the repository: cd /path/to/your/directory
Then, clone the repository by running the following command: git clone https://github.com/Asishkarthikeya/Datasecurity_Project.git
Navigate to the Cloned Directory: Once the repository is cloned, navigate to the project directory: cd DataSecurity_Project


Level 1 Instructions

Before running the code, ensure that Python and pip are installed on your system.

Verify Python Installation:

python --version  # or python3 --version

Verify pip Installation:

pip --version
Install Required Libraries: Install the required dependencies using pip: pip install efficientnet_pytorch==0.7.1 scikit_learn==1.4.2
Install Additional Dependencies: Run the following command to install necessary libraries:

pip install torch torchvision matplotlib
Running the Code
Navigate to the Directory Containing level_1.py: cd /path/to/your/level_1.py
Execute the Script: Run the script with the following command:

python level_1.py
Resolving SSL Errors
If you encounter the following SSL error:

<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)>
To resolve this:

Update Certificates on macOS: Run the following command in your terminal to update certificates:

/Applications/Python\ 3.12/Install\ Certificates.command
(Replace 3.12 with your installed Python version, e.g., 3.11, 3.9.)

Retry Running the Script: After updating the certificates, run the script again:

python level_1.py
Level 2 and Level 3 Instructions
Running Level 2 and Level 3 Scripts: If you have already executed Level 1, simply run the following commands to execute the Level 2 or Level 3 scripts: python level_2.py python level_3.py
The necessary dependencies will have already been installed during Level 1.

If Level 1 Hasn't Been Executed: Follow the Prerequisites and Running the Code steps mentioned above for Level 1, then execute the respective script for Level 2 or Level 3.
