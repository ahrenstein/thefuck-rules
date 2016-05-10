def match(command):
    return ('ahrenstien' in command.script.lower() or 'arenstein' in command.script.lower())

def get_new_command(command):
    return command.script.replace("ahrenstien","ahrenstein").replace("arenstein","ahrenstein")

# Optional:
enabled_by_default = True
