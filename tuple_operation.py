numbers = tuple(map(int, input("Enter integers separated by space: ").split()))
print("Total number of items in tuple:", len(numbers))
if len(numbers) > 0:
    print("Last item in tuple:", numbers[-1])
else:
    print("Tuple is empty")
print("Tuple in reverse order:", numbers[::-1])
if 5 in numbers:
    print("Yes, 5 is present in the tuple")
else:
    print("No, 5 is not present in the tuple")
if len(numbers) > 2:
    new_tuple = tuple(sorted(numbers[1:-1]))
    print("Sorted tuple after removing first and last elements:", new_tuple)
else:
    print("Not enough elements to remove first and last")