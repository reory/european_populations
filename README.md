# Altair European Populations Map

![Last Commit](https://img.shields.io/github/last-commit/reory/european_populations?cacheSeconds=60)
![Repo Size](https://img.shields.io/github/repo-size/reory/european_populations?cacheSeconds=60)
![License](https://img.shields.io/badge/License-MIT-green)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Altair](https://img.shields.io/badge/Altair-FF7A00?style=for-the-badge&logo=vega&logoColor=white)
![vega-datasets](https://img.shields.io/badge/vega--datasets-007EC6?style=for-the-badge&logo=vega&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A modular Python visualization project that renders an interactive population map of Europe alongside a statistical breakdown of country populations. This project overcomes standard Altair limitations regarding geo-projection interactivity by utilizing a custom JavaScript injection bridge.

---

## 📸 Screenshots
Main Image of Europe and populations of cities and countries.
![](screenshots/altair%20map%20of%20europe.png)

---

## 🚀 Features

- Interactive Mapping: A Mercator-projected map of Europe that supports scroll-to-zoom and click-and-drag panning.

- Synchronized Analytics: An automated side-by-side bar chart displaying the top-N countries by population, maintaining visual consistency with the main map.

- Modular Architecture: Clean separation of concerns with dedicated modules for data storage, chart generation, and control injection.

- Custom Control Layer: Uses a targeted `JavaScript` workaround to bypass standard Vega-Lite limitations, ensuring smooth mouse controls in generated HTML.

---

## 📂 Project Structure

```python
├── map.py             # Entry point: CLI interface and workflow orchestration
├── bar_chart.py       # Handles the generation of the stats bar chart
├── data_store.py      # Contains cities_data dictionary used for the city-layers
├── inject_controls.py # The js engine for the interactivity.
│                      # It post-processes the generated HTML to wire up zoom/pan  
├                      # event listeners.
├── country_data.csv   # The dataset for country populations and geographic IDs
└── requirements.tx    # Project dependencies
└── tests/             # Test suite
      └── test_bar_chart.py
      └── test_data_store.py
      └── test_inject_controls.py
```

--- 

## 🛠️ Installation
- Clone the repository.

- Install the required dependencies:

```python
pip install -r requirements.txt
```
### 📈 Usage
To generate the map and interactive visualizations, run the main script:

```python
python map.py
```
- This will generate map_europe.html in your root directory. Open this file in any modern web browser to interact with the map.

---

## 💡 Technical Implementation Notes

This project implements several workarounds to handle limitations in the standard `Altair`/`Vega-Lite` stack:

- Interactivity Workaround: `Altair` does not natively support .interactive() on geo projections. This project bypasses this by defining signals (zoom_scale, pan_x, pan_y) and injecting a custom `JavaScript` bridge (inject_controls.py) that manipulates these signals via the Vega view API.

- Rendering Fixes: The project correctly identifies that vega-embed 7 renders SVG by default rather than Canvas. The control injection logic targets the #vis container div, ensuring event listeners function regardless of the renderer.

- Data Integrity: Both the map and the bar chart share the same data cleaning pipeline to ensure population statistics remain identical across all visualizations.

---

## 📊 Tech Stack

- `Altair`: A declarative statistical visualization library used to create interactive charts based on the Vega-Lite grammar.

- `Pandas`: A comprehensive library for data manipulation and analysis, centered around the DataFrame structure for handling tabular data.

- `Vega-Datasets`: A collection of ready-to-use sample datasets specifically designed for testing and prototyping data visualization projects.

- `Numpy`: The fundamental library for scientific computing, providing powerful N-dimensional array objects and a vast collection of high-performance mathematical functions.

- `JavaScript`: A versatile programming language used here to inject custom event listeners into the generated HTML, enabling interactive features like zoom and pan that are not natively supported by Altair.

---

## 🛣️ Roadmap Features

- [ ] Integrate a public API (such as the World Bank or Eurostat) to replace your static country_data.csv, enabling the map to reflect real-time or updated population statistics automatically.

- [ ] Add a temporal dimension to your schema, allowing users to scrub through a timeline slider to visualize population growth and shifts across decades, rather than viewing a static snapshot.

- [ ] Transition from generating a standalone HTML file to deploying as a dynamic dashboard (using `Flet`, `Streamlit` or `Flask`), which would allow for real-time UI filtering and interactive parameter tuning without needing to re-run the script.

---

* **Built by Roy Peters** 😊
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Roy%20Peters-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roy-p-74980b382/)