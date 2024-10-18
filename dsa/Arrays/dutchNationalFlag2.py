import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles
readFiles = readFiles()

#writing None to the output file
readFiles.write_output(mode = 'w')

#getting the input
input_data = readFiles.read_input()

# move all the negative elements to one side of an array
# function

def dutchFlag(input:list):

    start = 0
    last = len(input)-1
    

    while start <=last:
        
        if input[start]<0:
            start+=1
        elif input[start]>=0:
            #swap with last element
            input[start],input[last]=input[last],input[start]
            last-=1
        

    return input
    


for i in range(len(input_data)):
    
    current_input = input_data[i].strip().split(",")
    
    current_input = [int(x) for  x in current_input]
    output_data = dutchFlag(current_input)
    print(output_data)
    # output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=str(output_data)+"\n",mode = 'a')