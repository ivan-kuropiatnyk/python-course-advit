print('============Less24-RegExpressions-part-1===============')
print('===========================')

import re

input_filename = "Less24InputFile"
output_filename = "Less24OutputFile"

inputfile = (input_filename, mode='r', encoding='Latin-1')
outputfile = (input_filename, mode='w', encoding='Latin-1')
text_of_input_file = inputfile.read()

lookfor = r"[A-Z][a-z]+"

results = re.findall(lookfor, text_of_input_file)

for item in results
    print(item)
    outputfile.write(item+"\n")

print("Total: " + str(len(results)))
