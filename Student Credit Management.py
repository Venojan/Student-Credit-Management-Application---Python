
# Date : 11/18/2023

    
from graphics import* #import graphics  module or third party library


# define the funcion main
def main():
    results=[]
    # valid range of the credit
    vaild_range=[0,20,40,60,80,100,120]
    count={"Progress":0,"Progress (module trailer)":0,"Do not progress-module retriever":0,"Exclude":0}

    # open file in write mode 
    file=open("Marks.txt","w")

    
    while True: # the condition is true
        pass_credits=input("please enter your credits at pass : ")
        # if the input in number 
        try:
            pass_credits=int(pass_credits)
        # if the input not as an integer or i is string 
        except ValueError:
            print("Integer required",'\n')
            continue
        #if the number not in valid range
        if pass_credits not in vaild_range:
            print("Out of range",'\n')
            continue

        deffer_credits=input("please enter your credits at deffer : ")
        # if the input in number
        try:
            deffer_credits=int(deffer_credits)
        # if the input not as an integer or input is string 
        except ValueError:
            print("Integer required",'\n')
            continue
        #if the number not in valid range
        if deffer_credits not in vaild_range:
            print("Out of range",'\n')
            continue
    
        fail_credits=input("please enter your credits at fail : ")
        # if the input in number
        try:
            fail_credits=int(fail_credits)
        # if the input not as an integer or input is string 
        except ValueError:
            print("Integer required",'\n')
            continue
        #if the number not in valid range
        if fail_credits not in vaild_range:
            print("Out of range",'\n')
            continue

        Total=pass_credits+deffer_credits+fail_credits

        # if the total of inputs are incorrect
        if Total != 120:
            print("Total incorrect",'\n')
            continue

        # conditions for credis
        if pass_credits == 120:
            progression_outcome="Progress"
            
        elif pass_credits == 100:
            progression_outcome="Progress (module trailer)"
            
        elif 80 <= fail_credits and pass_credits <= 40 :
            progression_outcome="Exclude"
            
        else :
            progression_outcome="Do not progress-module retriever"
            

        print(progression_outcome,'\n')

        # add increased value to values in count
        count[progression_outcome]+=1


        # append the outcome and inputs into results
        results.append(progression_outcome) 
        results.append(pass_credits)
        results.append(deffer_credits)
        results.append(fail_credits)

        # write the user input into the file
        file.write(progression_outcome+'-')
        file.write(str(pass_credits)+' ')
        file.write(str(deffer_credits)+' ')
        file.write(str(fail_credits)+'\n')

        print("Would yuo like to enter another set of data ?")
        user=input("Enter 'y' for yes or 'q' to quit and view results : ")
        print()

        # if the user 
        if user.lower()=='q':
            
            # open graphis window
            win=GraphWin("Historgram ",750,600)
            win.setBackground("AliceBlue")

            # create a straight line
            straight=Line(Point(50,530),Point(700,530))
            straight.draw(win)

            # heading for histogram
            Heading=Text(Point(150,30),"Histogram Results")
            Heading.setStyle("bold")
            Heading.setSize(15)
            Heading.draw(win)

            # create rectangle for progress
            Progress=Rectangle(Point(100,530),Point(220,530-(count["Progress"]*10)))
            Progress.setFill("Pale Green")
            Progress.draw(win)
            # create lable for progress
            Progress_label=Text(Point(160,540),"Progress")
            Progress_label.draw(win)
            # display total number of progress
            Progress_count=Text(Point(160,530-(count["Progress"]*10)-10),count["Progress"])
            Progress_count.draw(win)
            
            # create rectangle for trailer
            Trailer=Rectangle(Point(240,530),Point(360,530-(count["Progress (module trailer)"]*10)))
            Trailer.setFill("Green")
            Trailer.draw(win)
            # create lable for trailer
            Trailer_label=Text(Point(300,540),"Trailer")
            Trailer_label.draw(win)
            # display total number of trailer
            Trailer_count=Text(Point(300,530-(count["Progress (module trailer)"]*10)-10),count["Progress (module trailer)"])
            Trailer_count.draw(win)
            
            # create rectangle for retriver
            Retriver=Rectangle(Point(380,530),Point(500,530-(count["Do not progress-module retriever"]*10)))
            Retriver.setFill("Yellowgreen")
            Retriver.draw(win)
            # create lable for retriver
            Retriver_label=Text(Point(440,540),"Retriever")
            Retriver_label.draw(win)
            Retriver_count=Text(Point(440,530-(count["Do not progress-module retriever"]*10)-10),count["Do not progress-module retriever"])
            Retriver_count.draw(win)
            
            # create rectangle for exclude
            Exclude=Rectangle(Point(520,530),Point(640,530-(count["Exclude"]*10)))
            Exclude.setFill("pink")
            Exclude.draw(win)
            # create lable for exclude
            Exclude_label=Text(Point(580,540),"Excluded")
            Exclude_label.draw(win)
            # display total number of exclude
            Exclude_count=Text(Point(580,530-(count["Exclude"]*10)-10),count["Exclude"])
            Exclude_count.draw(win)

            #diplay total number of outcome
            Total_results=Text(Point(150,565),f"{sum(count.values())} Outcome in total")
            Total_results.setSize(14)
            Total_results.draw(win)

            print("Part 2 : ",'\n')
            # get user inputs from results list
            for i in range(0,len(results),4):
                print(results[i],"-",results[i+1],results[i+2],results[i+3])
            # close the file
            file.close()
            print()
            print("Part 3 : ",'\n')
            # open file in read mode
            file=open("Marks.txt","r")
            # read data from the file
            data=file.readlines()
            for line in data:
                print(line)

            # close the file
            file.close()

            # wait for mouse click to view the histogram
            win.getMouse()

            # close the histogram window
            win.close()

            # break out of the loop
            break
        
# call the main function        
main()


    
    
