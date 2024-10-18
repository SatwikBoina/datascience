import os,sys
sys.path.append(os.path.join(os.getcwd(),"dsa"))

from utils.readFiles import readFiles
readFiles = readFiles()

#writing None to the output file
readFiles.write_output(mode = 'w')

#getting the input
input_data = readFiles.read_input()

# distinct elements of two sorted arrays 
# function

def intersection(a:list,b:list):

    result = [None for i in range(len(a) if len(a)<=len(b) else len(b))]
    i =0
    j = 0
    k =0

    while i < len(a) and j < len(b):

        if a[i]<b[j]:
            #result[k] = a[i]
            #k+=1
            i+=1
        elif a[i]==b[j]:
            result[k] = a[i]
            k+=1
            i+=1
            j+=1
        elif a[i]>b[j]:
            #result[k]=b[j]
            j+=1
            #k+=1
    

    return result



def union(a:list,b:list):

    result = [None for i in range(len(a)+len(b))]
    i =0
    j = 0
    k =0

    while i < len(a) and j < len(b):

        if a[i]<b[j]:
            result[k] = a[i]
            k+=1
            i+=1
        elif a[i]==b[j]:
            result[k] = a[i]
            k+=1
            i+=1
            j+=1
        elif a[i]>b[j]:
            result[k]=b[j]
            j+=1
            k+=1
    
    while i<len(a):
        result[k] =a[i]
        i+=1
        k+=1
    while j<len(b):
        result[k]=b[j]
        j+=1
        k+=1


    return result
    


for i in range(len(input_data)):

    # provide two sorted lists seperated by ; in input.txt
    
    a,b = input_data[i].strip().split(";")
    
    a = [int(x) for  x in a.strip().split(',')]
    b = [int(x) for x in b.strip().split(',')]
    output_data = intersection(a,b)
    print(output_data)
    # output_data = ", ".join(output_data)+"\n"

    readFiles.write_output(output_data=str(output_data)+"\n",mode = 'a')