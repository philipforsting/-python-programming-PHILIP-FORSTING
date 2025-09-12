# In first square of the chessboard there is one grain of rice, in the second square there is two grains, 
# in the third square there is four grains and so on. How many grains are there in the whole chessboard when all squares are filled using this pattern?


sum = 0
squares = 64
for i in range(0, 64):
    sum += 2**i

print(f"{sum}")