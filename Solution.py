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
        """
        Prob 2: going to submit our answer for p1 to see where we at commiting now for fresh start
        """
        clients = list(self.info["list_clients"]) #correction this will give me the client ids so ill submit this since it keeps saying im giving strings and not int. I found this in utlitly.py checking if it works - Fy
        paths = bfs_path(self.graph, self.isp, clients) #Bfs path will take the graph, use isp as starting node and find a path for every client, going to submit -FY
        bandwidths, priorities = {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
