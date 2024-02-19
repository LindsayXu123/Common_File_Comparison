#Project to compare two files
import sys

script_name = sys.argv[0]
file_1 = sys.argv[1] #arguments
file_2 = sys.argv[2]

print(f"Comparing files '{file_1}' and '{file_2}'...")

def compare_files(file_1, file_2):
    count = 0 #number of common files
    file_1_exists = False
    file_2_exists = False
    
    #read lines from each file
    try:
        with open(file_1, 'r') as file1:
            file1_lines = file1.readlines()       
    except:
        print(f"The first file '{file_1}' could not be found")
    else:
        file_1_exists = True
    
    try:
        with open(file_2, 'r') as file2:
            file2_lines = file2.readlines()
    except:
        print(f"The second file '{file_2}' could not be found")    
    else:
        file_2_exists = True
        
    if file_1_exists and file_2_exists: #will start comparing the files if they both are found
        print("\n"+ "Here is a list of all the common files: ")
        
        with open("common_files", 'w') as common_files: #creates the output file
            common_files.write("Here is a list of common files from the two files: " + "\n")
            
            for i in range(len(file1_lines)): #go through each line in the first file
                line_file1 = file1_lines[i]
                if "/" in line_file1:
                    start_of_file1 = line_file1.rfind('/') #find where the file name starts to only take the content after the /
                    file1_content = line_file1[start_of_file1 + 1:].strip()
            
                    for i in range(len(file2_lines)): # go through each lines in the second file
                        line_file2 = file2_lines[i]
                        if "/" in line_file2:
                            #comparing the line from file 1 to the line from file 2
                            start_of_file2 = line_file2.rfind('/')
                            file2_content = line_file2[start_of_file2 + 1:].strip()
                    
                            if file1_content == file2_content:
                                print(file1_content)
                                common_files.write(file1_content + "\n")
                                count += 1 #add to the count of number of common files
                                
            common_files.write(f"Number of common files: {count}")
            if count == 0:
                common_files.write("There are no common files") #if there are no common files
                            
        print(f"Number of common files: {count}")
        
    else:
        print("Please check your file names") #if the two files were not found
          
compare_files(file_1, file_2)