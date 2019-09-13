#
# Define methods
#

def algo1(n):
    a = 0
    count = 0

    while (a < n * n * n):
        print(f"a:{a}, n:{n} - n * n * n {n * n * n}")
        a = a + n * n
        count += 1

    print(f"Count: {count}\n")

# 
# Execute methods
# 

if __name__ == '__main__':
    algo1(0)   #=> Count: 0
    algo1(1)   #=> Count: 1
    algo1(2)   #=> Count: 2
    algo1(3)   #=> Count: 3
    algo1(4)   #=> Count: 4
    algo1(5)   #=> Count: 5
    algo1(10)  #=> Count: 10
    algo1(100) #=> Count: 100
