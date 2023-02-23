"""
This progam will take 1 txt file and hopefully convert it into several csv files
while converting it should: 
    - change any '.' into '-1' and
    - put a ',' between all elements
    - convert any '0' into an unused higher number and then convert any 'r' into '0'  
the csv files should then be saved in the boards folder
"""
import csv

def read_file():
    board = []
    text = open("sample_output.txt", "r")
    csvCount =0
    for count in text:
        board.append(count)
        if count.__contains__(","):
            # end of board
            csvCount+=1
            board.append(count)
            make_file(board, csvCount)
            board.clear() 
            

    text.close

    return 


def make_file(linesBoard, boardId):
    # gets 1 board line by line processes and saves it
    completeBoard = []
    #print(linesBoard)
    boardSize = linesBoard.__sizeof__()
    boardSize = boardSize.__str__() + "x"+ boardSize.__str__()
    for count in linesBoard:
        completeBoard.append(process_file(count))
    print(completeBoard.__str__()+ "  P")
    with open("boards\\board"+boardSize+"_"+boardId.__str__()+".csv", "w") as csvFile:
        write = csv.writer(csvFile)
        write.writerows(completeBoard)
    #csvFile.write(completeBoard.__str__())
    csvFile.close()

    return

def process_file(unprocessedText):
    processed = []
    found = False
    max = 0
    while(found):
        if unprocessedText.contains(max.__str__()):
            max+=1
        else:
            found = True
    #print(unprocessedText.__str__()+ "U")
    for element in unprocessedText:
        if element == ".":
            processed.append( "-1")
        elif element == ',' or element == '\n':
            element = "" # dont add it to processed
        elif element == 'r':
            processed.append("0")
        elif element == '0':
            processed.append(max.__str__())
        else:
            processed.append(element)
    #print(processed.__str__()+ "  P")
    return processed


if __name__ == '__main__':
    # first open the txt file, read it and separate from the ',' while removing them 

    read_file()

    print("Done!")

