# Instructions

This is a template for a web-based textbook/lecture notes for the University of Iceland's mathematics department, using sphinx (see sphinx-doc.org).
For the following instructions find out which version of python you are running by executing:
```bash
python --version
```
or
```bash
python3 --version
```
Either one will work fine as long as it is Python 3 but not Python 2.

## Virtual environment

To avoid dependencies clashing between projects it is best to create a virtual environment in which you will build your project. In this environment you will install all of the required dependencies without affecting other projects. Start by creating a directory which will become the root of your project, e.g. edbook. Open that directory.

### Anaconda

If you are using Anaconda run:
```bash
conda create --name <name-of-environment>
```
Activate your virtual environment by running in Linux or MacOS:
```bash
source activate <name-of-environment>
```
For Windows OS run:
```bash
activate <name-of-environment>
```
To deactivate the environment run:
```bash
source deactivate
```
```bash
deactivate
```
For Linux/MacOS and Windows respectively.

### Pip

If you are using pip run:
```bash
python3 -m venv <name-of-environment>
```
Activate your virtual environment by running in Linux or MacOS:
```bash
source <name-of-environment>/bin/activate
```
For Windows OS run:
```bash
<name-of-environment>\Scripts\activate.bat
```
To deactivate the environment run:
```bash
deactivate
```

## Installing packages

If you don't have git already start by installing git, either by running
```bash
sudo apt-get install git
```
for Linux/MacOS or by downloading and installing git from their website if you are using Windows.

Within your virtual environment git clone the Template project by running:
```bash
git clone https://github.com/edbook/Template.git
```
If you intend to work on the Template repository it is good practice to create a new branch to work on by running
```bash
git checkout -b iss53
```
There should now be a template folder in /home/user.
Now install all of the necessary packages needed to build the edbook project by running: 
```bash
sudo apt-get install python3-sphinx
sudo apt-get install python3-sphinx-rtd-theme
sudo apt-get install python3-setuptools
sudo apt-get install python3-sagecell
sudo apt-get install pandoc
```
For Windows users the packages from above can be downloaded using [pip](https://pypi.org/project/pip/)

Navigate to the template folder.
The following folders are in the template folder: 

* sagecell-extension
* toggleblock-extension
* ggbextension
* google-analytics
* hoverrole
* katex-extension
* panoptoextension
* datacamp-extension

You can install every custom extension with a single command:
```bash
make extensioninstall
```
list of extensions can be found and modified in the file `extension_names`:

Install each one in Linux/MacOS with:
```bash
make singleinstall EX=name_of_extension
```
Install each one in Windows with:
```bash
make extensioninstall name_of_extension
```
Alternatively you can navigate to each of the extension folders and run for Linux/MacOS: 
```bash
python3 setup.py build
sudo python3 setup.py install
```
Or Windows:
```bash
python(3) setup.py build
python(3) setup.py install
```

Finally you should be able to run the command to see if everything worked out:
```bash
make html
```
You should be able to produce the html files according to the .rst documents.

If you get: `WARNING: extension 'sagecell.sagecell' has no setup() function; is it really a Sphinx extension module?`, go to sagecell-extension and run: 
```bash
sudo python3 setup.py install --user
```

You can now edit the template in /template/chapter01.rst and compile the html file with the make html command. The html pages are in /template/_build/html.

Once you have edited your content run `make clean` before you build again with `make html`

# Cloning other repositories for edbook

To begin working on other courses for edbook, navigate back to your original project folder, which you created before cloning the Template repository.
Make sure that your virtual environment is activated and clone whatever project you want to work on, for example:
```bash
git clone https://github.com/edbook/Numerical-analysis.git
```
Your project structure should now look something like this:
```
edbook                      # Project root
└── Template                # Template repository
└── Numerical-analysis      # Numerical analysis repository
└── <name-of-environment>   # Virtual environment folder
```
You should now be able to build the html or pdf files for your project.

Sphinx
======
Information on how to install sphinx can be found here: http://sphinx-doc.org/latest/install.html

Instructions for getting started with sphinx are here: http://sphinx-doc.org/latest/tutorial.html

This template comes with a source directory, `conf.py` file with the values set as we found convenient for Mathematical Analysis I (the aprropriate project title and author name need to be inserted in certain places in the file), makefile, and a slightly modified version of the Read the Docs theme (https://docs.readthedocs.org/en/latest/theme.html) with Icelandic language settings and the Univeristy of Iceland and Raunvísindadeilds logos. It is therefore not necessary to run sphinx-quickstart to set up the project.


Pandoc
======
Sphinx generates html and latex files from rst files.
Pandoc can be used to convert files from tex to rst (and convert between many other filetypes) 

Information on pandoc installation can be found at http://pandoc.org/installing.html.

A command like the following can then be used to convert latex to rst (more info at http://pandoc.org):

pandoc -t rst filename.tex -o filename.rst

A few things to have in mind when using pandoc to convert latex to rst:

-   The conversion ignores commands such as \block, \frame, \theorem, and \proof
    You might want to replace such commands with \section, \subsection, \subsubsection, \paragraph, \subaparagraph before conversion.

-   math ($...$) within bold/italicized text sections


Sphinx extensions
=================
Many extensions have been written to add features and modifications to sphinx projects. 
Several extensions come bundled with sphinx: http://sphinx-doc.org/extensions.html

For the custom extensions see README in each folder.

