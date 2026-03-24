from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        """
        all we have to do is max out our revenue by keeping all clients subscribed the client unsubscribes if the path we 
        give them is longer than the shortest path from the source. routing delay is the distance from A to B
        so we just have to do BFS from source to client, we also have inf bandwidth so we just gotta give the path
        """
        paths = bfs_path(self.graph, self.source, self.clients) #we alr have bfs from traversals so this should work will submit but commit beforehand -FY
        bandwidths, priorities = {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
