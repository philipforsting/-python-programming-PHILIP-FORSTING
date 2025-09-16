
# a) 
chessAlpha = list("ABCDEFGH")
chessRow = [chessAlpha[i]+"1" for i in range(len(chessAlpha))]
print(chessRow)

# b)

ChessBoard = [[chessAlpha[i]+str(j) for i in range(len(chessRow))] for j in range(1,9)] # inspiration for building a 2D-list taken from https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
print(ChessBoard) # List is printed without linebreaks,is it ok?


