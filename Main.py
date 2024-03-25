# importing External Python Files
import Random_ASI_Times
import Processes

# printing the table of processes
print(Processes.Process_Table)

# printing Arrival, Service and Interarrival Times
print("Arrival Times:", Random_ASI_Times.arrival_times)
print("Service Times:", Random_ASI_Times.service_times)
print("Interarrival Times:", Random_ASI_Times.Interarrival_times)
