import os

inputPath = os.path.join(os.getcwd(),"dsa/input.txt")
outputPath = os.path.join(os.getcwd(),"dsa/output.txt")


def read_input():
    with open(inputPath, "r") as infile:
        input_data = infile.readlines()
    print(len(input_data))
    return input_data

def write_output(output_data="",mode = 'a'):
    '''
    modes are nothing but the file handling modes in python.
    
    '''
    with open(outputPath,mode) as outfile:
        outfile.write(output_data)