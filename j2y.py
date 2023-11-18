import json
import yaml
def converter(file1):
    with open(file1, 'r') as f:
        new_file1 = json.load(f)

    with open(file1.replace(".json", ".yaml"), "w") as yaml_file:
        yaml.dump(new_file1, yaml_file)

    with open(file1, 'r') as yaml_file:
        return yaml_file.read()

converter("donuts.json")
converter("emojis.json")