import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles

readFiles = readFiles()

def arrayRotate(input_data:list,k:int):
    n = len(input_data)
    
    input_data[0:k] = arrayReversal(input_data[0:k])
    input_data[k:] = arrayReversal(input_data[k:])
    input_data = arrayReversal(input_data)


    
    return input_data







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

    
    current_input = input_data[i].strip().split(";")
    k = int(current_input[-1])
    current_input = [int(x) for x in current_input[0].strip().split(',')]
    

    output_data = arrayRotate(current_input,k)
    print(output_data)
    #output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=str(output_data)+"\n",mode = 'a')
    




