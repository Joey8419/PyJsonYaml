import json
import yaml

def converter2(file2):
    with open(file2, 'r') as f, open(file2.replace("yaml", 'json'), "w") as json_file:
        yaml_object = yaml.safe_load(f)
        return json.dump(yaml_object, json_file)

converter2("verify.yaml")
converter2("xmas.yaml")