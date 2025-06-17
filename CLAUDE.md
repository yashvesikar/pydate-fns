# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pydate-fns is a Python port of the JavaScript date-fns library, providing a sensible collection of date manipulation functions. The library follows a modular architecture where each function is in its own directory with its implementation and tests.

## Architecture

### Module Structure
Each date function follows this structure:
```
pydate/function_name/
├── __init__.py      # Exports the function
├── function_name.py # Implementation
└── test.py          # Tests
```

### Key Design Principles
1. **DateTime Compatibility**: All functions accept both datetime objects and timestamps (float/int)
2. **NaN Handling**: Functions gracefully handle NaN values, returning NaN for comparisons
3. **UTC Consistency**: Timestamps are treated as UTC for consistency
4. **Python Conventions**: Maintains Python conventions (e.g., months 1-12) while implementing JavaScript logic

## Common Commands

### Testing
```bash
# Run all tests with coverage
make test

# Run tests directly with pytest
pytest --cov=pydate --cov-append --cov-report=lcov

# Run a specific test file
pytest pydate/function_name/test.py
```

### Development Tools
```bash
# Create a new function module
make create-module module=function_name

# Update README.md with function list
make update-readme

# Format code with black (line length 150)
black --line-length 150 pydate/

# Sort imports
isort --profile black pydate/
```

### Linting and Type Checking
The project uses:
- Black for code formatting (line length: 150)
- isort with Black profile for import sorting

## Adding New Functions

1. Use the module creation script:
   ```bash
   make create-module module=new_function
   ```

2. Implement the function following existing patterns:
   - Handle both datetime and timestamp inputs
   - Include comprehensive tests matching JavaScript implementation
   - Follow naming conventions from date-fns

3. Add export to `pydate/__init__.py`

4. Run tests to ensure everything works

## Testing Strategy

- Each function has its own `test.py` file
- Tests should cover edge cases (NaN, invalid dates, timezone transitions)
- Use pytest for all testing
- Aim for comprehensive coverage matching the JavaScript implementation