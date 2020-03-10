<div align="center">
    <h1>Introduction to Azure Functions in Python</h1>
    <p>Level: Beginner</p>
</div>

### Presentation: [DOWNLOAD IT HERE](https://github.com/pyladiesams/Azure-functions-beginner-mar2020/tree/master/workshop/presentation_slides)

## Project description

What you'll learn:
* Enough terminology and concepts to be able to read other Azure Functions resources without being perpetually confused.
* A painless way to get Azure Functions running on your computer.
* How to get started with Azure Functions in Python.
* How to properly structure & refactore your Python code, so you can migrate your application to the cloud.
* Helpful external resources for the material covered here.

By the end of this workshop, you’ll be ready to start integrating other Azure frameworks using Python Azure Functions. 

## Setup:

### Set up Python 3.
Azure Functions supports Python 3.6.x or 3.7.x.
If you have a lower version, you have to update it.
To install Python you need to download an installer:
* Windows: https://www.python.org/downloads/windows/
* Linux, Mac already has to have Python3, if you're not sure, type in command line:
`python --version` or `python3 --version`
and version will be in a first line. If you don't have proper version of python:
* Mac (you have to have [brew](https://brew.sh)): ``` brew install python3```
* Linux (Ubuntu): ```sudo apt-get update
sudo apt-get install python3.7```


### Install [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools).

To install Azure Functions Core Tools use:

* Windows: 

To install runtime with [npm](https://phoenixnap.com/kb/install-node-js-npm-on-windows) in your terminal run: ```npm i -g azure-functions-core-tools@2 --unsafe-perm true```

To install with [chocolatey](https://chocolatey.org/docs/installation): ```choco install azure-functions-core-tools```

Notice: To debug functions under vscode, x64 bitness is required: ```choco install azure-functions-core-tools --params "'/x64'"```

* Mac:

Using `npm`:\
Set up [npm](https://treehouse.github.io/installation-guides/mac/node-mac.html). In your terminal run: ```npm install -g azure-functions-core-tools```

Using `brew`:\

``` 
brew tap azure/functions 
brew install azure-functions-core-tools@2 
```

To verify that `Azure Functions Core Tools` is installed correctly on your machine, run the func command in your terminal: ```func```

* Linux:

In your terminal run:

```
wget -q https://packages.microsoft.com/config/ubuntu/18.10/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

### Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).
Follow the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

### Set up a [free Azure account](https://azure.microsoft.com/en-gb/).
 
### Install [Postman](https://www.postman.com/).

### Install [Docker](https://docs.docker.com/install/) and make sure it is running.

## Requirements
* Python 3.6.x or 3.7.x.

## Usage
* Clone the repository.
* Go to [workshop](https://github.com/pyladiesams/Azure-functions-beginner-mar2020/tree/master/workshop) and start with the README.md.

## Credits
This workshop was set up by [@PyLadiesAMS](https://www.meetup.com/PyLadiesAMS/) and [Dana Arsovska](https://github.com/Dzvezdana).
