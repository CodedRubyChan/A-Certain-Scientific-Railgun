init 999 python:
    if renpy.exists("debugmode.dbg"):
        config.developer = True
        config.console = True
    