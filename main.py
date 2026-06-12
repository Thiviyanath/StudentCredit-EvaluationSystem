
from graphics import *  # Importing graphics module
progress = trailer = exclude = retriever = 0
ordered_progression_list = []
prostate = "y"  # Set default state of loop in progression() to run
user = "staff"
output_type = ""
progress_list, trailer_list, retriever_list, exclude_list, = [], [], [], []


def progression():
    global progress, trailer, exclude, retriever  # Making variables available globally
    progress = trailer = exclude = retriever = 0
    global progress_list, trailer_list, retriever_list, exclude_list
    global prostate  # State of progression() loop, used globally for histogram()
    global user
    user = ""
    global output_type
    output_type = ""
    while True:
        try:
            user = input("User List (input 1 or 2)\n"
                         "1 : Staff\n"
                         "2 : Student\n"
                         "Select user: ")
            if user == "1":
                while True:
                    try:
                        print()
                        output_type = input("Select output type (input 1 or 2 or 3)\n"
                                            "1 : Part 1 (histogram)\n"
                                            "2 : Part 2 (list)\n"
                                            "3 : Part 3 (save to progression.txt as text)\n"
                                            "Select output type: ")
                        if output_type == "1":
                            break
                        if output_type == "2":
                            break
                        if output_type == "3":
                            break
                        raise IncorrectOutputType
                    except IncorrectOutputType:
                        print(end="")
                break
            if user == "2":
                break
            raise IncorrectUser
        except IncorrectUser:
            print()
    prostate = "y"
    while prostate == "y":
        try:
            def check_input_credits(input_credits):  # Check if input credits are x20 and in range
                if input_credits % 20 or input_credits < 0 or input_credits > 120:
                    raise OutOfRange

            pass_credits = int(input("Enter your total PASS credits: "))
            check_input_credits(pass_credits)
            defer_credits = int(input("Enter your total DEFER credits: "))
            check_input_credits(defer_credits)
            fail_credits = int(input("Enter your total FAIL credits: "))
            check_input_credits(fail_credits)
            credit_total = pass_credits + defer_credits + fail_credits
            if credit_total != 120:
                raise TotalIncorrect
            if pass_credits >= 100:
                if fail_credits + defer_credits < 20:
                    progression_outcome = "Progress"
                    print(progression_outcome)
                    progress += 1
                    progress_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
                else:
                    progression_outcome = "Progress (module trailer)"
                    print(progression_outcome)
                    trailer += 1
                    trailer_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
            elif pass_credits >= 40:
                if fail_credits == 80:
                    progression_outcome = "Exclude"
                    print(progression_outcome)
                    exclude += 1
                    exclude_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
                else:
                    progression_outcome = "Module retriever"
                    print(progression_outcome)
                    retriever += 1
                    retriever_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
            elif fail_credits < 80:
                progression_outcome = "Module retriever"
                print(progression_outcome)
                retriever += 1
                retriever_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
            else:
                progression_outcome = "Exclude"
                print(progression_outcome)
                exclude += 1
                exclude_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])
            print("")
            if user == "2":  # Ending program if user is a student
                break
            yorqstate = True
            while yorqstate:  # Error handling loop for when y or q is not input in prompt
                try:
                    prostate = input("Would you like to enter another set of data?\n"
                                     "Enter 'y' for yes or 'q' to quit and view results: ").lower()
                    print("")
                    if prostate == "y" or prostate == "q":  # Break error handling loop when y or q is input
                        break
                    raise YorQ
                except YorQ:
                    print(end="")
            global ordered_progression_list
            ordered_progression_list = progress_list + trailer_list + retriever_list + exclude_list

        except ValueError:
            print("Integer required")
        except OutOfRange:
            print("Out of range")
        except TotalIncorrect:
            print("Total incorrect")
        if prostate == "q":
            break


