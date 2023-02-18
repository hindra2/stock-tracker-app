import pickle

data_list = []

with open("user_stock", "rb") as f:
    try:
        while True:
            data = pickle.load(f)
            data_list.append(data)
    except EOFError:
        print("Done loading data")
f.close()

for dict_ in data_list:
    for ticker in dict_:
        dict_data = dict_[ticker]
    print(dict_data)
    gain = 10
    dict_data["Gain"] = gain
       
with open("user_stock", "wb") as f:
    pickle.dump(data, f)
f.close()


with open("user_stock", "rb") as f:
    try:
        while True:
            data = pickle.load(f)
            data_list.append(data)
    except EOFError:
        print("Done loading data")
f.close()
print(data_list)