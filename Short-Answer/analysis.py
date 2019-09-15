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

def algo2(n):
    total = 0
    count = 0

    for i in range(n):
        j = 1

        while j < n:
            j *= 2
            total += 1
            count += 1

    print(f"Count: {count}")

def bunnyEars(bunnies, count):
    count += 1
    print(f"Count: {count}")
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1, count)

# 
# Execute methods
# 

if __name__ == '__main__':
    # algo1(0)   #=> Count: 0
    # algo1(1)   #=> Count: 1
    # algo1(2)   #=> Count: 2
    # algo1(3)   #=> Count: 3
    # algo1(4)   #=> Count: 4
    # algo1(5)   #=> Count: 5
    # algo1(10)  #=> Count: 10
    # algo1(100) #=> Count: 100

    # algo2(0)   #=> Count: 0
    # algo2(1)   #=> Count: 0
    # algo2(2)   #=> Count: 2
    # algo2(3)   #=> Count: 6
    # algo2(4)   #=> Count: 8
    # algo2(5)   #=> Count: 15
    # algo2(10)  #=> Count: 40
    # algo2(100) #=> Count: 700

    # bunnyEars(1, 0)
    #=> Count: 1
    #=> Count: 2

    # bunnyEars(2, 0)
    #=> Count: 1
    #=> Count: 2
    #=> Count: 3

    # bunnyEars(4, 0)
    #=> Count: 1
    #=> Count: 2
    #=> Count: 3
    #=> Count: 4

    # bunnyEars(5, 0)
    #=> Count: 1
    #=> Count: 2
    #=> Count: 3
    #=> ...
    #=> Count: 6

    # bunnyEars(10, 0)
    #=> Count: 1
    #=> Count: 2
    #=> Count: 3
    #=> ...
    #=> Count: 11

    # bunnyEars(100, 0)
    #=> Count: 1
    #=> Count: 2
    #=> Count: 3
    #=> ...
    #=> Count: 101
