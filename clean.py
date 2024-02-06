import json

clean_data = []

with open(r"coffee_guide\data\clean_address.json", encoding="utf-8") as data_file:
    data = json.loads(data_file.read())
    for data_object in data:
        new_data = {
            "address": data_object["address"],
            "lat": float(data_object["lat"]),
            "lon": float(data_object["lon"]),
        }
        if new_data in clean_data:
            continue
        clean_data.append(new_data)
    uniq = []
    for i in clean_data:
        if i["address"] in uniq:
            clean_data.remove(i)
        uniq.append(i["address"])


with open(r"coffee_guide\data\clean_address.json", "w", encoding="utf-8") as data_file:
    json.dump(clean_data, data_file, ensure_ascii=False, indent=4)
