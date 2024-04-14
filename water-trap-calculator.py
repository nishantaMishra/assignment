def zero_counter(array):
    array = list(map(int, array.split(',')))

    total_zeroes = 0

    # reducing non-zero elements until all elements become zero
    while True:
        # Count and remove leading zeroes
        leading_zeroes = 0
        while array and array[0] == 0:
            array.pop(0)
            leading_zeroes += 1
        
        # Count and remove trailing zeroes
        trailing_zeroes = 0
        while array and array[-1] == 0:
            array.pop()
            trailing_zeroes += 1
        
        # Print the reduced array
        #print("Reduced array:", array)

        # Count the number of zeroes in the array
        zeroes_count = array.count(0)
        #print("Number of zeroes in array:", zeroes_count)

        # append total_zeroes
        total_zeroes += zeroes_count

        if not array:
            break

        # Reduce non-zero elements by one
        array = [max(0, x - 1) for x in array]
        #print("Reduced array:", array)

    return total_zeroes

array_input = input("Enter the elevation map: ")

total_zeroes = zero_counter(array_input)

print(f"Water trapped is: {total_zeroes} units" )

#to better understand how code works. Uncomment all the print statements.

