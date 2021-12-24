# ready-python-config
Simple config module ready to use.

## Setup

```shell
pip install git+https://github.com/alejandroperezcosio/ready-python-config.git
```

## Usage
With a directory structure like this:
```bash
~/apps/<project_name>/config/
~/apps/<project_name>/config/default.json
~/apps/<project_name>/config/production.json
~/apps/<project_name>/config/production-customer1.json
~/apps/<project_name>/config/production-customer2.json
~/apps/<project_name>/config/production-customer3.json
```

```bash
python app.py -env=production -c=customer2
```

```python
from rpyconfig import config

print config.* # This is an object
```
