import requests
import sys

# This Function is used to print the help message to the screen.
# It will be executed if the the user used -h option or if there is an error in the arguments.
def printHelp():
    helpMsg="""
        Developed by AbdulRhman Alfaifi
        --------------------------------
        Usage : ./commentRetriever.py [options] website
        Example: ./commentRetriever.py www.google.com
        --------------------------------
        Options:
        --------------------------------
        -oX                Output XML formatted output.
        -w [FILE]                 Write the results to a file.
        -h                 Print this message.
        --------------------------------
        Contacts:
        --------------------------------
        Twitter            @A__ALFAIFI
        E-mail             a.alfaifi.14@gmail.com
    """
    print(helpMsg)
    return

# this function is responsable in outputting the results stored in commentList.
def printComments():
    results=""
    if len(commentList) == 0:
        print("\x1b[31m--------------------\x1b[0m")
        print("\x1b[33m0 Comments Found.\x1b[0m")
        print("\x1b[31m--------------------\x1b[0m")
        return
    else:
        print("\x1b[31m--------------------\x1b[0m")
        print("\x1b[32m "+str(len(commentList))+" Comments Found.\x1b[0m")
        print("\x1b[31m--------------------\x1b[0m")
    # If the user used -oX option the result will be printed in XML format.
    if isXML:
        results= results+"<comments>\n"
        for index,comment in enumerate(commentList):
            results = results +"\t<comment id='" + str(index) + "'>\n"
            results = results +"\t\t"+comment[4:-3]+"\n"
            results = results +"\t</comment>\n"
        results = results +"</comments>\n"
    # Else the result will be printed in plain text.
    else:
        for comment in commentList:
            results = results +"\x1b[31m-\x1b[0m" * 20+"\n"  # \xb1[31m - RED    \xb1[0 - reset
            results = results +comment[4:-3]+"\n"
        results = results +"\x1b[31m-\x1b[0m" * 20+"\n"
    # If the user did not use the option -w the result will be printed to the screen.
    if writeToFile == False:
        print(results)
    # Else print the results to the file spicified by the user.
    else:
        file = open(saveToFile,"w")
        results = results.replace("\x1b[31m","").replace("\x1b[0m","")
        file.write(results)
        print("Results Saved To : "+saveToFile)
        print("\x1b[31m--------------------\x1b[0m")
    return

# Some varibales to save user options and the comments read from the webpage.
commentList = []
isXML = False
writeToFile = False
saveToFile = ""
website = ""

# This pice of code will read the argument and save them to above varibales for later use.
try:
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "-oX":
            isXML = True
        elif sys.argv[i] == "-w":
            writeToFile = True
            saveToFile = sys.argv[i+1]
            i+=1
        elif sys.argv[i] == "-h":
            printHelp()
            exit()
        elif sys.argv[i-1] != "-w":
            website = sys.argv[i]
            break
except IndexError:
    printHelp()
    exit()

# Check if the user did not spicifiy a website then call printHelp(). << Print the help message.
if len(website) == 0:
    printHelp()
    exit()
else:
    # Send a request to the webpage spicified by the user
    # then save the response to the varibale called response.
    response = requests.get("http://"+website).text
    # Go through all the comments one by one then save them to the list called commentList.
    while len(response) != 0:
        if(response.find("<!--") > 0):
            commentList.append(response[response.index("<!--"):response.index("-->")+3])
            response = response[response.index("-->")+2::]
        # When there is no more comments exit from the loop.
        else:
            break
    # call printComments() to output the results.
    printComments()
