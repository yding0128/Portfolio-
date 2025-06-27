import json
import csv

# Load the contents of the JSON file into a Python object
with open('data_all.json') as file:
    data = json.load(file)


def get_total_grade():
    for i in range(len(data)):
        data[i]['grades'] = round(((
            data[i]["block_a_score"] + data[i]["block_b_score"]) / 34 * 100), 2)


        # print(data[i]['grades'])
get_total_grade()


def get_calculator_usage():
    for i in range(len(data)):
        calculator = data[i]['assistive_uses']['4']
        data[i]['calculator_usage'] = calculator


get_calculator_usage()


def get_visits():
    for i in range(len(data)):
        visit_times = 0
        for each in data[i]['q_stats']:
            visit_times += (data[i]['q_stats'][each]['visits'])

        print(visit_times)

        if 'avg_visit_times' not in data[i]:
            data[i]["avg_visit_times"] = round((visit_times / 34), 3)

    return visit_times

get_visits()


def get_no2nd_attempts():
    for i in range(len(data)):
        data[i]['no2nd_attempts'] = 0
    for i in range(len(data)):
        if data[i]['avg_visit_times'] == 1.00 and data[i]['grades'] >= 70.00:
            data[i]['no2nd_attempts'] = 1


get_no2nd_attempts()


def get_toomuch_attempts():
    for i in range(len(data)):
        data[i]['toomuch_attempts'] = 0
    for i in range(len(data)):
        if data[i]['avg_visit_times'] >= 2.5:
            data[i]['toomuch_attempts'] = 1


get_toomuch_attempts()

list = ["VH098810", "VH098519", "VH098808", "VH139047", "VH098759", "VH098740", "VH134366", "VH098753", "VH134387", "VH098783", "VH098812", "VH139196", "VH134373", "VH098839", "VH098597", "VH098556", "VH098522",
        "VH098779", "VH098834", "VH266695", "VH304549", "VH336968", "VH303873", "VH263651", "VH304553", "VH262355", "VH287980", "VH304990", "VH344346", "VH261992", "VH302900", "VH304197", "VH271388", "VH302334"]


def get_toofast():
    for i in range(len(data)):
        data[i]['toofast'] = 0
    for q in list:
        sortedList = sorted(data, key=lambda x: x['q_stats'][q]['time'])
        top5perc = sortedList[0: int(len(data) * 0.05)]
        for i in range(len(data)):
            if data[i] in top5perc:
                data[i]['toofast'] += 1


    # for i in range(len(data)):
        # print(data[i]['toofast'])
get_toofast()


def get_rapidcopy():
    for q in list:
        for i in range(len(data)):
            if data[i]['toofast'] > 5 and data[i]['q_stats'][q]['correct'] == 2:
                data[i]['rapidcopy'] = 1

get_rapidcopy()


# print(data[0]['time_deltas'][len(data[0]["time_deltas"])-1])


data = sorted(data, key=lambda x: max(x['time_deltas']))

# print(data[0]['time_deltas'][len(data[0]["time_deltas"])-1])


def get_time():
    total_time = 0.0
    counter = 0
    for i in range(len(data)):
        # print(data[i]["student_id"])
        if 'testing_time' not in data[i]:
            data[i]["testing_time"] = round((data[i]["time_deltas"][len(
                data[i]["time_deltas"])-1] / 60), 2)
            total_time += data[i]["time_deltas"][len(data[i]["time_deltas"])-1]
            counter += 1
    avg = total_time / counter
    return avg, counter


avg, students = get_time()
# print(avg)


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
        # print(middle)
    # print(data[middle]['time_deltas'][len(data[middle]["time_deltas"])-1])
    return middle


def get_label():
    middles = data[329:1561]

    # with open('middles.json', 'w') as f:
    #     json.dump(middles, f)

    tails = data[:328] + data[1562:]

    # with open('tails.json', 'w') as f:
    #     json.dump(tails, f)

    for i in range(len(data)):
        data[i]['label'] = 0
        if data[i] in tails:
            data[i]['label'] = 1
        # print(data[i]['label'])


find_mean_record()
get_label()

with open('processed_data_2w.json', 'w') as file:
    json.dump(data, file)
