def match(command):
    return ('lcok: command not found' in command.output.lower())

def get_new_command(command):
    return command.script.replace("lcok","lock")

# Optional:
priority = 5
enabled_by_default = True
