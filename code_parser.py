import sys

from acom_config import *

filename = sys.argv[1]

codeBlock = []
actualCode = []
counter = 0
incrementer = 0

# Read in our MD file
#with open(base_path + filename, "r") as f:
with open(filename, "r") as f:

    inputLines = f.readlines()
    
    # For each line, search for our code block delimiters
    # We'll figure out if start and end later
    for i, line in enumerate(inputLines):
        if "```" in line:
            codeBlock.append(counter)
        counter += 1

# Reset our counter
counter = 0

# Now loop through our array of start and end code lines
while counter < len(codeBlock):

    # Get our start line number and how many lines of actual code are in this block
    codeLineStart = codeBlock[counter] + 1
    codeLineLength = ((codeBlock[counter + 1] - codeBlock[counter])) - 1
    
    # Loop through our actual code block and output
    while incrementer < codeLineLength:
    
        # We only want to process lines that begin with 'azure'
        # This will also need to be expanded to other code samples, we're just doing Azure CLI
        if inputLines[codeLineStart].startswith('azure'):
            actualCode.append(inputLines[(codeLineStart + incrementer)])
            incrementer +=1
            
        # Otherwise these are likely just showing code output
        # This isn't foolproof, should probably check this further
        else:
            incrementer += 1
            
    # Reset or increment our counters accordingly        
    incrementer = 0
    counter += 2
    
# Now write back out to file so that our build tool can import it
with open(commands_list, "w") as f:
    for s in actualCode:
       f.write(s)