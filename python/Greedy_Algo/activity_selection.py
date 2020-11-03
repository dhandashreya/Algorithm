# function to select maximum non conflicting activities
def activity_selection(s, f):
    k = list(zip(s, f))
    time = []
    # to sort the activities according to the finish time
    def sort_finish(ele):
        return ele[1]
    k.sort(key = sort_finish)
    for ele in k:
        time.append(ele)
    print(time[0])
    i = 0
    for j in range(1, len(time)):
        if time[i][1] <= time[j][0]:
            print(time[j])
            i = j

start = [5, 1, 3, 0, 5, 8]
finish = [9, 2, 4, 6, 7, 9]
activity_selection(start, finish)
