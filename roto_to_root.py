def match(command):
    return ('roto: command not found' in command.stderr.lower())

def get_new_command(command):
    return command.script.replace("roto","root")

# Optional:
enabled_by_default = True
