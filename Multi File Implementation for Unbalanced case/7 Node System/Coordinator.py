import socket
import json
import threading 
import time
import numpy as np


A = [
        [[1, 5, -1, -3, -5, -5, -3, -1, -4], [0, 2, 5, 5, 4, 3, -3, 0, 2], [3, -4, 5, -4, -4, -2, 5, 4, 1], [-3, -2, 0, 2, 0, 2, -3, -2, 5], [2, 4, -2, -5, 3, -3, 2, -4, -1], [-5, -1, -4, 4, -5, 3, 3, -2, 2], [1, 2, -2, -5, -5, 0, -4, -3, -5], [0, 4, -2, 5, 0, 3, -3, 0, 0], [-1, 1, -2, -4, 2, -1, 5, -1, -3], [4, 2, -4, -2, -5, 5, -2, -5, -4], [5, -4, 1, 5, -2, -2, 5, 1, 3]], 
        [[-3, 0, 2, -2, 3, -5, -2, -2, 0], [-4, -2, -2, -1, 2, -3, 3, 0, 0], [3, 2, -3, -2, 5, -4, 0, -5, -4], [-1, 5, 5, 3, -3, -1, -3, 0, -2], [0, 3, -4, -4, -4, 4, -3, 0, 1], [2, 1, -5, 5, 1, -4, -4, 3, 0], [5, 5, 1, -2, 4, 3, 5, -5, 4], [5, 3, 3, -3, 5, 4, 4, -1, 1], [4, 4, 2, -2, -1, 2, -1, 5, 2], [4, -3, 1, 5, -3, 4, -5, -1, 2], [3, 2, -1, 5, -3, 2, 3, 2, 3]] ,
        [[1, -5, -5, -4, 4, -1, 2, 0, 2], [5, 3, 0, -3, -1, 3, 4, -1, 0], [1, 2, 1, 5, 4, 1, -2, 3, -3], [5, 4, 0, -2, 1, 1, -1, 1, 5], [-5, 5, 1, 1, 4, 2, -2, -5, 3], [0, -5, 2, 5, 0, -4, 3, 3, 4], [1, -4, 5, -5, 0, 0, 3, -1, -2], [-1, 5, 0, 2, -2, 0, 5, 3, -1], [4, -1, 4, 1, -3, 5, -2, 0, 1], [5, 1, 5, -2, -5, -5, -3, 0, -1], [5, 3, -2, -3, 2, 1, -4, -5, -4]] ,
        [[-1, -2, -4, 4, -2, -1, -2, -3, -2], [4, 5, 5, 1, -5, -4, 4, 5, 1], [3, -3, 3, 4, -1, 1, -1, 3, 5], [1, -2, 2, -5, 0, 3, -5, -2, -2], [1, 5, 1, 3, 1, -4, -3, -5, -3], [0, 2, -1, 1, 2, 0, 1, -3, 0], [5, 3, 1, 2, 1, 5, 2, -5, -4], [3, -3, 1, 5, 3, -3, 1, 4, -5], [5, 5, 1, -4, -3, 5, -5, 5, 5], [3, -5, -5, 3, -4, 2, 4, 2, -5], [-5, -4, 1, -2, 3, 5, 1, -3, 1]], 
        [[0, 3, 1, -5, -4, -5, 5, -1, 5], [-1, -1, 1, -4, -3, -5, -4, -3, -4], [1, 0, 2, -3, -1, -4, 1, 4, 1], [-2, 1, -2, -3, -5, -5, 3, 3, -2], [1, 3, 0, 0, 3, 3, -3, -5, 3], [5, -2, 3, 5, -2, -5, 4, -4, 0], [-3, 0, -2, 2, 1, 2, 1, -1, -3], [-3, 3, 1, 1, -1, -5, 4, 0, -5], [5, 5, -5, -1, 2, 4, 4, -4, 4], [2, 0, -3, 5, 0, -4, -2, -2, 1], [-4, 5, 5, -5, -1, 4, -3, 3, -4]], 
        [[0, 5, -3, 3, 4, 3, 0, -3, 3], [-5, 1, -2, 1, -4, 4, 4, -5, -3], [-1, 4, -5, 5, -4, -3, 1, 4, -3], [5, 3, -1, 0, 2, 2, 0, -2, 1], [2, 2, 1, 4, 4, 3, -4, 1, -2], [1, 3, 1, 5, 4, -5, -2, 0, -2], [1, 1, 5, 2, -2, -4, 3, 3, -4], [3, -2, 2, 3, 4, 4, -2, 3, 0], [4, -2, -4, 4, -5, -5, 3, 4, -4], [-4, -1, -5, 3, -1, -5, -5, -5, 3], [-3, 4, 5, 2, -1, 1, 2, 4, 2]] ,
        [[9, -2, 18, 12, 3, 15, 2, 11, 2], [8, -5, 0, 9, 8, 6, -4, 6, 12], [-5, 3, 5, 3, 4, 18, 5, -2, 4], [-2, -3, 1, 7, 7, 0, 12, 5, -1], [7, -16, 5, 6, -10, -1, 22, 21, 4], [-2, 11, 10, -17, 8, 24, 2, 4, 0], [-5, -3, -4, 10, 8, 2, -7, 14, 15], [-5, -7, 0, -11, -3, 6, -8, -6, 15], [-10, -10, 7, 7, 10, -9, 1, 2, 5], [-13, 6, 15, -4, 20, 8, 14, 11, 4], [1, -2, -3, 5, 14, 2, -3, 8, 7]] 
    ]

