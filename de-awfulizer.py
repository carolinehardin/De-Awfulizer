#Final for CSCI 141 Western Washington University
#Created colaboratively by 97 students in 2 hours under the direction of Dr. Hardin
#June 8 2020
#Original: http://eponis.tumblr.com/post/113798088670/everything-is-awful-and-im-not-okay-questions-to Copyright Sinope (eponis.tumblr.com), 2015.
#This work is licensed under a Creative Commons Attribution 4.0 International License.

import random, turtle, csv


    
#a place to save the last art generation string
LAST_ART = ""

#the topic keywords
topickey = ['hydrated', 'food', 'shower', 'clothes','sleep', 'stretch', 'nice', 'music',
              'cuddle', 'getitdone', 'selfie',  'plan','therapist', 'recover','meds',  'wait']  # line 5 write topic key
    
#the log status file
eq_file = "log_status.csv"

#press 1
def random_advice():
    """
        prints a random piece of advice formatted based on input
        precondition: import random for it to work
        postcondition: you get advice formatted for you
    """

    #randomly selects the advice
    rand = random.choice(setadvice())
   
    print(rand)
  

#press 2
def log_status():
    """ Function to a ask user selfcare questions and get yes
        or no answer.
        Pre-conditions: file with questions
        Post-conditions: answers in a comma sperated file
    """
    log_status_ans = open('log_status.csv', 'a')
    #list for questions
    question_list = ["Are you hydrated? ", "Have you eaten in the past three hours? ",
                     "Have you showered in the past day? ", "If daytime: are you dressed? ",
                     "If nighttime: are you sleepy and fatigued but resisting going to sleep? ",
                     "Have you stretched your legs in the past day? ",
                     "Have you said something nice to someone in the past day? ",
                     "Have you moved your body to music in the past day? ",
                     "Have you cuddled a living being in the past two days? ",
                     "Do you feel ineffective? ", "Do you feel unattractive? ",
                     "Do you feel paralyzed by indecision? ", "Have you seen a therapist in the past few days? ",
                     "Have you been over-exerting yourself lately — physically, emotionally, socially, or intellectually? ",
                     "Have you changed any of your medications in the past couple of weeks, including skipped doses or a change in generic prescription brandHave you waited a week? "]
    
    #loop to ask questions and store in answer_list
    print("Let's log your self-care status. Answer these questions with 'y' for yes or 'n' for no.")
    for i in range(len(question_list)):
        answer = input(question_list[i]).lower()
        
        #while loop for if they enter wrong input
        while answer != "n" and answer != "y":
            print("Your answer was not valid. Please, try again!")
            answer = input(question_list[i]).lower()
        
        #stops before question 16 to fix appropriate commas
        if i<len(questionlist)-1:
            log_status_ans.write(answer + ", ")
        else:
            log_status_ans.write(answer)
    
    log_status_ans.write('\n')
    #close file
    log_status_ans.close()
    return None
            
#press 3
def readLogStatus():
    """
    This function is supposed to read in a csv.file and return a list of dictionaries.
    Preconditions: csv module is imported, the csv is opened using "open('name.csv', 'r')"
    Postconditions: the csv.file is available to have all lines called
    Return: a list of dictionaries made up from the users responses

    """
    logStatus = [] #make empty list of which we will put in dictionaries
    status_log = open(eq_file, 'r')
    
    for row in status_log: #iterate for each line in the csv file
        newrow = row.strip()
        newrow = newrow.split(',') #take out "\n"
        
        row_dict = {}
        if len(newrow) == len(topickey): #don't append incomplete rows
            for i in range(len(topickey)):
                row_dict[topickey[i]] = newrow[i]
                
            logStatus.append(row_dict) #add each line into the list
                                     
            
    status_log.close()
    return logStatus #return the list made up of dictionaries

