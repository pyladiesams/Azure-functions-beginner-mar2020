# Workshop Part 1 - Python Code Refactoring

In this part of the workshop we'll learn basic ways in which we can improve code readability and usability. The example we'll use is in Python, but
this is applicable to any programming language.

Open the [text_processing](https://github.com/pyladiesams/Azure-functions-beginner-mar2020/blob/master/workshop/part1_refactoring/text_processing.py) file. Keeping in mind the single responsibility principle we've discussed during the presentation what improvements can be made?

Try to:

* Improve the structure
* Make the code more readable
* Check for code duplication
* Check if the code is testable
* Make to code more robust
* Make the code more reusable


#### Let's create a virtual environment.
In your terminal run:

**Mac & Ubuntu:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**\
If you use `cmd`:
```bash
python -m venv .venv
.venv\Scripts\activate.bat 
```

If you use `PowerShell`:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1 
```

To install the dependencies run:
```bash
pip install -r requirements.txt
```

After finishing with this exercise, to deactivate the virtual environment run:
```bash
deactivate
```
