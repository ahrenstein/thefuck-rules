def match(command):
    return ('gut: command not found' in command.stderr.lower())

def get_new_command(command):
    return command.script.replace("gut ","git ")

# Optional:
priority = 5
enabled_by_default = True