#press 4 
def countYes():
    """Calculate which item has the fewest "yes" answers, and return that item.
    Breaks ties by selecting the first key with the lowest amount of .
    Precondition: Needs a list of dicts with the correct keys and values.
    Postcondition: Return the item with fewest yes answers."""
    
    # Block sets answer varibles to zero
    hydrateCount = 0
    foodCount = 0
    showerCount = 0
    stretchCount = 0
    niceCount = 0
    musicCount = 0
    cuddleCount = 0
    therapistCount = 0
    medsCount = 0
    clothesCount = 0
    sleepCount = 0
    getitdoneCount = 0
    selfieCount = 0
    planCount = 0
    recoverCount = 0
    waitCount = 0
    
    log = readLogStatus()

    # Loops throught the dictonary, checking the response.
    for x in log:
        # Checks to see if the Key is "yes"
        if x["hydrated"] == "y":
            # Adds 1 to the Varible
            hydrateCount += 1
        if x["food"] == "y":
            foodCount += 1
        if x["shower"] == "y":
            showerCount += 1
        if x["stretch"] == "y":
            stretchCount += 1
        if x["nice"] == "y":
            niceCount += 1
        if x["music"] == "y":
            musicCount += 1
        if x["cuddle"] == "y":
            cuddleCount += 1
        if x["therapist"] == "y":
            therapistCount += 1
        if x["meds"] == "y":
            medsCount += 1
        if x["clothes"] == "y":
            clothesCount += 1
        if x["sleep"] == "y":
            sleepCount += 1
        if x["getitdone"] == "y":
            getitdoneCount += 1
        if x["selfie"] == "y":
            selfieCount += 1
        if x["plan"] == "y":
            planCount += 1
        if x["recover"] == "y":
            recoverCount += 1
        if x["wait"] == "y":
            waitCount += 1
            
            
    # Creates a dict that contains all the yes counts
    count_list = {"hydrated": hydrateCount, "food": foodCount, "shower": showerCount,
        "stretch": stretchCount, "nice": niceCount, "music": musicCount, "cuddle": cuddleCount,
        "therapist": therapistCount, "meds": medsCount, "clothes": clothesCount, "sleep": sleepCount, "getitdone": getitdoneCount,
        "selfie": selfieCount, "plan": planCount, "recover": recoverCount, "wait": waitCount}
   
   # Sets the lowest yes counted item to a varible.
    lowest_yes = (min(count_list, key = count_list.get))
    print("According to the log, the item you're likely to need to attend to is:")
    print(lowest_yes)



def setadvice(): #fills given list with advice
    advice = []
    
    #these are used by predicted and ranom advice
    advice.append('Have a glass of water.')
    advice.append('Get some food — something with protein, not just simple carbs.  Perhaps some nuts or hummus?')
    advice.append('Take a shower right now.')
    advice.append('Put on clean clothes that aren’t pajamas.  Give yourself permission to wear something special, whether it’s a funny t-shirt or a pretty dress.')
    advice.append('Get some sleep. Put on pajamas, make yourself cozy in bed with a teddy bear and the sound of falling rain, and close your eyes for fifteen minutes — no electronic screens allowed.  If you’re still awake after that, you can get up again; no pressure.')
    advice.append('Get some exercise. If you don’t have the spoons for a run or trip to the gym, just walk around the block, then keep walking as long as you please.  If the weather’s crap, drive to a big box store (e.g. Target) and go on a brisk walk through the aisles you normally skip.')
    advice.append('Compliment someone, whether online or in person.  Make it genuine; wait until you see something really wonderful about someone, and tell them about it.')
    advice.append('Jog for the length of an EDM song at your favorite BPM, or just dance around the room for the length of an upbeat song.')
    advice.append('Don’t be afraid to ask for hugs from friends in your quarentine bubble, or from friends (while wearing masks), or friends’ pets.  Most of them will enjoy the cuddles too; you’re not imposing on them.')
    advice.append('Pause right now and get something small completed, whether it’s responding to an e-mail, loading up the dishwasher, or packing your gym bag for your next trip.  Good job!')
    advice.append('Take a goddamn selfie.  Your friends will remind you how great you look, and you’ll fight society’s restrictions on what beauty can look like.')
    advice.append('Give yourself ten minutes to sit back and figure out a game plan for the day.  If a particular decision or problem is still being a roadblock, simply set it aside for now, and pick something else that seems doable.  Right now, the important part is to break through that stasis, even if it means doing something trivial.')
    advice.append('Hang on until your next therapy visit and talk through things then.')
    advice.append('Overexerting yourself can take a toll that lingers for days. Give yourself a break in that area, whether it’s physical rest, taking time alone, or relaxing with some silly entertainment.')
    advice.append('New meds may be screwing with your head.  Give things a few days, then talk to your doctor if it doesn’t settle down.')
    advice.append('Sometimes our perception of life is skewed, and we can’t even tell that we’re not thinking clearly, and there’s no obvious external cause.  It happens.  Keep yourself going for a full week, whatever it takes, and see if you still feel the same way then.')
    
    #these are used by random advice
    advice.append("Do 25 jumping jacks.  Help circulate your blood!")
    advice.append("Drink some water.  This will help keep you hydrated!")
    advice.append("Get some fresh air.  It's good for you!")
    advice.append("Talk to a friend.  Reach out for help!")
    advice.append("Get some good sleep.  8 hours is recommended!")
    advice.append("Take a walk, even just around the block.")
    advice.append("Naps are ok! Put some quiet music on, or a meditation podcast, and lay down for 20 minutes.")
    advice.append("Put on some music you like, and clean an area of your house. It'll give you some satisfaction and make things more pleasant.")
    
    return advice


