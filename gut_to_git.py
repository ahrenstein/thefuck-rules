def match(command):
    return ('gut: command not found' in command.stderr.lower())

def get_new_command(command):
    return command.script.replace("gut ","git ")

# Optional:
enabled_by_default = True
