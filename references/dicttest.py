data = [{"MSFT": {"key1": "value1", "key2": "value2"}}, {"TSLA": {"key1": "value3", "key2": "value4"}}]
for i in data:
    for j in i:
        print(i[j])