# 📘 Arithmetic Progression (A.P.) Calculator

A simple Python command-line program for generating an **Arithmetic
Progression (A.P.)** from a first term, common difference, number of
terms, or last term.

> ⚠️ **Important:** This is a simple educational calculator. Read the
> warnings before running it.

------------------------------------------------------------------------

## ⚠️ STEP 1 --- READ BEFORE USING

-   This project is intended for learning and simple mathematical
    calculations.
-   Invalid numeric input can cause `ValueError` and stop the program.
-   The current code uses `int()`, so decimal values are not accepted.
-   The sequence is generated with Python `range()`, so integer terms
    and an integer common difference are expected.
-   Leave **last term** empty when you want the program to use the
    entered number of terms.
-   Leave **number of terms** empty when you want the program to
    generate terms up to the entered last term.
-   If both are supplied, the current code uses the last-term branch and
    does not validate that `n` matches the generated number of terms.
-   A common difference of `0` produces repeated terms.
-   Negative common differences may produce an empty or unexpected
    result because of the way `range()` is used.
-   Input validation and detailed error handling are not implemented.
-   The permission prompt continues only when the exact lowercase input
    `y` is entered.
-   The final `else` contains `exit` rather than an explicit `exit()`
    call.

------------------------------------------------------------------------

## 🛠️ STEP 2 --- REQUIREMENTS

Install **Python 3.x**. Check with:

``` bash
python --version
```

Required third-party package:

``` bash
pip install termcolor
```

The `time` module is included with Python and does not need separate
installation.

------------------------------------------------------------------------

## 📁 STEP 3 --- REPOSITORY STRUCTURE

``` text
AP-Calculator/
├── ap.py
├── requirements.txt
└── README.md
```

  File                 Purpose
  -------------------- ----------------------
  `ap.py`              Main A.P. calculator
  `requirements.txt`   Required package
  `README.md`          Documentation

------------------------------------------------------------------------

## 📦 STEP 4 --- INSTALL THE DEPENDENCY

From the project directory:

``` bash
pip install -r requirements.txt
```

`requirements.txt` contains:

``` text
termcolor
```

------------------------------------------------------------------------

## ▶️ STEP 5 --- RUN THE PROGRAM

``` bash
python ap.py
```

Or:

``` bash
python3 ap.py
```

When prompted:

``` text
do you want to continue [y/n] :
```

enter `y` to continue.

------------------------------------------------------------------------

## 🎮 STEP 6 --- UNDERSTAND THE INPUT

The program asks for:

-   **First term** --- first value of the A.P.
-   **Common difference** --- difference between consecutive terms
-   **Number of terms (`n`)** --- how many terms to generate
-   **Last term** --- final value of the progression

The program allows one of `n` or the last term to be left empty.

------------------------------------------------------------------------

## 🧮 STEP 7 --- EXAMPLES

### Example 1: First term + common difference + number of terms

Input:

``` text
first term : 2
Common diffrence of : 3
no of terms n : 5
last term :
```

Output:

``` text
A.P = [2, 5, 8, 11, 14]
n terms = 5
```

The source calculates the last term using:

$$a_n = a + (n-1)d$$

### Example 2: First term + common difference + last term

``` text
first term : 2
Common diffrence of : 3
no of terms n :
last term : 14
```

Output:

``` text
A.P = [2, 5, 8, 11, 14]
n terms = 5
```

### Example 3: Both `n` and last term supplied

The current source enters its final calculation branch and generates the
sequence using the first term, last term, and common difference. It does
not check whether the supplied `n` is consistent with the result.

------------------------------------------------------------------------

## 📐 STEP 8 --- A.P. FORMULAS

### nth term

$$a_n = a + (n-1)d$$

### Number of terms

$$n = \frac{l-a}{d}+1$$

where `a` is the first term, `d` is the common difference, `n` is the
number of terms, and `l` is the last term.

> The current program generates terms directly with Python `range()`
> rather than implementing every standard A.P. formula separately.

------------------------------------------------------------------------

## ✨ FEATURES

