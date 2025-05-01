def selection_sort(arr):

    for i in range(len(arr)):
        #loop for iterations : identify the min value
        min_value_position = i
        for j in range(i+1,len(arr)):
            # loop for comparisions and swapping
            if arr[j]<arr[min_value_position]:
                min_value_position = j
                #arr[j],min_value = swap_nums(arr[j],min_value)
        arr[i],arr[min_value_position] = swap_nums(arr[i],arr[min_value_position])
        

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
            sorted_array = selection_sort(array)
            results.append(str(sorted_array))
        except Exception as e:
            results.append(f"Error: {e}")

    # Write output to IP_OP/output.txt
    with open("IP_OP/output.txt", "w") as output_file:
        output_file.write("\n".join(results))






