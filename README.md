# CZ2001-Project-2

## BEFORE RUNNING THE ALGORTHM!

1. Open up the Interface.py file and edit all the path variables to the respective local paths on your own computer
2. Ensure the \\ is used instead of \ to prevent any errors from occuring.
   - graphPath will be the graph that the algorithm will run on
   - opPath will be .txt file that will have the output
   - hospitalPath will be the .txt file that contains the hospital nodes

- For example: C:\Users\madra\Documents\CZ2001\CZ2001-Project-2\Paths\roadNet-TX.txt
- Replace with: C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\roadNet-TX.txt

## Information:

1. All inputs will have the be in the same format as those already in the Paths folder
2. All graph outputs will be stored in the Outputs folder
3. Algorithm will be run from the Interface.py file

## To run the algorithm on custom graph:

1. Place the text file into the Paths folder
2. Copy the path of this new text file
3. Open up the interface.py file
4. Paste the path into the graphPath variable

## To change the hospital nodes:

1. Open the hospital.txt file
2. Add and remove hospitals to follow the same format shown in the file
3. Ensure that the total number of hospitals is reflected at the top of the file after the '#'

## Creating a seperate output file:

1. In the outputs folder, add a new .txt file and copy its path
2. Replace the hospitalPath variable with the path you just copied
3. Once again, ensure that \\ is used instead of \ (Refer to BEFORE RUNNING THE ALGORITHM)

## To generate a random graph:

1. Run the command `pip install networkx` to download the necessary package
2. Open the GraphGeneratorl.py file
3. Use the generateRandGraph() function to generate a random graph
4. n will be the number of total nodes and p will be the probability of an edge within each node
5. Run the file and a random graph should be generated
6. Replace the graphPath variable with this new path

### Done by:

- Goh Wei Pin
- Tan Keng Kai Luke
- Jonathan Chang Ji Ming
- Lynn Enhua Masillamoni
