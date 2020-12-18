from lib.collector import InfoCollector
import json
import logging

# Initialize object
info_collector = InfoCollector("10.2196/12121")

# Collect and output info
if info_collector.collect_info():
    json_object = [
        info_collector.toJSON(),
    ]

    print(json.dumps(json_object, indent=4))

# Log error
else:
    logging.error(
        "ERROR: Most likely rate limited or check your internet connections")
