#Pomodoro timer
#1.importing
import time
#def
def pomodoro_timer(total_time, work_time, break_time):
    cycles = total_time // (work_time + break_time)
    
    for _ in range(cycles):
        print("Work phase -", work_time, "minutes")
        # Convert minutes to seconds 
        time.sleep(work_time * 60)  
        
        print("Break phase -", break_time, "minutes")
        # Convert minutes to seconds
        time.sleep(break_time * 60) 
    
    print("Pomodoro timer completed!")

# Set the total time, work time, and break time (in minutes)
total_time = 60  # Total time for the Pomodoro timer
work_time = 25   # Time dedicated to focused work
break_time = 5   # Time for short breaks

pomodoro_timer(total_time, work_time, break_time)
