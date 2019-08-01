#! /usr/bin/python3

'''
    Created a connect four game to be played in the terminal. To represent
    the red and yellow markers, R is used to represent red, and Y represents
    yellow. 
'''

class ConnectFourBoard():
    def __init__ (self):
        self.GameBoard = [' '] * 16;

    def PrintGameBoard(self):
        print(self.GameBoard[0] +"|"+ self.GameBoard[1] +"|"+ self.GameBoard[2] +"|"+ self.GameBoard[3] +"\n"
        +"-------"+"\n"+
        self.GameBoard[4] +"|"+ self.GameBoard[5] +"|"+ self.GameBoard[6] +"|"+ self.GameBoard[7] +"\n"
        +"-------"+"\n"+
        self.GameBoard[8] +"|"+ self.GameBoard[9] +"|"+ self.GameBoard[10] +"|"+ self.GameBoard[11] +"\n"
        +"-------"+"\n"+
        self.GameBoard[12] +"|"+ self.GameBoard[13] +"|"+ self.GameBoard[14] +"|"+ self.GameBoard[15] +"\n")

    #Checks if player's selected position on board is empty before placing marker
    def IsPositionEmpty(self,position):
        return self.GameBoard[position] == " "

    #Ask for player's position input, then checks if position is open, and assigns marker
    def MakeMove(self, PlayerName, PlayerMarker):
        BoardPosition = int(input(f"{PlayerName} select position to drop marker (0 - 15): "))
        while not self.IsPositionEmpty(BoardPosition):
            BoardPosition = int(input(f"{PlayerName} select position to drop marker (0 - 15): "))
        self.GameBoard[BoardPosition] = PlayerMarker

    def WinnerCheck(self, PlayerMarker):
        #Verticals
        if (self.GameBoard[0] == self.GameBoard[4] == self.GameBoard[8] == self.GameBoard[12] == PlayerMarker) or (self.GameBoard[1] == self.GameBoard[5] == self.GameBoard[9] == self.GameBoard[13] == PlayerMarker) or (self.GameBoard[2] == self.GameBoard[6] == self.GameBoard[10] == self.GameBoard[14] == PlayerMarker) or (self.GameBoard[3] == self.GameBoard[7] == self.GameBoard[11] == self.GameBoard[15] == PlayerMarker):
            return True
        #Horizontals
        elif (self.GameBoard[0] == self.GameBoard[1] == self.GameBoard[2] == self.GameBoard[3] == PlayerMarker) or (self.GameBoard[4] == self.GameBoard[5] == self.GameBoard[6] == self.GameBoard[7] == PlayerMarker) or (self.GameBoard[8] == self.GameBoard[9] == self.GameBoard[10] == self.GameBoard[11] == PlayerMarker) or (self.GameBoard[12] == self.GameBoard[13] == self.GameBoard[14] == self.GameBoard[15] == PlayerMarker):
            return True
        #Diagonals
        elif (self.GameBoard[0] == self.GameBoard[5] == self.GameBoard[10] == self.GameBoard[15] == PlayerMarker) or (self.GameBoard[3] == self.GameBoard[6] == self.GameBoard[9] == self.GameBoard[12] == PlayerMarker):
            return True
        else:
            return False

    def FullBoardDraw(self):
        for i in range(0, 15):
            if self.IsPositionEmpty(i):
                return False
        return True

class Players():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def RetrievePlayerName(self):
        return self.name

    def RetrievePlayerMarker(self):
        return self.marker

def ConnectFourGame():
    while True:
        print ("Connect Four Game")

        GameBoard = ConnectFourBoard()

        Player1 = Players(name=input("Enter player 1's name: "), marker="R");
        Player2 = Players(name=input("Enter player 2's name: "), marker="Y");

        GameOn = True
        while GameOn:
            GameBoard.MakeMove(Player1.RetrievePlayerName(), Player1.RetrievePlayerMarker())

            GameBoard.PrintGameBoard()

            if GameBoard.WinnerCheck(Player1.RetrievePlayerMarker()) == True:
                GameOn = False
                print(f"{Player1.RetrievePlayerName()} won!")
                break
            elif GameBoard.FullBoardDraw():
                GameOn = False
                print("Draw!")
                break

            GameBoard.MakeMove(Player2.RetrievePlayerName(), Player2.RetrievePlayerMarker())

            GameBoard.PrintGameBoard()

            if GameBoard.WinnerCheck(Player2.RetrievePlayerMarker()) == True:
                GameOn = False
                print(f"{Player2.RetrievePlayerName()} won!")
                break
            elif GameBoard.FullBoardDraw():
                GameOn = False
                print("Draw!")
                break

        if input("Play again (Y/N): ") != 'Y':
            break

if __name__ == "__main__":
    ConnectFourGame()
