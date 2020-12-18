# Info Collector

Library is in `lib/collector.py`

## Requirements
- `requests`
- (optional) `pipenv`

### Setup
```bash
git clone <repourl>
```
```python
pip3 install requests

# Or via pipenv with other other dependancies
pip3 install pipenv
pipenv --python 3
pipenv shell
pipenv install
```

Example
```python
# Import
from lib.collector import InfoCollector

# Initialize object
info_collector = InfoCollector("10.2196/12121")

# Collect info
info_collector.collect_info()

# Output info
print(json.dumps(json_object, indent=4))
```

or run the example

```bash
python3 example.py
```