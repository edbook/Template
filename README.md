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

## Virtual environment -- Poetry

To avoid dependencies clashing between projects it is best to create a virtual environment in which you will build your project. For this we use Poetry,
see [Poetry docs](https://python-poetry.org/docs/#installation) for recommended install method.


Run the following after Poetry has been installed, which will create a virtualenv and install all dependencies and custom Sphinx extensions. It also comes with a custom cli tool `hicli` to do all kinds of boring chores. See `hicli --help` for docs or [the hicli README](cli/README.md)

```sh
poetry shell
poetry install
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
git checkout -b <branch-name>
```
There should now be a template folder in your project root folder.

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

In short
========

* install Python
* clone this repository
* install [Poetry](https://python-poetry.org/docs/#installation)
* set up Poetry 
  ```sh 
  poetry shell
  poetry install
  ```
* edit the .rst files
* compile
  ```sh
  make html
  ```
* check out *_build/html/index.html* (if everything worked)
