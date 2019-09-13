#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm has a linear runtime complexity with O(n). The number of iterations increases in direct proportion to the number of elements passed as input. This is a result of how `n * n` expressions negate each other in the control flow.

```python
def algo1(n):
    a = 0
    count = 0

    while (a < n * n * n):
        a = a + n * n
        count += 1

    print(f"Count: {count}\n")

algo1(0)   #=> Count: 0
algo1(1)   #=> Count: 1
algo1(2)   #=> Count: 2
algo1(3)   #=> Count: 3
algo1(4)   #=> Count: 4
algo1(5)   #=> Count: 5
algo1(10)  #=> Count: 10
algo1(100) #=> Count: 100
```

b) This algorithm has a lineararithmic runtime complexity with O(n log n). Runtime complexity is shown to be between linear and polynomial.

```python
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

algo2(0)   #=> Count: 0
algo2(1)   #=> Count: 0
algo2(2)   #=> Count: 2
algo2(3)   #=> Count: 6
algo2(4)   #=> Count: 8
algo2(5)   #=> Count: 15
algo2(10)  #=> Count: 40
algo2(100) #=> Count: 700
```

c) This algorithm has a linear runtime complexity with O(n). Despite the actual runtime being n + 1 computers don't care much about adding one additional operation. Based on that we can remove the constant from the runtime complexity.

```python
def bunnyEars(bunnies, count):
    count += 1
    print(f"Count: {count}")
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1, count)

bunnyEars(1, 0)
#=> Count: 1
#=> Count: 2

bunnyEars(2, 0)
#=> Count: 1
#=> Count: 2
#=> Count: 3

bunnyEars(4, 0)
#=> Count: 1
#=> Count: 2
#=> Count: 3
#=> Count: 4

bunnyEars(5, 0)
#=> Count: 1
#=> Count: 2
#=> Count: 3
#=> ...
#=> Count: 6

bunnyEars(10, 0)
#=> Count: 1
#=> Count: 2
#=> Count: 3
#=> ...
#=> Count: 11

bunnyEars(100, 0)
#=> Count: 1
#=> Count: 2
#=> Count: 3
#=> ...
#=> Count: 101
```

## Exercise II


