import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles

readFiles = readFiles()




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

input_data = readFiles.read_input()

#writing None to the output file
readFiles.write_output(mode = 'w')

for i in range(len(input_data)):
    current_input = input_data[i].strip().split(",")
    output_data = arrayReversal(current_input)
    print(output_data)
    output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=output_data,mode = 'a')
    




