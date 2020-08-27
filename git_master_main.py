def match(command):
    return ('error: pathspec \'master\' did not match any file(s) known to git' in command.output.lower())

def get_new_command(command):
    return command.script.replace("master","main")

# Optional:
priority = 5
enabled_by_default = True
