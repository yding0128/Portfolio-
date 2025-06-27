import json
import csv

# Load the contents of the JSON file into a Python object
with open('/Users/yiding/Desktop/indep/data_all.json') as file:
    data = json.load(file)

# print(data[0]['time_deltas'][len(data[0]["time_deltas"])-1])

data = sorted(data, key=lambda x: max(x['time_deltas']))

# print(data[0]['time_deltas'][len(data[0]["time_deltas"])-1])


def get_time():

    total_time = 0.0
    counter = 0
    for i in range(len(data)):
        # print(data[i]["student_id"])
        if 'testing_time' not in data[i]:
            data[i]["testing_time"] = data[i]["time_deltas"][len(
                data[i]["time_deltas"])-1]
            total_time += data[i]["time_deltas"][len(data[i]["time_deltas"])-1]
            counter += 1
    avg = total_time / counter
    return avg, counter


avg, students = get_time()
print(avg)


def find_mean_record():
    mean = 0
    upper = students
    print(upper, students)
    lower = 0
    middle = (upper+lower)//2
    print(middle)

    while abs(mean-avg) > 0.5:
        mean = data[middle]['time_deltas'][len(data[middle]["time_deltas"])-1]
        if mean < avg:
            lower = middle
            middle = (upper + lower)//2
        else:
            upper = middle
            middle = (upper + lower)//2
        print(middle)
    print(data[middle]['time_deltas'][len(data[middle]["time_deltas"])-1])

    return middle

# find_mean_record()


# middles = data[329:1561]

# with open('middles.json', 'w') as f:
#     json.dump(middles, f)


# tails = data[:328] + data[1562:]

# with open('tails.json', 'w') as f:
#     json.dump(tails, f)


with open('/Users/yiding/Desktop/indep/middles.json') as file:
    middles = json.load(file)

with open('/Users/yiding/Desktop/indep/tails.json') as file:
    tails = json.load(file)

print(len(middles),len(tails))
