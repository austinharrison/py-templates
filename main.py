import logging
import yaml
import os

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create logs folder if it doesn't exist
os.makedirs('./logs/', exist_ok=True)
# create file handler which logs even debug messages
fh = logging.FileHandler('./logs/logs.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('Logging started')

# create example creds.yml if one doesn't exist
if not os.path.isfile('./creds/creds.yml'):
    # create creds dirs
    os.makedirs('./creds/', exist_ok=True)
    with open('./creds/creds.yml', 'w') as f:
        f.write("example:\n  username: username\n  password: password\n")

with open('./creds/creds.yml') as f:
    CREDS = yaml.safe_load(f)


def main():
    logger.info('example username:' + CREDS['example']['username'])


if __name__ == "__main__":
    main()
