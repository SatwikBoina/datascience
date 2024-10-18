import os

class readFiles : 
    def __init__(self):
        self.inputPath = os.path.join(os.getcwd(),"dsa/input.txt")
        self.outputPath = os.path.join(os.getcwd(),"dsa/output.txt")
    def read_input(self):
        with open(self.inputPath, "r") as infile:
            input_data = infile.readlines()
        print(len(input_data))
        return input_data

    def write_output(self,output_data="",mode = 'a'):
        '''
        modes are nothing but the file handling modes in python.
        
        '''
        with open(self.outputPath,mode) as outfile:
            outfile.write(output_data)

