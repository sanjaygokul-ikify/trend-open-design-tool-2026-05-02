# Open Design Tool

import os
import json
from design_generator import generate_design

# Load configuration
try:
    with open('config.json') as f:
        config = json.load(f)
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
print('Exporting design...')
try:
    with open('design.html', 'w') as f:
        f.write(design)
except Exception as e:
    print(f'Failed to export design: {str(e)}')
    exit(1)

if __name__ == '__main__':
    # Run the Open Design Tool
    print('Running Open Design Tool...')
    # Start the design generation process
    try:
        design = generate_design(config)
        print(design)
    except Exception as e:
        print(f'Failed to generate design: {str(e)}')
        exit(1)
