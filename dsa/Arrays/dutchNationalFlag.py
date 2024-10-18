import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles
readFiles = readFiles()

#writing None to the output file
readFiles.write_output(mode = 'w')

#getting the input
input_data = readFiles.read_input()

# sort an array containing 0,1,2 without using the sorting algorithm.
# function

def dutchFlag(input:list):

    start = 0
    last = len(input)-1
    mid = 0

    while mid <=last:
        if input[mid]==0:
            input[start],input[mid]=input[mid],input[start]
            start +=1
            mid+=1
        elif input[mid]==1:
            mid+=1
        else:
            input[last],input[mid] = input[mid],input[last]
            last -=1



    return input
    


for i in range(len(input_data)):
    
    current_input = input_data[i].strip().split(",")
    
    current_input = [int(x) for  x in current_input]
    output_data = dutchFlag(current_input)
    print(output_data)
    # output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=str(output_data)+"\n",mode = 'a')