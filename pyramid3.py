# Opposite pyramid pattern

def drawP(n):
    for i in range(n + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")

n = int(input("Enter Number : "))
drawP(n)
print("Process Over")

# * * * * *
# * * * *
# * * *
# * *
# *