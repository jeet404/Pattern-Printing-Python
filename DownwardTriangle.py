# Downward Triangle Pattern

def drawP(n):
    k = 2 * n - 2
    # Outer loop in reverse order
    for i in range(n, -1, -1):
        # Inner loop will print the number of space.
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        # This inner loop will print the number o stars
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")

n = int(input("Enter Number : "))
drawP(n)
print("Process Over")