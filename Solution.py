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
        Prob 2: revenue is off, but here is what we have to do: for each of the clients we can run bfs to find the shortest delay
        then we should give each client a deadline to help us find out the max delay for each client. we also need to have a way to track
        how many packets are in a node to get rid of congestion like pn=0. ill try to sort the clients by higher priority being our rev first and if that
        doesnt work then we can start with the most needy clients. if we use dijstras algo we can find all the paths for the packets and then if we set the edges weights outselfs 
        we can control the flow of dijstras which controls the congestion and nodes that are at their max bandwidth from clogging.
        """
        graph = self.graph #added these for QOL - FY
        isp = self.isp
        info = self.info
        clients = list(info["list_clients"]) #correction this will give me the client ids so ill submit this since it keeps saying im giving strings and not int. I found this in utlitly.py checking if it works - Fy
        bandwidths = info["bandwidths"]

        #dijkalgo done but not tested and need to use it to get the paths, also need to implement the packet load tracking and update it as we assign paths to clients - Fy

        # Problem 1)
        paths = bfs_path(graph, isp, clients) #Bfs path will take the graph, use isp as starting node and find a path for every client, going to submit -FY
        bandwidths, priorities = {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN

        # Problem 2 main code:
        
        return (paths, bandwidths, priorities)
