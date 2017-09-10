from future.builtins import next

import os
import csv
import re
import logging
import optparse

import dedupe
from unidecode import unidecode

optp = optparse.OptionParser()
optp.add_option('-v', '--verbose', dest='verbose', action='count',
                help='Increase verbosity (specify multiple times for more)'
                )
(opts, args) = optp.parse_args()
log_level = logging.WARNING 
if opts.verbose:
    if opts.verbose == 1:
        log_level = logging.INFO
    elif opts.verbose >= 2:
        log_level = logging.DEBUG
logging.getLogger().setLevel(log_level)

input_file = 'csv_example_messy_input.csv'
output_file = 'csv_example_output.csv'
settings_file = 'csv_example_learned_settings'
training_file = 'csv_example_training.json'
