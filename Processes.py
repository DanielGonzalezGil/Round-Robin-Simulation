# importing rich library to create tables
from rich.console import Console
from rich.table import Table


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

# creating a single list of the processes instances to put them in one table
processes = [ProcessQueue1, ProcessQueue2, ProcessQueue3, ProcessQueue4, ProcessQueue5]

# printing table
Process_Table = ProcessQueue1.create_ProcessTable(processes)
