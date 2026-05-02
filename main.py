# Open Design Tool

import os
import json
from design_generator import generate_design

# Load configuration
with open('config.json') as f:
    config = json.load(f)

# Generate design
design = generate_design(config)

# Preview design
print('Previewing design...')
print(design)

# Export design
print('Exporting design...')
with open('design.html', 'w') as f:
    f.write(design)

if __name__ == '__main__':
    # Run the Open Design Tool
    print('Running Open Design Tool...')
    # Start the design generation process
    generate_design(config)