def real(issue, topickey):
    """ real(issue) setting the if, elif, else (28-34)
        prints out given advice for topic specified
        precon:non
        postcon:advice is given
      """
    newli = setadvice()[topickey.index(issue)].split('.')
    for i in range(len(newli)):
        print(newli[i])
    


def mainsix():#if and else statments regarding topic keys (38)
    """ if and else statments regarding topic keys (38)
        precon:non
        postcon:passes problem to real
      """
    print("I can help you with:", topickey)
    problem = input('what would you like advice on?') #input "what would you like advice on?"(27)

    if problem in topickey:
        real(problem, topickey) # real(issue) setting the if, elif, else (28-34)

    else:
        print('please input a correct choice')
        print(topickey)
        mainsix()

   


#press 7
def log_good_memory():
    """
    Ask user for a good memory or something they are greatful for.
    Then write the users response to a file called log_good.txt.
    If this file already contains information, add the input on a new line of the file.
    Post condition: the users input is the last line in the log_good.txt file
    """
    #get user input
    user_input = input("What is a good memory or something that you are greatful for?")

    #if user does not enter anything tell them and ask same question again
    while user_input == "":
        print("Invalid input.")
        user_input = input("What is a good memory or something that you are greatful for?")
    
    #open file log_good.txt
    file = open("log_good.txt", 'a')
    
    #create variable to check if file is empty
    check_file = open("log_good.txt", 'r')
    
    #if file is empty print user input on first line
    if check_file.read() == "":
        #add user input to the end of log_good.txt
        file.write(user_input)
    #if file is not empty print user input on line below last line
    else:
        file.write("\n" + user_input)

    #close file
    file.close()
    print("Memory logged!")

#press 7
def good_memory():
    """
    Remind the user of a random good memory
    
    preconditions: User enters in 8 for the main prompt. File must be named log_good.txt
    
    postconditions: Returns random line from the text
    """

    file = open("log_good.txt", "r")
    memories = []
    #Strips each line and stores it in memories list
    for line in file:
        split = line.split(",")
        strip = line.strip("\n")
        memories.append(strip)
    # If the list is not empty, pick random line
    if len(memories) > 0:
        print(random.choice(memories))
    else:
        print("No memories yet logged. Record one from the main menu.")
    
    file.close()
    return memories

    

#press 8
def move_direction(t, direction):
    """ moves turtle t 100 units in its current facing direction with a random color
        PRE: t is a turtle, colormode is 255, direction is a string in ['w', 's', 'a', 'd']
    """
    t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.forward(100)
    return direction

