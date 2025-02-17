# **Contributing Guidelines**

We welcome contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help is greatly appreciated. This guide will walk you through the process of contributing to this project.

---

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Code Contributions](#code-contributions)
3. [Pull Request Guidelines](#pull-request-guidelines)
4. [Code Style and Standards](#code-style-and-standards)
5. [Labeling Guidelines](#labeling-guidelines)
6. [Community Guidelines](#community-guidelines)

---

## **Getting Started**
Before contributing, please:
1. **Fork the repository** and clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/gap-pattern-detection.git
   cd gap-pattern-detection
   ```
2. Set up the development environment (see Setting Up the Development Environment).
3. Familiarize yourself with the project structure and codebase.

## **How to Contribute**

### Reporting Bugs
If you find a bug, please:
1. Check if the issue has already been reported in the Issues section.
2. If not, open a new issue and provide:
   - A clear and descriptive title.
   - Steps to reproduce the bug.
   - Expected vs. actual behavior.
   - Screenshots or error logs (if applicable).

### Suggesting Enhancements
If you have an idea for a new feature or improvement:
1. Check if the enhancement has already been suggested.
2. Open a new issue and describe:
   - The problem or limitation you’re addressing.
   - Your proposed solution.
   - Any relevant examples or references.

### Code Contributions
To contribute code:
1. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and test them thoroughly.
3. Commit your changes with a clear and descriptive message:

   ```bash
   git commit -m "Add your message here"
   ```
4. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request (PR)** on the main repository.

## Pull Request Guidelines

- **Keep PRs Small**: Focus on one feature or bugfix per PR.
- **Describe Your Changes**: Provide a clear description of what your PR does and why it’s needed.
- **Include Tests**: If applicable, add tests to verify your changes.
- **Update Documentation**: Ensure the README.md and other documentation are updated if your changes affect them.

## Code Style and Standards

- Follow **PEP 8** guidelines for Python code.
- Use descriptive variable and function names.
- Add comments to explain complex logic.

## Labeling Guidelines

If you’re labeling new data for the dataset, follow these guidelines:

- Use a labeling tool like LabelImg or CVAT.
- For each GAP UP or GAP DOWN pattern:
  - Draw a bounding box around the two candlesticks involved in the pattern.
  - Assign the correct class label (0 for GAP DOWN, 1 for GAP UP).
- Ensure the bounding boxes are tight and accurate.

## Community Guidelines

- Be respectful and inclusive.
- Provide constructive feedback.

Thank You!
Your contributions help make this project better for everyone. We appreciate your time and effort! 🚀
