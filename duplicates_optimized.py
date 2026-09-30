import time
import random


def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)

numbers = [random.randint(1, 5000) for _ in range(10000)]
start = time.perf_counter()
result = find_duplicates(numbers)
end = time.perf_counter()
print("Number of elements:", len(numbers))
print("Execution time:", end - start, "seconds")