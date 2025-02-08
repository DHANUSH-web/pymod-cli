"""
    *************************************************************************
    Copyright (c) 2025 Dhanush H V. All rights reserved.
    Licensed under the MIT License. See the LICENSE file for more details.
    *************************************************************************
"""


import json
import os


# Show all the available templates
def show_templates() -> None:
    # TODO: Implement this method
    ...


# Show developer info
def show_developer_info(template: str) -> None:
    # TODO: Implement this method
    ...


# Get virtual environment
def get_virtual_environment(template: str) -> str:
    if not os.path.exists(f"templates/{template}.json"):
        raise FileNotFoundError(f"Template {template} not found. Please add this template to templates folder.")

    with open(f"templates/{template}.json", "r") as file:
        data = json.load(file)
        return data.get("venv", ".venv")


# Create virtual environment
def create_virtual_environment(template: str) -> None:
    # TODO: Implement this method
    ...
