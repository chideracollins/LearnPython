import math


class Person:
    def __init__(self, x):
        global slope, x_mean, y_mean
        self.x = x
        self.y_pred = slope * (self.x - x_mean) + y_mean


def extract_csv(csv, data_lenght):
    file = open(csv, "r")
    data_set = []
    labels = []
    labels_num, data_set_num = 0, 0
    for x in file:
        if len(data_set) == data_lenght:
            break
        data_set_row = []
        txt = ""
        for y in x:
            if y == "," or y.isspace():
                try:
                    try:
                        data_set_row.append(int(txt))
                    except ValueError:
                        data_set_row.append(float(txt))
                except:
                    data_set_row.append(txt)
                txt = ""
                continue
            elif y.isdigit() or y == ".":
                txt = txt + y
            else:
                txt = txt + y
        if all(type(x) == int or float for x in data_set_row) and len(data_set_row) == labels_num:
            data_set.append(data_set_row)
        elif all(type(x) == str for x in data_set_row):
            labels = data_set_row.copy()
            labels_num = len(labels)
    file.close()
    data_set_num = len(data_set)
    return labels, data_set, data_set_num


def linear_reg(data_path, x_label, y_label, x_test, total_data = -1):
    global x_mean, y_mean, slope
    sum_xy = 0
    x_mean = 0
    y_mean = 0
    sum_x_sqr = 0
    slope = 0
    labels, data_set, data_set_num = extract_csv(data_path, total_data)
    try:
        x = labels.index(x_label)
        y = labels.index(y_label)
    except:
        raise Exception("Wrong label(s)!")
    N = math.floor((1- x_test) * data_set_num)
    n = 0
    for row in data_set:
        if data_set.index(row) == N-1:
            break
        x_mean += row[x]
        y_mean += row[y]
        sum_xy += row[x] * row[y]
        sum_x_sqr += pow(row[x], 2)
    del data_set[0 : N-1]
    x_mean = x_mean/N
    y_mean = y_mean/N
    slope =(sum_xy - (N * x_mean * y_mean)) / (sum_x_sqr - (N * pow(x_mean, 2)))
    rmse = 0
    for row in data_set:
        x_train = Person(row[x])
        print("prediction:", x_train.y_pred, "actual:", row[y])
        rmse += pow(row[y] - x_train.y_pred, 2)
    rmse = math.sqrt(rmse / (data_set_num - N))
    print(rmse)


linear_reg("SOCR-HeightWeight.csv", "Height(Inches)", "Weight(Pounds)", 0.25)
# linear_reg("measureOfStrenght.csv", "Age", "Weight", 0.8)

