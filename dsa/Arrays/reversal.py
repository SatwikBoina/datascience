import os

inputPath = os.path.join(os.getcwd(),"dsa/input.txt")
outputPath = os.path.join(os.getcwd(),"dsa/output.txt")

with open(inputPath, "r") as infile:
    input_data = infile.readlines()
print(len(input_data))


def arrayReversal(input_data : list):
    
    first = 0
    last = len(input_data)-1
    while first < last : 
        temp = input_data[first]
        input_data[first] = input_data[last]
        input_data[last]=temp
        last -= 1
        first +=1
    return input_data


for i in range(len(input_data)):
    current_input = input_data[i].split(",")
    output_data = arrayReversal(current_input)
    print(output_data)

    with open(outputPath,'a') as outfile:
        outfile.writelines(", ".join(output_data)+"\n")
    
    




