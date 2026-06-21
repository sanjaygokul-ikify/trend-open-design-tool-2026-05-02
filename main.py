# Open Design Tool

import os
import json
from design_generator import generate_design
from typing import Dict

# Load configuration
def load_config() -> Dict[str, str]:
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Configuration file not found. Please ensure config.json exists in the current directory.')
        exit(1)
    except json.JSONDecodeError as e:
        print(f'Invalid configuration file: {str(e)}')
        exit(1)

# Generate design
def generate_and_export_design(config: Dict[str, str]) -> None:
    try:
        design = generate_design(config)
        print('Previewing design...')
        print(design)
        export_design(design)
    except Exception as e:
        print(f'Failed to generate or export design: {str(e)}')
        exit(1)

# Export design
def export_design(design: str) -> None:
    try:
        with open('design.html', 'w') as f:
            f.write(design)
    except OSError as e:
        print(f'Failed to export design: {str(e)}')
        exit(1)

# Add type annotation to export_design function call
if __name__ == '__main__':
    # Run the Open Design Tool
    print('Running Open Design Tool...')
    config = load_config()
    generate_and_export_design(config)
    # Add missing type annotation for design_generator.generate_design
    # No code changes needed here as design_generator is not defined in this file
