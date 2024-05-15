import time
from scapy.all import *

def get_remote_timestamp(host):
    # Send ICMP timestamp request and capture response
    ans, unans = sr(IP(dst=host)/ICMP(type="timestamp_request"), timeout=2, verbose=False)
    
    if ans:
        # Extract the original timestamp from the response
        remote_timestamp = ans[0][1][ICMP].ts_ori
        return remote_timestamp
    else:
        return None

def calculate_time_difference(remote_timestamp):
    if remote_timestamp:
        # Calculate the difference between local and remote timestamps
        local_timestamp = time.time()
        time_difference = abs(local_timestamp - remote_timestamp)
        return time_difference
    else:
        return None

def main():
    target_host = input("Enter the target host IP address: ")
    remote_timestamp = get_remote_timestamp(target_host)
    
    if remote_timestamp:
        time_difference = calculate_time_difference(remote_timestamp)
        if time_difference is not None:
            print(f"The difference between the local and remote clocks is {time_difference} seconds.")
        else:
            print("Failed to calculate time difference.")
    else:
        print("No response received from the target host.")

if __name__ == "__main__":
    main()
