import json
import sys

if len(sys.argv) != 2:
        print("Usage: python pyfile_name.py <file_name>")
        sys.exit(1)

def json_to_nagios_config(json_data):
    config_lines = []

    for obj_type, objects in json_data.items():
        for obj in objects:
            config_lines.append(f"define {obj_type} {{")
            for key, value in obj.items():
                config_lines.append(f"    {key} {value}")
            config_lines.append("}\n") 

    return "\n".join(config_lines)

# Load the JSON data
json_file_path = sys.argv[1]  
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Convert JSON to Nagios config format
nagios_config = json_to_nagios_config(json_data)

# Print or save the Nagios configuration
print(nagios_config)

# Optionally, write to a Nagios config file
with open('nagios_config.cfg', 'w') as nagios_file:
    nagios_file.write(nagios_config)
