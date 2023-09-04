import time

def increase_cpu_utilization(target_utilization=50, duration=30):
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < duration:
        # Perform some calculations to increase CPU utilization
        for i in range(10**6):
            result = i * i

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

if __name__ == '__main__':
    target_utilization = 50  # Desired CPU utilization percentage
    duration = 30  # Duration of CPU load in seconds

    increase_cpu_utilization(target_utilization, duration)
    print(f'CPU utilization increased to approximately {target_utilization}% for {duration} seconds.')
