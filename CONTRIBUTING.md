# 🤝 Contributing to Altair European Populations Map

Thank you for wanting to contribute to Altair European Populations Map

---

### 🐛 Bug Reports
If you find a bug, please create a new issue on GitHub. To help us fix it quickly, please include:

Steps to Reproduce: What exact code or commands did you run?

Expected vs. Actual Behavior: What did you think would happen, and what actually happened?

Environment: Your Python version and any relevant OS details.

Screenshots/Logs: If the visualization breaks, please provide a screenshot or any error messages from your terminal.

---

### 💡 Feature Requests
Have an idea to improve the mapping, add a new dataset, or enhance the dashboard? Open an issue and label it as a "Feature Request." We welcome discussions on the project roadmap!

---

### 💻 Pull Request Process
We encourage code contributions. Please follow these steps:

- Fork the Repo: Create your own copy of the repository.

- Create a Branch: Use a descriptive branch name (e.g., feature/add-time-slider or fix/js-injection-bug).

---

### Setup Environment: Ensure you have the requirements installed:

```Bash
pip install -r requirements.txt
```
- Follow Project Style: * This project values modularity. Keep logic in the appropriate file (e.g., map.py for orchestration, bar_chart.py for charts).

- Maintain clean, readable Python code.

- Test Your Changes: Run your changes locally to ensure the visualization generates correctly. If you've modified math or data processing, ensure you run any relevant tests.

- Submit: Open a Pull Request against the main branch.

---

### 🛠️ Development Guidelines
- JavaScript Injection: Please be careful when modifying inject_controls.py. This file handles the bridge between Altair's Vega-Lite output and the browser. Changes here may require manual testing in a browser to ensure the zoom/pan functionality still works.

- Modularization: When adding new charts or data sources, try to avoid bloating map.py. Create new modules or helper functions if a block of code becomes too large.

- Consistency: Ensure any new dependencies added to requirements.txt are necessary and stable.

---

Chat later 😊