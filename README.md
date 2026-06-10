# Password Strength Checker

## Overview

This is a simple Python console application that evaluates the strength of a user-provided password. The program checks the password against common security criteria and provides a strength rating along with suggestions for improvement.

The application continuously prompts the user for passwords until they choose to exit.

## Features

* Evaluates password strength based on:

  * Length
  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Assigns a strength rating:

  * Weak
  * Medium
  * Strong
* Provides feedback to improve password security
* Runs in a loop until the user enters `quit`

### Libraries Used

This project uses the following built-in Python library:

```python
import string
```

No external packages need to be installed.

## How to Run

1. Save the program.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the program.

## Example Usage

```text
Enter a password (or type 'quit' to exit): Password123

Password Analysis
-------------------
Score: 4/6
Strength: Medium

Suggestions:
- Password must contain a special character.
```

## Scoring 

| Criteria                   | Points |
| -------------------------- | ------ |
| Password length ≥ 12       | 2      |
| Password length 8–11       | 1      |
| Contains uppercase letter  | 1      |
| Contains lowercase letter  | 1      |
| Contains number            | 1      |
| Contains special character | 1      |

## Objectives

This project demonstrates the use of:

* Variables
* User input
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`)
* Lists
* String methods
* Basic password validation logic

