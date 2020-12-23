import json


simple_list = [1, "simple", "list"]

with open("newJson.json", "w") as f:
    json.dump(simple_list, f)



# read file
jsondata = ""
with open("1__exampled_json_file.json", "r") as jsonfile:
    for f_line in jsonfile:
        jsondata += str(f_line)
# or
#   with open("1__exampled_json_file.json", "r") as jsonfile:
#       jsondata = jsonfile.read()

# parse file
json_obj = json.loads(jsondata)

# print(json_obj)

for single_obj in list(json_obj):
    print(single_obj)
    print(json_obj['glossary'])

for el in list(json_obj['glossary']):
    print(str(el) + " --- " + str(json_obj['glossary'][str(el)]))
