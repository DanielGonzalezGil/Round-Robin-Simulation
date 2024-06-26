import random
import math


def generate_interarrival_times(
    number_Of_processes, minimum_interarrival, max_interarrival
):
    """
    Arguments that are passed to the function are as follows:
        number_Of_processes (int): The number of processes.
        min_interarrival (float): The minimum interarrival time.
        max_interarrival (float): The maximum interarrival time.

    Returns:
        A list of random interarrival times between the min and max interarrival times.

    Notes:
        The underscore is used as a placeholder because we only the number of iterations is important, not the actual value.
        The math.floor function is used to round down to the nearest integer.
        The random.uniform function was then used to generate a random float between the minimum and maximum interarrival times.
    """

    return [
        math.floor(random.uniform(minimum_interarrival, max_interarrival))
        for _ in range(number_Of_processes)
    ]


def generate_arrival_times(number_Of_processes, minimum_interarrival, max_interarrival):
    """
    Generates a list of arrival times for a given number of processes.

    Args:
        number_Of_processes (int): The total number of processes.
        minimum_interarrival (int): The minimum interarrival time between processes.
        max_interarrival (int): The maximum interarrival time between processes.

    Returns:
        A list of arrival times for each process.

    Notes:
        A random list of interarrival times between the max and min interarrival is generated using the generate_interarrival_times function.
        The arrival_times list is then generated by summing the interarrival_times list.
        The arrival_times list is then inserted into the first index of the arrival_times list.
    """
    # generates a random list of interarrival times between the max and min interarrival
    interarrival_times = generate_interarrival_times(
        number_Of_processes, minimum_interarrival, max_interarrival
    )

    # generates a list of arrival times for each process
    arrival_times = [sum(interarrival_times[:i]) for i in range(1, number_Of_processes)]

    # inserts the arrival times list into the first index of the arrival times list
    arrival_times.insert(0, 0)

    return arrival_times


def generate_service_times(number_Of_processes, minimum_service_time, max_service_time):
    """
    Generates a list of service times for a given number of processes.

    Args:
        number_Of_processes (int): The number of processes.
        minimum_service_time (float): The minimum service time.
        max_service_time (float): The maximum service time.

    Returns:
        A list of random service times for each process between the min and max service time.

    Notes:
        The underscore is used as a placeholder because we only the number of iterations is important, not the actual value.
        The math.floor function is used to round down to the nearest integer.
        The random.uniform function was then used to generate a random float between the minimum and maximum service times.
    """
    return [
        math.floor(random.uniform(minimum_service_time, max_service_time))
        for _ in range(number_Of_processes)
    ]


# initailizing values
number_Of_processes = 99
minimum_interarrival = 4
max_interarrival = 10
minimum_service_time = 2
max_service_time = 6

# calling the functions
arrival_times = generate_arrival_times(
    number_Of_processes, minimum_interarrival, max_interarrival
)
service_times = generate_service_times(
    number_Of_processes, minimum_service_time, max_service_time
)
Interarrival_times = generate_interarrival_times(
    number_Of_processes, minimum_interarrival, max_interarrival
)

# displaying the results
# print("Arrival Times:", arrival_times)
# print("Service Times:", service_times)
# print("interarrival_times:", Interarrival_times)
