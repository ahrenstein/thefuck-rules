def match(command):
    return ('cd //' in command.script.lower())

def get_new_command(command):
    return command.script.replace("cd //","cd - && cd ../")

# Optional:
priority = 5
enabled_by_default = True
