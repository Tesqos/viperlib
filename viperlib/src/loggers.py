def loggers_set_level(mode, *args):
        for each in args:
            each.setLevel(mode)
