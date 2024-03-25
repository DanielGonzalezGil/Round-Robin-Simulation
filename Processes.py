# importing rich library to create tables
from rich.console import Console
from rich.table import Table

# importing Random_ASI_Times.py to get the arrival, service and interarrival times
import Random_ASI_Times


# class for creating instances of the processes in the Round Robin algorithm
class ProcessQueue:
    # constructor to initalize the attributes for the processes
    def __init__(self, ProcessID, ServiceTime, ArrivalTime):
        self.ProcessID = ProcessID
        self.ServiceTime = ServiceTime
        self.ArrivalTime = ArrivalTime
        self.processes = []

    # method to add elements to the ProcessList
    def add_to_list(self, data):

        for process in data:
            self.processes.append(
                ProcessQueue(
                    process["id"],
                    process["Servicetime"],
                    process["arrivaltime"],
                )
            )

    # for i in range(100):
    #     self.processes.append(
    #         ProcessQueue(
    #             i + 1,
    #             Random_ASI_Times.service_times[i],
    #             Random_ASI_Times.arrival_times[i],
    #         )
    #     )

    # method to create the table for the processes
    def create_ProcessTable(
        self, processes
    ):  # added processes as an argument to create the rows for tables

        process_table = Table(title="Process Table")

        # Adding columns for the table
        process_table.add_column("Process ID", justify="left")
        process_table.add_column("Service Time", justify="left")
        process_table.add_column("Arrival Time", justify="left")

        # Adding rows for the table
        for process in processes:
            process_table.add_row(
                f"{process.ProcessID}",
                f"{process.ServiceTime}",
                f"{process.ArrivalTime}",
            )

        console = Console()
        console.print(process_table)


# creating instances of the processes
ProcessQueue1 = ProcessQueue(1, 75, 0)
ProcessQueue2 = ProcessQueue(2, 40, 10)
ProcessQueue3 = ProcessQueue(3, 25, 10)
ProcessQueue4 = ProcessQueue(4, 20, 80)
ProcessQueue5 = ProcessQueue(5, 45, 85)

# Call the add_to_list method on each instance
ProcessQueue1.add_to_list(ProcessQueue1)
ProcessQueue2.add_to_list(ProcessQueue2)
ProcessQueue3.add_to_list(ProcessQueue3)
ProcessQueue4.add_to_list(ProcessQueue4)
ProcessQueue5.add_to_list(ProcessQueue5)

# creating a single list of the processes instances to put them in one table
processes = [ProcessQueue1, ProcessQueue2, ProcessQueue3, ProcessQueue4, ProcessQueue5]

# printing table
Process_Table = ProcessQueue1.create_ProcessTable(ProcessQueue1.processes)

print(ProcessQueue1)
