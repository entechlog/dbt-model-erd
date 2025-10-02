# 📊 dbt-erd

> Generate beautiful entity-relationship diagrams for your dbt models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/dbt-erd.svg)](https://badge.fury.io/py/dbt-erd)

## ✨ Features

- 🖼️ **Visual Clarity**: Generate clean, professional ER diagrams for your data warehouse
- 🔄 **Auto-Detection**: Automatically detects relationships between fact and dimension tables
- 📝 **Documentation**: Embeds diagrams directly in your dbt model documentation
- 🧠 **Smart Inference**: Intelligently infers primary keys, foreign keys, and column types
- 🛠️ **Highly Configurable**: Customize every aspect of your diagrams
- 🔒 **No External Dependencies**: Renders diagrams client-side without requiring Node.js
- 🏎️ **CI/CD Friendly**: Works seamlessly in continuous integration environments

## 🚀 Installation

```bash
pip install dbt-erd
```

## 📋 Usage

```bash
# Generate diagrams for fact models
python -m dbt_erd --model-path models/dw/fact

# With custom configuration
python -m dbt_erd --model-path models/dw/fact --config advanced_config.yml

# Create a default configuration file
python -m dbt_erd --output-config my_config.yml

# Process models in parallel
python -m dbt_erd --model-path models/dw/fact --parallel

# Enable verbose mode for debugging
python -m dbt_erd --model-path models/dw/fact --verbose
```

## 📄 Configuration

Two sample configuration files are included: `basic_config.yml` and `advanced_config.yml`.

### Basic Configuration

```yaml
# Visualization settings
visualization:
  max_dimensions: 10
  show_columns: true
  column_limit: 20

# Mermaid settings
mermaid:
  theme: "default"
  direction: "LR"
  outputs:
    mmd: true   # Generate raw Mermaid source code
    html: true  # Generate HTML with client-side rendering
  interactive: true
  
  # Table styling options
  style:
    fact_table_fill: "#f5f5f5"       # Light gray for fact tables
    dimension_table_fill: "#e8f4f8"  # Light blue for dimension tables
```

### Advanced Configuration

```yaml
# Visualization settings
visualization:
  max_dimensions: 20
  show_columns: true
  column_limit: 75

# Advanced Mermaid settings
mermaid:
  theme: "neutral"
  direction: "LR"
  outputs:
    mmd: true
    html: true
  
  # Table styling options
  style:
    fact_table_fill: "#f9f4de"       # Light yellow for fact tables
    dimension_table_fill: "#e4f1f7"  # Light blue for dimension tables
    
  # Embedding options for dbt docs
  embed:
    type: "html"  # Embed HTML links in dbt docs
```

## 🖼️ How It Works

### Pure Browser-Based Rendering

dbt-erd generates diagrams without requiring Node.js or making external API calls:

1. **Mermaid Source Code (.mmd)**: The raw diagram definition
2. **HTML with Client-Side Rendering (.html)**: Interactive diagram rendered in the browser

When embedded in dbt docs, you get HTML links to interactive diagrams.

### Customizable Table Styling

You can customize the appearance of your diagrams:

- Set different colors for fact and dimension tables
- Choose from different themes (default, neutral, forest, dark)
- Set diagram direction (LR or TB)

### Diagram Generation Process

1. Analyzes SQL files to find fact and dimension tables based on naming patterns
2. Detects relationships between tables by identifying foreign keys
3. Generates Mermaid diagram code representing these relationships
4. Creates HTML files that render the diagrams client-side
5. Updates your model YAML files to include links to the diagrams in dbt docs

## 📦 CI/CD Integration

This package is designed for CI/CD environments and works without Node.js or external API calls.

Example GitHub Actions workflow:

```yaml
name: Update ERD Diagrams

on:
  push:
    branches: [ main ]
    paths:
      - 'models/**/*.sql'
      - 'models/**/*.yml'

jobs:
  update-diagrams:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          pip install dbt-erd
      - name: Generate ERD diagrams
        run: |
          python -m dbt_erd --model-path models/dw/fact --config ci_config.yml
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add assets/
          git commit -m "Update ERD diagrams" || echo "No changes to commit"
          git push
```

## 📚 Documentation

View the embedded diagrams in your dbt docs by running:

```bash
dbt docs serve
```

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.