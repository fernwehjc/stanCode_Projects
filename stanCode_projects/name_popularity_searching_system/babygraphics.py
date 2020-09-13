"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

File: babygraphics.py
Name: Jade Yeh
This file shows graphic of the name_data.
The user provides names and the coder will draw a line chart containing year and rank for the certain names.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000  # Width of the canvas.
CANVAS_HEIGHT = 600  # Height of the canvas.
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]  # Year list for all files in database.
GRAPH_MARGIN_SIZE = 20  # The edge size for the canvas.
COLORS = ['red', 'purple', 'green', 'blue', 'orange']  # Color list for coloring texts and lines.
TEXT_DX = 2  # Text distance from a vertical line.
LINE_WIDTH = 2  # The width size of a line.
MAX_RANK = 1000  # The max rank in the files.


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # Divides the width of the line chart by the total number of years and get x-coordinate by year.
    space = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + year_index * space
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw the top frame line for the line chart.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Draw the bottom frame line for the line chart.
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Draw vertical lines and texts for line chart by year.
    for yr in range(len(YEARS)):
        x = get_x_coordinate(width=CANVAS_WIDTH, year_index=yr)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[yr], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_num = 0
    # Look up each name for the year&rank data that the user wants to view.
    for name in lookup_names:
        # 1st for-loop creates a list of rank by year order.
        rank_lst = []
        for i in range(len(YEARS)):
            #  Look up data in dict{year: rank} by year in string format.
            if str(YEARS[i]) not in name_data[name]:
                # Assign a rank as '9999' for a non-existed name in the database for a certain year.
                rk = '9999'
            else:
                rk = name_data[name][str(YEARS[i])]
            # List the rank in an integer format.
            rank_lst.append(int(rk))
        # 2nd for-loop creates a list of x- and y-coordinate by year order.
        x_y_lst = []
        for j in range(len(YEARS)):
            x = get_x_coordinate(width=CANVAS_WIDTH, year_index=j)
            y = get_y_coordinate(height=CANVAS_HEIGHT, rank=rank_lst[j])
            x_y_lst.append(x)
            x_y_lst.append(y)
            # Show '*' as the rank value for the name with actual rank over the MAX_RANK constant.
            if rank_lst[j] > MAX_RANK:
                canvas.create_text(x + TEXT_DX, y, text=str(name) + '*', anchor=tkinter.SW,
                                   fill=COLORS[color_num % len(COLORS)])
            # Show the name with its rank value.
            else:
                canvas.create_text(x+TEXT_DX, y, text=str(name)+str(rank_lst[j]), anchor=tkinter.SW,
                                   fill=COLORS[color_num % len(COLORS)])
        # 3rd for-loop draws the trend lines.
        for n in range(len(YEARS)-1):
            canvas.create_line(x_y_lst[n * 2], x_y_lst[n * 2 + 1], x_y_lst[n * 2 + 2],
                               x_y_lst[n * 2 + 3], width=LINE_WIDTH, fill=COLORS[color_num % len(COLORS)])
        # Change color for the next name data.
        color_num += 1


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the index of the current rank
    in the rank list, returns the y coordinate of one end of the trend line
    associated with that rank.

    Input:
        height (int): The height of the canvas
        rank (int): The rank associated with a certain name in a certain year
    Returns:
        y_coordinate (float): The y coordinate of one end of the trend line associated
                              with the rank of the current year.
    """
    # Divided the line chart frame by MAX_RANK vertically and equally AND get y by the current rank.
    if rank > MAX_RANK:
        # Set y as the bottom frame line when the current rank is over MAX_RANK.
        y = height - GRAPH_MARGIN_SIZE
    else:
        y = (height - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * rank + GRAPH_MARGIN_SIZE
    return y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