-   🔢 Generates Arithmetic Progressions
-   ➕ Supports integer common differences
-   🎯 Can generate a sequence from a specified number of terms
-   📌 Can generate a sequence up to a supplied last term
-   📊 Displays the generated A.P. and number of terms
-   🎨 Uses `termcolor` for colored terminal output
-   ⏱️ Uses `time.sleep()` for a short startup delay

------------------------------------------------------------------------

## 🔐 STEP 9 --- USAGE NOTE

This project is useful for practicing Python `input()`, conditions,
`while` loops, lists, and `range()`, while learning the basic concept of
Arithmetic Progression.

It is **not intended to be a complete scientific mathematics
application**.

------------------------------------------------------------------------

## 💻 SOURCE CODE

The complete source is provided in `ap.py`.

``` python
from termcolor import colored
import time

banner='''
            ┏━━━┓━━┏━━━┓
            ┃┏━┓┃━━┃┏━┓┃
            ┃┃━┃┃━━┃┗━┛┃
            ┃┗━┛┃━━┃┏━━┛  
            ┃┏━┓┃┏┓┃┃━━━
            ┗┛━┗┛┗┛┗┛━━━
            ━━━━━━━━━━━━
            ━━━━━━━━━━━━
'''

print(colored(banner, "light_red",attrs=['bold']))

caption='''
this toos is made for  some mathematical calculation of (A.P).
 
    [A] enter first term
    [B] enter common diffrence
    [C] enter no of terms
    [D] enter last term
    '''

permission=input(colored("do you want to continue [y/n] : ", "light_yellow"))

print()
print()
print(colored("DEVLOP BY :", "light_yellow", "on_light_red"), colored(" khalidx456", "light_cyan"))

print(colored(caption, "light_blue"))

print(colored("Note", "light_yellow", "on_red"),colored(": if value is not given then press enter.", "white"))
print()

if permission=="y":
    time.sleep(0.3)
    
    while True:
        first_terms=int(input(colored("first term : ", "light_green")))
        common_diff=int(input(colored("Common diffrence of : ", "light_green")))
        nterms=input(colored("no of terms n : ", "light_green"))
        last_terms=input(colored("last term : ", "light_green"))
        
        if last_terms=="":
            nA=[]
            calc_last_terms=first_terms+(int(nterms)*common_diff)-common_diff
            for termsA in range(first_terms,calc_last_terms+1,common_diff):
                nA.append(termsA)
            print()
            print(colored("A.P = ", "light_yellow"),colored(nA, "light_cyan"))
            
            print(colored("n terms = ", "light_yellow"), colored(len(nA), "light_green"))
            print()
            
        elif nterms=="":
            nB=[] 
            for termsB in range(first_terms,int(last_terms)+1,common_diff):
                nB.append(termsB) 
                
            print()
            print(colored("A.P = ", "light_yellow"),colored(nB, "light_cyan"))
            
            print(colored("n terms = ", "light_yellow"), colored(len(nB), "light_green"))
            print()
            
        else:
            nC=[] 
            for termsC in range(first_terms,int(last_terms)+1,common_diff):
                nC.append(termsC) 
                
            print()
            print(colored("A.P = ", "light_yellow"),colored(nC, "light_cyan"))
            
            print(colored("n terms = ", "light_yellow"), colored(len(nC), "light_green"))
            print()
            
        print(colored("Thanks !!", "light_red"))       
        print()       
        print()     
else:
    exit
```

------------------------------------------------------------------------

## 🚀 POSSIBLE IMPROVEMENTS

-   Add `try/except` error handling.
-   Support decimal values.
-   Validate negative/zero common differences.
-   Validate consistency between `n` and the last term.
-   Add a proper quit option inside the loop.
-   Use functions and a `main()` function.
-   Add A.P. sum calculation.
-   Improve support for descending progressions.
-   Improve spelling and variable names.
-   Add automated tests.

------------------------------------------------------------------------

## 📄 LICENSE

Add your preferred open-source license, such as MIT, if you plan to
publish the project.

------------------------------------------------------------------------

## ⭐ PROJECT SUMMARY

**AP Calculator** is a lightweight Python terminal program for
practicing Arithmetic Progression calculations.

**Main file:** `ap.py`\
**Dependency:** `termcolor`\
**Run:** `python ap.py`
