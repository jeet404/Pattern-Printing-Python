# Simple pyramid pattern

def drawP(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

n = input("Enter Number : ")
drawP(int(n))
print("Process Over")


# *
# * *
# * * *
# * * * *
# * * * * *