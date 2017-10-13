
import sys
import puzzle 
import time
from search_algorithms.bfs import BFS
from search_algorithms.dfs import DFS
from search_algorithms.ids import IDS
from search_algorithms.greedy1 import GREEDY1
from search_algorithms.greedy2 import GREEDY2
from search_algorithms.astar1 import ASTAR1
from search_algorithms.astar2 import ASTAR2



t = puzzle.TilePuzzle(int(sys.argv[1]))


t.permute(int(sys.argv[2]))

print "Initial Board Configuration:"
t.printPuzzle()


if sys.argv[3] == "bfs":
    print "BFS Search Algorithm initiated"
    start_time = time.time()
    BFS(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

#Disclosure: For the nature of the problem, as the search tree is infinite, DFS will rarely find a solution to the puzzle
elif sys.argv[3] == "dfs":
    print "DFS Search Algorithm initiated"
    start_time = time.time()
    DFS(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "ids":
    print "IDS Search Algorithm initiated"
    start_time = time.time()
    IDS(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "greedy1":
    print "GREEDY1 Search Algorithm initiated"
    start_time = time.time()
    GREEDY1(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "greedy2":
    print "GREEDY2 Search Algorithm initiated"
    start_time = time.time()
    GREEDY2(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "astar1":
    print "A*1 Search Algorithm initiated"
    start_time = time.time()
    ASTAR1(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "astar2":
    print "A*2 Search Algorithm initiated"
    start_time = time.time()
    ASTAR2(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

elif sys.argv[3] == "all":
    print "BFS Search Algorithm initiated"
    start_time = time.time()
    BFS(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

    print "IDS Search Algorithm initiated"
    start_time = time.time()
    IDS(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

    print "GREEDY1 Search Algorithm initiated"
    start_time = time.time()
    GREEDY1(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

    print "GREEDY2 Search Algorithm initiated"
    start_time = time.time()
    GREEDY2(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

    print "A*1 Search Algorithm initiated"
    start_time = time.time()
    ASTAR1(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"

    print "A*2 Search Algorithm initiated"
    start_time = time.time()
    ASTAR2(t).solvePuzzle()
    print "The Search Algorithm took", float(time.time() - start_time), "seconds"