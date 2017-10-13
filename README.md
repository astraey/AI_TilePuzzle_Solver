# Artificial Intelligence based Tile Puzzle Solver 🌊


Tile Puzzle Solver through various Artificial Intelligence Algorithms.

Currently implemented search algorithms: BFS, DFS, IDS, Greedy and A*, with two different heuristics for the last two. 

This framework was built with the idea of benchmarking these algorithms and get an idea of their performance in this type of problems, as well as their limitations dictated by time and space complexity. A full analysis can be found in the full paper.

[Link to Full Paper](documentation/paper.pdf)

To run the code, you can simply execute the following command, where the first parameter represents the size of the tile puzzle, the second parameter will define the number of permutations applied to the initial puzzle and the third parameter will run a specific search algorithm.
```
python tilepuzzle.py 3 3 bfs
``` 
