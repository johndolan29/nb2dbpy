# nb2dbpy
A command-line tool for converting between Databricks .py script files and .ipynb notebooks. This tool was build in collaboration with 
[Yoyodyne-Data-Science](https://github.com/Yoyodyne-Data-Science), thank you for setting the foundations for this tool.

## Overview
When working with Databricks, notebooks are often exported as .py files for easier version control and collaboration. However, these scripts may not be ideal for local development in VS Code. nb2dbpy bridges this gap by enabling seamless conversion between Databricks-formatted Python scripts and Jupyter notebooks directly from the command line.

## Features
- **Bidirectional Conversion**: Convert from .py scripts to .ipynb notebooks and vice versa.
- **Command-Line Interface**: Perform conversions easily without writing additional code.
- **Databricks Compatibility**: Handles Databricks-specific syntax and comments.
- **Preserves Cell Structure**: Maintains code and markdown cells accurately during conversion.

## Installation
Clone the repository and install the required dependencies:

```
pip install nb2dbpy
```

## Usage
Use nb2dbpy from the command line to perform conversions.

#### Converting from .py to .ipynb
To convert a Databricks-exported Python script to a Jupyter notebook:

```
nb2dbpy your_python_script.py
```

This command will generate your_python_script.ipynb in the same directory.

#### Converting from .ipynb to .py
To convert a Jupyter notebook into a Databricks-compatible Python script:

```
nb2dbpy your_notebook.ipynb
```
This will create your_notebook.py, ready for import into Databricks.

#### Specifying Output Files
You can specify a custom output file name using the -o or --output option:

```
nb2dbpy input_file.py -o custom_output.ipynb
```

#### Dealing with Existing Files
If the output file already exists, the tool will find the next available filename, for example, if you already have created test.py from test.ipynb, the tool with next create test(1).py to protect against overwriting. 

## Examples
#### Example 1: Converting a Databricks Script to a Notebook
Suppose you have a file analysis.py exported from Databricks. To convert it to a Jupyter notebook:

```
nb2dbpy analysis.py
```
Open analysis.ipynb with VS Code to continue your work locally.

#### Example 2: Converting a Notebook for Databricks
You have developed a notebook experiment.ipynb and now want to run it in Databricks:

```
nb2dbpy experiment.ipynb
```
Upload the resulting experiment.py to your Databricks workspace.

## Limitations
- Advanced notebook features like interactive widgets are not supported.

### License
This project is licensed under the MIT License.

### Contributions
Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.
