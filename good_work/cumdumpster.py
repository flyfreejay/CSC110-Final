"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

main.py for our final project submission. If you wish to interactively view our visual data,
uncomment a specified block below and run the main.py. Follow the instructions on the terminal.

Copyright and Usage Information
===============================

TODO

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""
# IMPORTS
from bar_graph import *
from bubble_map_with_two_traces import *
from scatter_plot import *
from tree_map_political_party import *

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['scatter_plot', 'bar_graph',
                          'bubble_map_with_two_traces', 'tree_map_political_party'],
        'allowed-io': ['print', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # UNCOMMENT THE BLOCK BELOW TO USE THE INTERACTIVE TERMINAL FEATURE
    print('*-------------------------------------------------------*')
    print('|        Welcome to our Final CSC1110 Project!          |')
    print('*=======================================================*')
    print('|       Here, you can use the terminal I/O to           |')
    print('|       interactively display our visual data           |')
    print('*=======================================================*')
    print('| 1) Display a bar graph comparing Asian hate crimes    |')
    print('|  in 2019 and 2020                                     |')
    print('| 2) Display a scatter plot showing the relationship    |')
    print('|  between the % of AAPI and hate crime                 |')
    print('| 3) Display a treemap that shows the number of  Asian  |')
    print('|  hate crimes to the political pref of the cities      |')
    print('| 4) Display a bubble map of Asian hate crimes using a  |')
    print('|  geographical map of US as the board                  |')
    print('| 5) Quit the program                                   |')
    print('*-------------------------------------------------------*')
    print()
    usr_input = ''

    while usr_input != '5':
        usr_input = input('YOUR INPUT(1-5): ')
        if usr_input == '1':
            draw_anti_asian_comparison()

        elif usr_input == '2':
            draw_aapi_to_asian_hatecrime()

        elif usr_input == '3':
            draw_total_aapi_hate_crime_2020_tree_map()

        elif usr_input == '4':
            draw_bubble_map()

        else:
            print('The answer you gave is invalid, please try again!')

    print('You have quit the program successfully. Give us a 4.0!')
