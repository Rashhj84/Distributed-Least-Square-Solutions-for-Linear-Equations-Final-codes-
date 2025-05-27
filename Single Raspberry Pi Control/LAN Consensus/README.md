# LAN Consensus
In the above implementation in Raspberry Pi, one should choose a Raspberry Pi as coordinator and get IP address. Then we have to get the IP address of the other Raspberry Pi. We then have to include them in the sender.py and coordinator.py files. Its also important to choose the port number for every nodes and coordinators. Any valid port number can be choosed but it needs to be maintained througout. After this we need to establish SSH and SCP connection between all Raspberry Pi. The step for connection and all other details have been mentioned in another document. Make sure that the node.py files (ex: n1.py) has the ip address of the correct node it needs to reach.

Once all the above steps are done, run the sender.py which is responsible to both send and run the file in the other Raspberry Pi. After waiting for a few seconds and running the Coordinator.py will send initiation message to other nodes and start the consensus process.

All the Raspberry Pi just need to be connected to power supply and the Switch (through Ethernet Connection) for the consensus. The processes like obtaining IPs and establishing SSH connection might require other nodes to be connected to the display (monitor). Once the above steps are done, we only have to connect the display (monitor) to the Coordinator to observe consensus. 

Once the consesnus is over, the csv file containing data of evolution is sent back to coordinator by each node. We then run plotter.py of observe the evolutions.
