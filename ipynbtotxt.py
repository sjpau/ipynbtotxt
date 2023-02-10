import json
import sys

if len(sys.argv) != 2:
    print("Please pass the name of the Jupiter notebook file.")
    exit(1)
try:
    with open(sys.argv[1]) as f:
        data = json.load(f)
except json.decoder.JSONDecodeError as e:
    print("Error: Unable to parse Jupyter notebook file.", e)
    exit(1)

# "Cells" is a parameter in Jupyter notebook JSON
cells = data["cells"]

# Extract the plain text from each cell
plain_text = ""
for cell in cells:
    if cell["cell_type"] == "markdown":
        plain_text += "".join(cell["source"])

print(plain_text)

# Over-the-top functionality; uncomment if needed.

#out = open('out.txt', 'w')
#out.write(plain_text)
#out.close()
