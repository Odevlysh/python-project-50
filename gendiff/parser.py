import json
import yaml


def parse(file_path):
    with open(file_path, 'r') as f:
        if file_path.endswith('.json'):
            return json.load(f)
        elif file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {file_path}')