def histogram(progress_no, trailer_no, retriever_no, exclude_no):
    total_no_entries = progress + trailer + retriever + exclude
    try:
        win = GraphWin('Histogram', 430, 320)
        win.setBackground('#edf2ec')
        # Title
        histogram_label = Text(Point(115, 15), 'Histogram Results')
        histogram_label.draw(win)
        histogram_label.setSize(13)
        histogram_label.setTextColor('#676767')
        histogram_label.setStyle('bold')
        # Bar rectangle - Progress
        progress_graph = Rectangle(Point(45, 265), Point(125, 265 - (progress_no * 10)))
        progress_graph.draw(win)
        progress_graph.setFill('#aef8a1')
        progress_graph.setOutline('#9da59a')
        # Bar rectangle - Trailer
        trailer_graph = Rectangle(Point(130, 265), Point(210, 265 - (trailer_no * 10)))
        trailer_graph.draw(win)
        trailer_graph.setFill('#a0c689')
        trailer_graph.setOutline('#9da59a')
        # Bar rectangle - Retriever
        retriever_graph = Rectangle(Point(215, 265), Point(295, 265 - (retriever_no * 10)))
        retriever_graph.draw(win)
        retriever_graph.setFill('#a7bc77')
        retriever_graph.setOutline('#9da59a')
        # Bar rectangle - Exclude
        exclude_graph = Rectangle(Point(300, 265), Point(380, 265 - (exclude_no * 10)))
        exclude_graph.draw(win)
        exclude_graph.setFill('#d2b6b5')
        exclude_graph.setOutline('#9da59a')
        # Label of No of progress above the progress-bar on graph
        progress_no_label = Text(Point(85, 255 - (progress_no * 10)), progress_no)
        progress_no_label.draw(win)
        progress_no_label.setSize(13)
        progress_no_label.setTextColor('#7e8a97')
        progress_no_label.setStyle('bold')
        # Label of No of trailer above the trailer-bar on graph
        trailer_no_label = Text(Point(170, 255 - (trailer_no * 10)), trailer_no)
        trailer_no_label.draw(win)
        trailer_no_label.setSize(13)
        trailer_no_label.setTextColor('#7e8a97')
        trailer_no_label.setStyle('bold')
        # Label of No of retriever above the retriever-bar on graph
        retriever_no_label = Text(Point(255, 255 - (retriever_no * 10)), retriever_no)
        retriever_no_label.draw(win)
        retriever_no_label.setSize(13)
        retriever_no_label.setTextColor('#7e8a97')
        retriever_no_label.setStyle('bold')
        # Label of No of exclude above the exclude-bar on graph
        exclude_no_label = Text(Point(340, 255 - (exclude_no * 10)), exclude_no)
        exclude_no_label.draw(win)
        exclude_no_label.setSize(13)
        exclude_no_label.setTextColor('#7e8a97')
        exclude_no_label.setStyle('bold')
        # Bottom 0 line
        bottom_line = Line(Point(20, 266), Point(410, 266))
        bottom_line.draw(win)
        bottom_line.setWidth(2)
        bottom_line.setFill('#9da59a')
        # X axis label progress
        progress_label = Text(Point(85, 278), 'Progress')
        progress_label.draw(win)
        progress_label.setSize(10)
        progress_label.setTextColor('#7e8a97')
        progress_label.setStyle('bold')
        # X axis label trailer
        trailer_label = Text(Point(170, 278), 'Trailer')
        trailer_label.draw(win)
        trailer_label.setSize(10)
        trailer_label.setTextColor('#7e8a97')
        trailer_label.setStyle('bold')
        # X axis label retriever
        retriever_label = Text(Point(255, 278), 'Retriever')
        retriever_label.draw(win)
        retriever_label.setSize(10)
        retriever_label.setTextColor('#7e8a97')
        retriever_label.setStyle('bold')
        # X axis label exclude
        exclude_label = Text(Point(340, 278), 'Excluded')
        exclude_label.draw(win)
        exclude_label.setSize(10)
        exclude_label.setTextColor('#7e8a97')
        exclude_label.setStyle('bold')
        # Total no of entries label
        total_entry_no_label = Text(Point(133, 298), f'{total_no_entries} outcomes in total.')
        total_entry_no_label.draw(win)
        total_entry_no_label.setSize(13)
        total_entry_no_label.setTextColor('#7e8a97')
        total_entry_no_label.setStyle('bold')

        win.getMouse()
        win.close()

    except GraphicsError:
        """When the cross is clicked and the exception occurs"""


def print_filtered_progression():
    print("Part 2:")
    for i in range(len(ordered_progression_list)):
        print(f"{ordered_progression_list[i][0]} - {ordered_progression_list[i][1]}, "
              f"{ordered_progression_list[i][2]}, {ordered_progression_list[i][3]}")


def write_to_file():
    f = open('progression.txt', 'wt')
    f.write("Part 3:\n")
    for i in range(len(ordered_progression_list)):
        f.write(f"{ordered_progression_list[i][0]} - {ordered_progression_list[i][1]}, "
                f"{ordered_progression_list[i][2]}, {ordered_progression_list[i][3]}\n")
    f.close()
    print()


def read_from_file():
    f = open('progression.txt', 'rt')
    for line in f:
        print(line, end="")
    f.close()


class OutOfRange(Exception):
    """Raised when credits entered are not in the range 0, 20, 40, 60, 80,100 and 120"""
    pass


class TotalIncorrect(Exception):
    """Raised when the total of the pass, defer and fail credits is not 120."""
    pass


class YorQ(Exception):
    """Raised when y or q is not entered when exiting or continuing"""
    pass


class IncorrectUser(Exception):
    """Raised when 1 or 2 is not entered when prompted for user"""
    pass


class IncorrectOutputType(Exception):
    """Raised when 1 or 2 or 3 is not entered when prompted for output_type"""
    pass


progression()
if user == "1":     # Staff outputs
    if output_type == "1":  # Part 1 output
        histogram(progress, trailer, retriever, exclude)
    if output_type == "2":  # Part 2 output
        print_filtered_progression()
    if output_type == "3":  # Part 3 output
        write_to_file()
        read_from_file()
