import os
import re
import json
import sys

if len(sys.argv) != 2:
        print("Usage: python pyfile_name.py <file_name>")
        sys.exit(1)

def read_nagios_config(file_path):
    if not os.path.isfile(file_path):
        print(f"{file_path} is not a valid file.")
        return {}

    with open(file_path, 'r') as file:
        content = file.readlines()

    # Initialize the data structure for all definitions
    config_data = {
        "service": [],
        "host": [],
        "hostgroup": [],
        "servicegroup": [],
        "contact": [],
        "contactgroup": [],
        "command": [],
        "timeperiod": [],
        "notification": [],
        "escalation": [],
        "eventhandler": [],
        "hostdependency": [],
        "servicedependency": [],
        "servicetemplate": [],
        "hosttemplate": [],
        "comment": []
    }

    current_section = None
    current_item = None
    in_block = False

    for line in content:
        line = line.strip()

        # Skip comment lines and empty lines
        if line.startswith('#') or not line:
            continue

        # Determine the section based on the line
        if line.startswith('define servicegroup'):
            current_section = 'servicegroup'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define hostgroup'):
            current_section = 'hostgroup'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define hosttemplate'):
            current_section = 'hosttemplate'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define service'):
            current_section = 'service'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define host'):
            current_section = 'host'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define contactgroup'):
            current_section = 'contactgroup'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define contact'):
            current_section = 'contact'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define command'):
            current_section = 'command'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define timeperiod'):
            current_section = 'timeperiod'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define notification'):
            current_section = 'notification'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define escalation'):
            current_section = 'escalation'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define eventhandler'):
            current_section = 'eventhandler'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define hostdependency'):
            current_section = 'hostdependency'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define servicedependency'):
            current_section = 'servicedependency'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define servicetemplate'):
            current_section = 'servicetemplate'
            in_block = True
            current_item = {}
            continue
        elif line.startswith('define comment'):
            current_section = 'comment'
            in_block = True
            current_item = {}
            continue
        
        # End of a block
        if line == '}':
            if current_item:
                config_data[current_section].append(current_item)
            in_block = False
            current_section = None
            continue

        # Extract key-value pairs if inside a block
        if in_block:
            key_value_match = re.match(r'(\S+)\s+(.+)', line)
            if key_value_match:
                key, value = key_value_match.groups()
                current_item[key] = value.strip()  # Remove extra spaces

    return config_data

# Example usage
config_file_path =  sys.argv[1]
config_data = read_nagios_config(config_file_path)

# Convert to JSON format
config_json = json.dumps(config_data, indent=4)

# Print or save the JSON data
print(config_json)

# Optionally, write to a JSON file
with open(f'{sys.argv[1]}.json', 'w') as json_file:
    json_file.write(config_json)
