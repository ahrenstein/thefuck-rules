def match(command):
    return ('roto: command not found' in command.output.lower())

def get_new_command(command):
    return command.script.replace("roto","root")

# Optional:
priority = 5
enabled_by_default = True
