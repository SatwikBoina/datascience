import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles
readFiles = readFiles()

#writing None to the output file
readFiles.write_output(mode = 'w')

#getting the input
input_data = readFiles.read_input()

# function

def get_min_max(input:list):
    min = float("inf")
    max = float("-inf")

    for i in range(len(input)):

        if input[i]<min:
            min = input[i]
        elif input[i]>max:
            max = input[i]
    
    return min,max



for i in range(len(input_data)):
    
    current_input = input_data[i].strip().split(",")
    
    current_input = [int(x) for  x in current_input]
    output_data = get_min_max(current_input)
    print(output_data)
    # output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=str(output_data)+"\n",mode = 'a')