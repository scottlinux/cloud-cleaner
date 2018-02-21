from cloud_cleaner.config import CloudCleanerConfig
from cloud_cleaner.resources import all_resources

import sys


def main(args=sys.argv):
    config = CloudCleanerConfig(args=args)
    for Resource in all_resources:
        Resource(config)
