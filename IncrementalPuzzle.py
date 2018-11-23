sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10),  (9, 12),(9, 10), (10, 11), (10, 12), (8, 9),(8, 10), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),(8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
def solver(schedule):
    #times with people being added
    incoming_time=[x[0] for x in schedule]
    #times with people leaving
    outgoing_time=[x[1] for x in schedule]
    #times with change associated
    critical_times=set([x[i] for i in range(0,2) for x in schedule])
    sorted_times=sorted(critical_times)
    current_density=0;max_=[0,0]
    for x in sorted_times:
        current_density+=incoming_time.count(x)-outgoing_time.count(x)
        if max_[1]<current_density:
            max_=[x,current_density]
    print("The Best TIme For Party is",max_[0],"where there will be",max_[1],"celebrities")
solver(sched2)