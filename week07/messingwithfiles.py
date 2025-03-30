# messing with files
# Author: Orla Woods

FILENAME= "data.txt" # caps means it is set and not going to change
'''

with open(FILENAME, 'rt') as f: # read with text mode (as opposed to binary mode to make sure it's safe)
    # data = f.read() better to do line below instead of just the line commented out here
        for data in f: # will read out data one line at a time
            # print(data, end="") # end = "" strips the extra lines in the output
            # or could write 
            print(data.strip())
            # or print(data[:-1])
'''

with open("data2.txt", "w+") as f: # open in write mode and in text mode
      f.write("what the hell\n") # data2 file doesnt exist as i type this but if i run this file mssingwithfiles.py, it will
      f.write("brown cow\n")  # create the data2.txt file. to check what's in it in the terminal, write cat .\data2.txt
      # if i change the string text here, it will overwrite hte text in data2.txt
      # if i change wt to a it will append into the file and not write over
      f.seek(0) # i was at the end of the program so it didnt print higher info. so need this to go back to the 
      # beginning and print from there
      data = f.read()
      print(data)

print("done")