def make_art():
    """ Function lets user use WASD to move a turtle to create
        a drawing with random colors and prints out a comma separated string
        of direction history after they are done.
        PRE: t is a turtle in colormode 255 (turtle.colormode(255))
        POST: returns comma separated string of direction history
    """
    import turtle
    import random
    
    # define direction and direction string before they are used
    dir_str = ''
    direction = 0
    prompt="Press 'w' to move up, 's' to move down, 'a' to move left, 'd' to move right, or 'f' to finish."
    
    # define turtle 't' and assign it 255 RGB colormode
    t = turtle.Turtle()
    turtle.colormode(255)
    # while the user does not press 'q', keep going
    while direction != "f":
        print(prompt)
        direction = input()
    
        t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # use if statements to move the turtle in the specified direction
        if direction == 'w':
            # move north
            t.seth(90)
            # choose a random color
           
            t.forward(100)
            dir_str += 'w,'

        elif direction == 's':
            # move south
            t.seth(270)
            
            t.forward(100)
            dir_str += 's,'
            
        elif direction == 'a':
            # move west
            t.seth(180)
            
            t.forward(100)
            dir_str += 'a,'
            
        elif direction == 'd':
            # move east
            t.seth(0)
         
            t.forward(100)
            dir_str += 'd,'

    dir_str += 'f'
    print(dir_str)
    return dir_str

#press 9
def share_art():
    """runs the code for part ten, no parameters or return values"""


    #asks for input, stores in put in user_input_ten.
    user_input_ten=input("Type 'Save' to save the last thing you drew, or 'Load' to load. ")
    if user_input_ten.lower()=="save":#if user enters save,writes the output of share_art in draw.csv.
        
        if len(LAST_ART) == 0: #this will be zero if they haven't made any art yet
            print("You haven't drawn anything yet. Let's make some art!")
            draw_string=make_art()
           
        else:
            draw_string=LAST_ART
        
        saveToDraw=open("draw.csv","w")
        saveToDraw.write(draw_string)
        saveToDraw.close()
        print("Your art has been saved to a file draw.csv. Share it with a friend!")
        
    elif user_input_ten.lower()=="load":#if user enters load,reads line zero of draw.csv and makes it into a list of directions.  
        t=turtle.Turtle()
        readToDraw=open("draw.csv","r")
        draw_string=readToDraw.readlines()[0]
        draw_list=draw_string.split(",")#splits the text in draw_string by commas.
        for i in range(len(draw_list)):#for every value in the number of values in draw_list plus one. 
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if draw_list[i]=="w":#movements for turtle with values w,a,d,s,q in draw_list.
                t.setheading(90)
                t.forward(100)
            elif draw_list[i]=="a":
                t.setheading(180)
                t.forward(100)
            elif draw_list[i]=="d":
                t.setheading(0)
                t.forward(100)
            elif draw_list[i]=="s":
                t.setheading(270)
                t.forward(100)
            elif draw_list[i]=="f":
              
                print("Done drawing!")
        readToDraw.close()#closes readTodraw file after turtle is done. 
        
            


def main():
    """Prompts user for a numerical input 0-9 from user menu, if 0 is entered
    program exits
    Pre: functions must be defined to input in list
         User input must be an integer or program will crash
    Post: function runs repeatedly until user enters 0
    No returns"""
    
    #define list of tasks
    tasks = ["", "Random Advice", "Log Status", "Predict Topic", "Targeted Advice", "Log Good Memory", "Remind Good Memory", "Make Art", "Share Art"]
   
   #list of functions to call 
    functions = ["", random_advice, log_status, countYes, mainsix, log_good_memory, good_memory, make_art, share_art]
    
          
    while True:
        #for loop to print menu options
        for i in range(len(tasks)):
            if i > 0:
                print("Enter", i, "for", tasks[i])
            i += 1
        print("Enter 0 to exit")
        action = int(input())
        
        
        #if user enters 0
        if action == 0:
            exit()
        #if invalid input
        elif action > len(tasks)-1 or action < 0:
            print("Invalid option")
        elif action == 7: #make art
            LAST_ART = functions[action]()
       
        #if valid input
        elif action > 0:
            functions[action]()
        
        input("(Hit enter to continue)")
        print()
        
main()