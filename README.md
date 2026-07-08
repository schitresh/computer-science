# Software Development

Visit [this](https://schitresh.github.io/notes-and-references) site to view notes & references on:

- Computer Science
  - Object Oriented Programming
  - Database System
  - Operating System
  - Computer Networks
- Development Tools
  - Git
  - Linux
  - Vim
  - VS Code
- Programming Languages
  - Python
  - Ruby
  - JavaScript
- Web Frameworks
  - Rails
  - React
  - SQL
- System Design
  - Design Concepts
  - Design Patterns
  - Website Designs

## Development

This repository contains an automated documentation site powered by **MkDocs** and the **Material theme**. The layout is built automatically based on your folder structure and numbers, completely removing the need to manage manual navigation links inside your configuration file.

### Environment Setup

Install `pipx` and `mkdocs` via terminal:

```bash
brew install pipx
pipx ensurepath
pipx install mkdocs
pipx inject mkdocs mkdocs-material mkdocs-gen-nav-plugin
```

### Development Server

1. **Start the Local Server**:

   ```bash
   mkdocs serve
   ```

2. **Preview Your Work**:

   Open your web browser and go to:

   ```text
   http://localhost:8000
   ```

3. **Clear Cache & Restart**:

   If changes or new pages do not show up properly, stop the server (`Ctrl + C`) and run a clean reset:

   ```bash
   mkdocs build --clean
   ```

### Deployment

To regenerate the indexes for new content, run:

```bash
mkdocs build --clean
```

Publish updates directly to your GitHub repository hosting branch with one command:

```bash
mkdocs gh-deploy --clean
```
