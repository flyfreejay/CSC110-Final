"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

main.py for our final project submission. If you wish to interactively view our visual data,
uncomment a specified block below and run the main.py. Follow the instructions on the terminal.

Copyright and Usage Information
===============================
This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    #UNCOMMENT THE BLOCK BELOW TO USE THE INTERACTIVE TERMINAL FEATURE
