<div align="center">
    <h1>Introduction to Azure Functions in Python</h1>
    <p>Level: Beginner</p>
</div>

### Presentation: ADD LINK HERE

## Project description

What you'll learn:
* Enough terminology and concepts to be able to read other Azure Functions resources without being perpetually confused
* A painless way to get Azure Functions running on your computer
* How to get started with Azure Functions in Python
* How to properly structure & refactore your Python code, so you can migrate your application to the cloud 
* Helpful external resources for the material covered here

By the end of this workshop, you’ll be ready to start integrating other Azure frameworks using Python Azure Functions. 

## Setup:

### Set up a Python 3.
Azure Functions supports Python 3.6.x or higher.
If you have a lower version, you have to update it.
To install Python you need to download an installer:
* Windows(https://www.python.org/downloads/windows/)
* Linux, Mac already has to have Python3, if you're not sure, type in command line:
`python --version` or `python3 --version`
and version will be in a first line. If you don't have proper version of python:
* Mac (you have to have [brew](https://brew.sh)): ``` brew install python3```
* Linux (Ubuntu): ```sudo apt-get update
sudo apt-get install python3.7```


### Install [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools).

To install Azure Functions Core Tools use:

* Windows: 

In your terminal run: ```npm i -g azure-functions-core-tools@2 --unsafe-perm true```

* Mac:

In your terminal run: ```npm install -g azure-functions-core-tools```
To verify that `Azure Functions Core Tools` is installed correctly on your machine, run the func command in your terminal: ```func```

* Linux:

In your terminal run:

```
wget -q https://packages.microsoft.com/config/ubuntu/18.10/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

### Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
Follow the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

### Set up a [free Azure account]((https://azure.microsoft.com/en-gb/)).
 
### Install [Postman](https://www.postman.com/).


## Requirements
* Python 3.6.x or higher.

## Usage
* Clone the repository.
* Go to [workshop]() and start with the README.md.

## Credits
This workshop was set up by [@PyLadiesAMS](https://www.meetup.com/PyLadiesAMS/) and [Dana Arsovska](https://github.com/Dzvezdana).
