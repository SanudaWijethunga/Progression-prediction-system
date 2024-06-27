# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052741
# Date: 10.12.2023

#import the grphics module
from graphics import *

#declare and initialize variables
total = 0
value = 0
all_inputs = []
progress_count = 0
module_trailer_count = 0
exclude_count = 0
module_retriever_count = 0

def user_input():
    "This function will get the values from the user"
    marks_range = [0,20,40,60,80,100,120]
    credit_range = ["PASS","DEFER","FAIL"]
    list_input = []
    for credit in credit_range:
        while True:
            try:
                value = int(input(f"Enter your total {credit} credits : "))
                if value in marks_range:
                    #append to the user input list
                    list_input.append(value)
                    break
                else:
                    print("Out of range\n")
            except:
                print("Integer required\n")
    return list_input

def displaying_histrogram(progress_count,module_trailer_count,exclude_count,module_retriever_count):
    "This function will create and display the histrogram"
    #create the window
    win = GraphWin("Histrogram",450,300)
    win.setBackground("white")
    border_line = Line(Point(40,240),Point(410,240))
    border_line.draw(win)
    top_text = Text(Point(80,30),"Histrogram results")
    top_text.draw(win)
    
    #calculate the total outcomes and display
    total_outcomes = (progress_count + module_trailer_count + exclude_count + module_retriever_count)
    total_outcomes_text = Text(Point(80,280),f"{total_outcomes} outcomes in total")
    total_outcomes_text.setSize(11)
    total_outcomes_text.draw(win)

    #create the bar for Progress
    rectangle_progress = Rectangle(Point(50,240),Point(100,240 - progress_count * 10))
    rectangle_progress.setFill("lightblue")
    rectangle_progress.draw(win)
    
    rectangle_progress_lable = Text(Point(75,250),"Progress")
    rectangle_progress_lable.setSize(10)
    rectangle_progress_lable.draw(win)
    
    rectangle_progress_total = Text(Point(75,(240 - progress_count * 10)-10),f"{progress_count}")
    rectangle_progress_total.setSize(10)
    rectangle_progress_total.draw(win)

    #create the bar for Trailer
    rectangle_trailer = Rectangle(Point(150,240),Point(200,240 - module_trailer_count * 10))
    rectangle_trailer.setFill("red")
    rectangle_trailer.draw(win)

    rectangle_trailer_lable = Text(Point(175,250),"Trailer")
    rectangle_trailer_lable.setSize(10)
    rectangle_trailer_lable.draw(win)

    rectangle_trailer_total = Text(Point(175,(240 - module_trailer_count * 10) - 10),f"{module_trailer_count}")
    rectangle_trailer_total.setSize(10)
    rectangle_trailer_total.draw(win)

    #create the bar for Module retiever
    rectangle_retriever = Rectangle(Point(250,240),Point(300,240 - module_retriever_count * 10))
    rectangle_retriever.setFill("pink")
    rectangle_retriever.draw(win)

    rectangle_retriever_lable = Text(Point(275,250),"Retriever")
    rectangle_retriever_lable.setSize(10)
    rectangle_retriever_lable.draw(win)

    rectangle_retriever_total = Text(Point(275,(240 - module_retriever_count * 10) - 10),f"{module_retriever_count}")
    rectangle_retriever_total.setSize(10)
    rectangle_retriever_total.draw(win)

    #create the bar for Exclude
    rectangle_exclude = Rectangle(Point(350,240),Point(400,240 - exclude_count * 10))
    rectangle_exclude.setFill("lightgreen")
    rectangle_exclude.draw(win)

    rectangle_exclude_lable = (Text(Point(375,250),"Exclude"))
    rectangle_exclude_lable.setSize(10)
    rectangle_exclude_lable.draw(win)

    rectangle_exclude_total = Text(Point(375,(240 - exclude_count * 10) - 10),f"{exclude_count}")
    rectangle_exclude_total.setSize(10)
    rectangle_exclude_total.draw(win)
    
    win.getMouse()
    win.close()
    
def again_or_not():
    "This function will take user idea for another set of data"
    print("would you like to enter another set of data ?")
    again_or_not = input("Enter 'y' for yes or 'q' to quit and view results: ")
    again_or_not = again_or_not.lower()
    print()
    return again_or_not

#main
while True:
    total = user_input()
    if sum(total) == 120:
        #display outcome and count the outcomes
        if total[0] == 120:
            print("Progress\n")
            all_inputs.append(f"Progress - {total[0]},{total[1]},{total[1]}")
            progress_count += 1    
        elif total[0] == 100:
            print("Progress(module trailer)\n")
            all_inputs.append(f"Progress(module trailer) - {total[0]},{total[1]},{total[2]}")
            module_trailer_count += 1   
        elif total[2] >= 80:
            print("Exclude\n")
            all_inputs.append(f"Exclude - {total[0]},{total[1]},{total[2]}")
            exclude_count += 1
        else:
            print("Do not progress - module retriever\n")
            all_inputs.append(f"Module retriever - {total[0]},{total[1]},{total[2]}")
            module_retriever_count += 1
    else:
        print("Total incorrect\n")
    #asking user want to enter another set of data 
    choice = again_or_not()
    if choice != 'y':
       break
    
#print the summary of all input data and write those to a text file
fo = 0
fo = open("Progression_outcomes.txt","w")
print("Part 2 :")
fo.write("Part 3 :\n")
for outcome in all_inputs: 
    print(outcome)
    fo.write(f"{outcome}\n")
fo.close()

#displaying the histrogram
displaying_histrogram(progress_count,module_trailer_count,exclude_count,module_retriever_count)
