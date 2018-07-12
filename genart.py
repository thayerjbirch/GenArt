import sys
import os
import json
import logging as log
import sources
from pathlib import Path
from painter import Painter

def parse_args(argv):
    if len(argv) < 2:
        raise Exception("Not enough arguments")

    args = dict()
    args["conf"] = argv[0]
    args["output"] = Path(argv[1])

    return args

def configure_logging(args):
    #todo verbose/is a terminal stuff stuff
    #global verbose
    #verbose = args.verbose
    if 'logging' in args:
        for path in args.logging:
            logging.config.fileConfig(str(path), disable_existing_loggers=False)
    #if sys.stderr.isatty():
    level = log.INFO
    fmt = '%(asctime)s %(module)s %(levelname)s %(message)s'
    handler = log.StreamHandler()
    handler.setFormatter(log.Formatter(fmt))
    logger = log.getLogger()
    logger.setLevel(level)
    logger.addHandler(handler)

def parse_config(conf_path):
    with open(conf_path, 'r') as conf:
        settings = dict()
        contents = json.loads(conf.read())
        return contents

def main(argv):
    args = parse_args(argv)
    configure_logging(args)
    settings = parse_config(args["conf"])
    log.info("Starting process")
    #painter = Painter(settings)

if __name__ == '__main__':
    main(sys.argv[1:])
