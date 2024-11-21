# Installation / Startup Guide

## Getting the Project from GitLab
To clone the project repository from GitLab, run the following command:
```
git clone git@github.com:Andoxtra/maln.git
```
Then, switch to the development branch:
```
git checkout master
```

### If No Files Appear (Other Than README.md)
If you only see the README.md file and no other project files, please use the following command to fetch the latest updates:
```
git fetch origin
```

## Starting the Program

## Setup venv
To create a .venv folder execute:
```
python -m venv .venv
```
To activate execute:

Windows:
```
./.venv/Scripts/activate
```
Linux:
```
source ./.venv/bin/activate
```
### Installing Requirements
To install the necessary packages listed in `requirements.txt`, execute:
```
pip install -r ./txt/requirements.txt
```

### Running the Code
Start the application by running:
```
python main.py
```
You can now interact with the figures in the console using the **d** key and pressing **Enter**. The playfield will be displayed in a separate window.

## Tip
For better multitasking, use **Windows + Arrow Keys** to quickly align the console and playfield windows.

## Configuration of the Program
- **Playfield Display**: You can customize how the playfield is presented in the `main.py` file. Choose between displaying it in a window using Tkinter or using the playboard directly.
  
- **Player Configuration**: Modify the input/output devices for each player in the `playerConfig.py` file.

## Important Notes
- Please be aware that the Physical or LCD Display configuration options cannot be used unless you are operating with the playboard itself. Make sure to choose the appropriate settings based on your setup. 

