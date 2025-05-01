def bubble_sort(arr):

    for i in range(len(arr)):
        #loop for iterations :
        for j in range(len(arr)-i-1):
            # loop for comparisions and swapping
            swapped = False
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = swap_nums(arr[j],arr[j+1])
                swapped = True
            
        if not swapped:
                print("Iteration:",i)
                # if there is no swapping, then the arrays are already sorted.
                break    

    return arr

swap_nums = lambda x, y: (y, x)

if __name__ == "__main__":
    # Read input from IP_OP/input.txt
    with open("IP_OP/input.txt", "r") as input_file:
        lines = input_file.read().splitlines()

    results = []
    for line in lines:
        try:
            # Convert the line to a list (e.g., "[1, 2, 3]" -> [1, 2, 3])
            array = eval(line)
            sorted_array = bubble_sort(array)
            results.append(str(sorted_array))
        except Exception as e:
            results.append(f"Error: {e}")

    # Write output to IP_OP/output.txt
    with open("IP_OP/output.txt", "w") as output_file:
        output_file.write("\n".join(results))






