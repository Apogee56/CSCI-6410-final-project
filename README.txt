This program runs using the following command when run out of the terminal:

python abc.py graph.txt

The text file can be replaced with any file of a similar format. 
The first number in the file is the number of vertices in the graph.
The second number in the file was the number of edges.
The remaining lines are the edges in the form WEIGHT V1 V2.

There are parameters at the top of the file which can be modified to change how the program runs:
limit: the number of times a food source may go unimproved before it is replaced with a new source
n_e: the number of employeed bees and the number of solutions to display at the end
MFE: the maximum number of evaluations, acts as a termination condition

The program will, upon completion, list off a collection of spanning trees which it found during the course of it's operation,
in the form of a tuple containing their weight and the binary encoding representing the edges used from the original graph.

My algorithm differs from the one described in my base paper in that they provided no details at all on the onlooker bee stage,
and so I elected to not include such a stage in this implementation of the algorithm.

I have included the files graph.txt and papgraph.txt. graph.txt is a file containing my very own small graph. papgraph.txt is from the
paper I covered in homework 3 on a similar algorithm. Indeed, the authors of my current base paper did not include the edge weights of 
their graph, so there is no way to compare results. However, my results can be compared to those in the paper from homework 3. Despite
the lack of an onlooker bee stage, the performance of my implementation is quite similar to the experimental results shown in the homework
3 paper.