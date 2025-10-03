#!/usr/bin/env python
"""dbt-erd: Generate entity-relationship diagrams for dbt models

This package provides tools to generate Mermaid entity-relationship diagrams
for dbt models based on naming standards and SQL references.
"""

__version__ = "0.1.0"

from .config import load_config, save_default_config
from .dbt_erd import main as _main
from .mermaid_renderer import generate_html_with_mermaid, save_mermaid_outputs


def main():
    """Entry point for the application."""
    return _main()


if __name__ == "__main__":
    main()
