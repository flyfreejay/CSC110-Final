"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

main.py for our final project submission. If you wish to interactively view our visual data,
uncomment a specified block below and run the main.py. Follow the instructions on the terminal.

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""
# IMPORTS
from bar_graph import draw_bar_graph
from bubble_map import draw_bubble_map
from bubble_map_delta_increase import draw_bubble_map_delta_increase
from scatter_plot import draw_scatter_plot
from tree_map import draw_tree_map

draw_bar_graph()
draw_tree_map()
draw_bubble_map()
draw_scatter_plot()
# Draw the bubble map where bubble sizes are based on the difference in change in hate crimes
# draw_bubble_map_delta_increase()

# UNCOMMENT THE BLOCK BELOW TO USE THE INTERACTIVE TERMINAL FEATURE
# print('*-------------------------------------------------------*')
# print('|        Welcome to our Final CSC1110 Project!          |')
# print('*=======================================================*')
# print('|       Here, you can use the terminal I/O to           |')
# print('|       interactively display our visual data           |')
# print('*=======================================================*')
# print('| 1) Display a bar graph comparing Asian hate crimes    |')
# print('|  in 2019 and 2020                                     |')
# print('| 2) Display a scatter plot showing the relationship    |')
# print('|  between the % of AAPI and hate crime                 |')
# print('| 3) Display a treemap that shows the number of  Asian  |')
# print('|  hate crimes to the political pref of the cities      |')
# print('| 4) Display a bubble map of Asian hate crimes using a  |')
# print('|  geographical map of US as the board (based on        |')
# print('|  a percentage increase)                               |')
# print('| 5) Display a bubble map of Asian hate crimes using a  |')
# print('|  geographical map of US as the board (based on the    |')
# print('|  net increase in hate crimes)                         |')
# print('| 6) Quit the program                                   |')
# print('*-------------------------------------------------------*')
# print()
# usr_input = ''
#
# while usr_input != '5':
#     usr_input = input('YOUR INPUT(1-5): ')
#     if usr_input == '1':
#         draw_bar_graph()
#
#     elif usr_input == '2':
#         draw_scatter_plot()
#
#     elif usr_input == '3':
#         draw_tree_map()
#
#     elif usr_input == '4':
#         draw_bubble_map()
#
#     elif usr_input == '5':
#         draw_bubble_map_delta_increase()
#
#     else:
#         print('The answer you gave is invalid, please try again!')
#
# print('You have quit the program successfully.')

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        # The names (strs) of imported modules
        'extra-imports': ['scatter_plot', 'bar_graph', 'bubble_map', 'tree_map',
                          'bubble_map_delta_increase'],
        'allowed-io': ['print', 'input'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