b = [
        [[12], [10], [2], [13], [10], [14], [-2], [-1], [-5], [4], [2]] ,
        [[-2], [4], [-3], [5], [9], [-1], [12], [5], [2], [10], [6]] ,
        [[-2], [13], [7], [-5], [13], [9], [9], [-3], [1], [15], [6]] ,
        [[11], [1], [10], [14], [4], [11], [-1], [1], [5], [-4], [6]] ,
        [[14], [15], [-5], [11], [10], [10], [2], [-1], [12], [1], [8]], 
        [[10], [-1], [15], [8], [9], [2], [15], [8], [1], [3], [12]] ,
        [[70], [54], [83], [40], [12], [109], [36], [177], [84], [7], [7]] 
    ]

def print_time_taken(description, start_time):
    end_time = time.time()
    print(f"{description} took {end_time - start_time:.6f} seconds")
    #This function is used to print the time taken from start of each step when the start_time inputted in the function is the time recorded at the start
    #Currently in this code all the print_time_functions are removed. If necessary the user can use this to get an idea of execution time

def send_init_message(ip, port, node_id,iteration_number,neighbors,alpha,iter,nodes,beta,gamma,delta,gaps,initiation,indegree):
    #This function is responsible to send initialisation message of all the nodes when the coordinator iteration starts.
    #Along with the initialisation message things like iteration number, alpha, sleeptime,etc.. are sent.
    message = {
        "init": "INIT",
        "inum": iteration_number,
        "alpha": alpha,
        "iter": iter,
        "neighbors": neighbors,
        "nodes": nodes,
        "num_nodes": num_nodes,
        "sleep_time" : sleep_time,
        "beta": beta,
        "gamma": gamma,
        "delta": delta,
        "A": A[node_id-1],
        "b": b[node_id-1],
        "gaps": gaps,
        "node_id": node_id,
        "strt": initiation,
        "indegree": indegree
    }
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(json.dumps(message).encode('utf-8'), (ip, port))   #This line sends all the above data in message to the ip of the node and its port.
        #ip and port in the above statement denotes the ip and port in which the destination nodes listens

def send_messages_to_node(ip, port, node_id, neighbors, nodes,iteration_number,alpha,iter,beta,gamma,delta,gaps,initiation,indegree):
    send_init_message(ip, port, node_id, iteration_number,neighbors,alpha,iter,nodes,beta,gamma,delta,gaps,initiation,indegree)

if __name__ == "__main__":
    nodes = [("127.0.0.1",12345,1), ("127.0.0.1",12346,2), ("127.0.0.1",12347,3), ("127.0.0.1",12348,4), ("127.0.0.1",12349,5), ("127.0.0.1",12350,6), ("127.0.0.1",12351,7)]   #Node information is stored in this list
    #The nodes list contains every nodes ip address along with the port which the node listens. The above line is to changed while changing the order and number of nodes.
    #The tuple at index 0 represents node 1 and index 1 represents node 2 and so on.
    #Its important to make sure the node numbers match with their ip addresses in both coordinator and node.py file
    iteration_number = 1000000  #Its upto the user to decide the number of iterations. More the iterations accurate are the results
    sleep_time = 0.006       #Sleep time has some constraints
    gaps = 1000
    initiation = 10
    # For LAN connection sleep time can not be less than 0.0033 seconds for good results
    # For WiFi connection sleep time can not go lesser than 0.1 seconds for accurate results
    neighbors = [
        [],
        [2,3,4,5,6],
        [7],
        [2],
        [1,3,5],
        [6],
        [7],
        [1]
    ]
    # Data transfer is an edge. (Opposite to convention)
    siz = len(neighbors)
    indegree = [0]*siz
    for i in range(1,siz):
        for j in neighbors[i]:
            indegree[j]+=1
    print(indegree)
    # Neighbor list is supposed to be modified to change the edges of the graph which is then responsible for change in communication
    num_nodes = 7     #Change this when there is a change in number of nodes
    alpha = 5 
    beta = 1e-2
    gamma = 5e-3
    delta = 3e-3   
    iter = 1
    start_time = time.time()  #This measures the time taken for each step for our use. These can be removed to make the code run faster
    threads = []
    #This portion of the code is responsible to perform threading so that all the messages sent to the nodes are sent simultaneously.
    #The threads list initially stores all the threads that are to be started. Its then initiated in the loop below for messages to be sent simultaneously
    for node in nodes:
        thread = threading.Thread(target=send_messages_to_node, args=(node[0], node[1], node[2], neighbors, nodes,iteration_number,alpha,iter,beta,gamma,delta,gaps,initiation,indegree))
        threads.append(thread)
    time.sleep(1)
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Initialization messages sent to all nodes.")