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
except json.JSONDecodeError:
    print('Invalid configuration file. Please ensure config.json contains valid JSON.')
    exit(1)

# Generate design
design = generate_design(config)

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
    generate_design(config)