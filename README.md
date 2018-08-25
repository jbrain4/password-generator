# Password Generator
---
A memorable password generator written in Python 3.7. Based on  [xkpasswd.net](http://www.xkpasswd.net/).

Some examples of passwords include:
```
FARMER\journalism\BATTERIES\03
74+BOXING+done+COLUMNISTS~~
**LOGS.lakes.32****
```

## Getting Started

### Including PasswordGenerator in Your project
- Have a copy of `PasswordGenerator.py` and `dict.txt` in your project directory
- Add the following line of code to the top of your Python program.
```python
from PasswordGenerator import PasswordGenerator
```
- Initiate an instance of the `PasswordGenerator` object
```python
passwdGenerator = PasswordGenerator()
```

### Generator A Basic Password
After initiating a new instance of `PasswordGenerator`, you can just call the `generatePassword()` method like so.
```python
passwdGenerator.generatePassword()
```
**Note:** `generatePassword()` returns the generated passwords in a list, even if there is only one generated password.
