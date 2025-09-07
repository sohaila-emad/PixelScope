Contributing to PixelScope
Thank you for your interest in contributing to PixelScope! We welcome contributions from everyone.
🚀 Getting Started
Prerequisites

Python 3.8 or higher
Git
Basic knowledge of Python and image processing concepts

Development Setup

Fork the repository

Click the "Fork" button at the top right of the repository page
Clone your fork locally:

bashgit clone https://github.com/YOUR_USERNAME/PixelScope.git
cd PixelScope

Set up your development environment
bash# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy

Set up the upstream remote
bashgit remote add upstream https://github.com/sohaila-emad/PixelScope.git


🔄 Making Changes
Before You Start

Check existing issues to avoid duplicating work
Create an issue to discuss major changes
Keep changes focused and atomic

Development Workflow

Update your fork
bashgit checkout main
git fetch upstream
git merge upstream/main

Create a feature branch
bashgit checkout -b feature/your-feature-name

Make your changes

Write clean, readable code
Follow the existing code style
Add comments for complex logic
Update documentation if needed


Test your changes
bash# Run tests
python -m pytest

# Check code formatting
black --check .

# Check for linting issues
flake8 .

# Run type checking
mypy .

Commit your changes
bashgit add .
git commit -m "feat: add new feature description"
Use conventional commit messages:

feat: for new features
fix: for bug fixes
docs: for documentation changes
style: for formatting changes
refactor: for code refactoring
test: for adding tests
chore: for maintenance tasks


Push and create a Pull Request
bashgit push origin feature/your-feature-name
Then create a Pull Request on GitHub.

📝 Code Style Guidelines
Python Code Style

Follow PEP 8 standards
Use Black for code formatting: black .
Maximum line length: 88 characters
Use type hints where appropriate
Write descriptive docstrings for functions and classes

Example Function Format
pythondef calculate_snr(signal: np.ndarray, noise: np.ndarray) -> float:
    """Calculate Signal-to-Noise Ratio.
    
    Args:
        signal: The signal array
        noise: The noise array
    
    Returns:
        The calculated SNR value
    
    Raises:
        ValueError: If arrays have different shapes
    """
    if signal.shape != noise.shape:
        raise ValueError("Signal and noise arrays must have the same shape")
    
    return np.mean(signal) / np.std(noise)
GUI Code Guidelines

Use descriptive variable names for UI elements
Group related functionality in classes
Add tooltips for user interface elements
Handle exceptions gracefully with user-friendly messages

🧪 Testing
Writing Tests

Place tests in the tests/ directory
Name test files with test_ prefix
Write tests for new functionality
Include edge cases and error conditions

Running Tests
bash# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src

# Run specific test file
python -m pytest tests/test_image_processing.py
📚 Documentation
Updating Documentation

Update README.md for user-facing changes
Add docstrings to new functions and classes
Update inline comments for complex logic
Consider adding examples for new features

Documentation Style

Use clear, concise language
Include code examples where helpful
Keep documentation up-to-date with code changes

🐛 Reporting Issues
Bug Reports
Please include:

Description: Clear description of the bug
Steps to reproduce: Exact steps to trigger the issue
Expected behavior: What should have happened
Actual behavior: What actually happened
Environment: OS, Python version, dependencies
Screenshots: If applicable
Additional context: Any other relevant information

Feature Requests
Please include:

Description: Clear description of the desired feature
Use case: Why this feature would be useful
Proposed solution: How you think it should work
Alternatives: Other solutions you've considered

📋 Pull Request Process
Before Submitting

 Code follows the style guidelines
 Tests pass locally
 Documentation is updated
 Commit messages follow conventional format
 Changes are focused and atomic

Pull Request Template
markdown## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tests pass
- [ ] New tests added (if applicable)
- [ ] Manual testing performed

## Screenshots
(if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
🎯 Areas for Contribution
We especially welcome contributions in these areas:
🔧 Technical Improvements

Performance optimizations
Memory usage improvements
Code refactoring and cleanup
Error handling improvements

✨ New Features

Additional image processing filters
New analysis tools
Export format support
Batch processing capabilities

📖 Documentation

User tutorials and guides
API documentation
Code examples and demos
Translations

🧪 Testing

Unit tests for existing features
Integration tests
Performance benchmarks
Edge case testing

🤝 Community Guidelines
Be Respectful

Use welcoming and inclusive language
Respect different viewpoints and experiences
Accept constructive criticism gracefully
Focus on what's best for the community

Be Collaborative

Help others learn and grow
Share knowledge and resources
Provide constructive feedback
Celebrate contributions from others

📞 Getting Help

Documentation: Check the README and Wiki first
Issues: Search existing issues before creating new ones
Discussions: Use GitHub Discussions for questions and ideas
Code Review: Don't hesitate to ask for help in pull requests

🏆 Recognition
Contributors will be:

Listed in the project's contributors section
Mentioned in release notes for significant contributions
Welcomed to join as maintainers for consistent, high-quality contributions

Thank you for contributing to PixelScope! 🎉
