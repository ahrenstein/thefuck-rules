def match(command):
    return ('lcok: command not found' in command.stderr.lower())

def get_new_command(command):
    return command.script.replace("lcok","lock")

# Optional:
enabled_by_default = True
