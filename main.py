# Open Design Tool

import os
import json
from design_generator import generate_design
from typing import Dict

# Load configuration
try:
    with open('config.json') as f:
        config: Dict[str, str] = json.load(f)
except FileNotFoundError:
    print('Configuration file not found. Please ensure config.json exists in the current directory.')
    exit(1)
except json.JSONDecodeError as e:
    print(f'Invalid configuration file: {str(e)}')
    exit(1)

# Generate design
try:
    design = generate_design(config)
except Exception as e:
    print(f'Failed to generate design: {str(e)}')
    exit(1)

# Preview design
print('Previewing design...')
print(design)

# Export design
def export_design(design: str) -> None:
    try:
        with open('design.html', 'w') as f:
            f.write(design)
    except OSError as e:
        print(f'Failed to export design: {str(e)}')
        exit(1)

export_design(design)

if __name__ == '__main__':
    # Run the Open Design Tool
    print('Running Open Design Tool...')
    try:
        config: Dict[str, str] = json.load(open('config.json'))
        design = generate_design(config)
        print(design)
        export_design(design)
    except Exception as e:
        print(f'Failed to generate design: {str(e)}')
        exit(1)
