# Open Design Tool

import os
import json
from design_generator import generate_design
from typing import Dict, Callable

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
        export_design_refactored(design)
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

# Define type annotation for generate_design function
generate_design: Callable[[Dict[str, str]], str] = generate_design

def export_design_error_handler(e: Exception) -> None:
    print(f'Error exporting design: {str(e)}')

# Refactored export_design function with better error handling
def export_design_refactored(design: str) -> None:
    try:
        with open('design.html', 'w') as f:
            f.write(design)
    except OSError as e:
        export_design_error_handler(e)

# Refactored generate_and_export_design function with better error handling
def generate_and_export_design_refactored(config: Dict[str, str]) -> None:
    try:
        design = generate_design(config)
        print('Previewing design...')
        print(design)
        export_design_refactored(design)
    except Exception as e:
        print(f'Failed to generate or export design: {str(e)}')

if __name__ == '__main__':
    # Run the Open Design Tool
    print('Running Open Design Tool...')
    config = load_config()
    generate_and_export_design(config)
