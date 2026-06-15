import altair as alt
import pandas as pd
from vega_datasets import data
from bar_chart import get_bar_chart
from inject_controls import inject_mouse_controls
from data_store import cities_data
from loguru import logger

# Load Data Sources
countries_geo = alt.topo_feature(data.world_110m.url, "countries")
df = pd.read_csv("country_data.csv")

# Clean Country Data
df.columns = df.columns.str.strip()
df = df.dropna(subset=["id"])
df["id"] = df["id"].astype(int)
df = df.reset_index(drop=True)

# Define Interactions & Signals
hover = alt.selection_point(on="mouseover", nearest=False, fields=["id"], empty=False)

# Zoom / pan params for the JS workaround
zoom_param = alt.param(name="zoom_scale", value=420)
pan_x_param = alt.param(name="pan_x", value=325)
pan_y_param = alt.param(name="pan_y", value=650)

# Define Individual Layers
# The Base Map (Countries)
map_chart = (
    alt.Chart(countries_geo)
    .mark_geoshape(stroke="#080707", strokeWidth=0.8)
    .encode(
        color=alt.condition(
            hover,
            alt.value("#ff9900"),
            alt.Color(
                "population:Q",
                scale=alt.Scale(scheme="tealblues"),
                legend=alt.Legend(title="Total Population"),
            ),
        ),
        tooltip=[
            alt.Tooltip("name:N", title="Country"),
            alt.Tooltip("population:Q", title="Population", format=","),
            alt.Tooltip("display_note:N", title=" "),
        ],
    )
    .transform_lookup(
        lookup="id",
        from_=alt.LookupData(df, "id", ["name", "population", "note"]),
    )
    .transform_calculate(
        display_note="datum.name == 'United Kingdom' ? datum.note : ''"
    )
)

# Load the DataFrame from the imported list
cities_df = pd.DataFrame(cities_data)

# Updated Cities Chart (Local Data)
cities_chart = (
    alt.Chart(cities_df)
    .mark_circle(color="white", stroke="#080707", strokeWidth=0.3, opacity=0.9)
    .encode(
        longitude="lng:Q",
        latitude="lat:Q",
        size=alt.Size(
            "pop:Q",
            scale=alt.Scale(range=[20, 500]),
            legend=alt.Legend(title="City Population", format="~s"),
        ),
        tooltip=[
            alt.Tooltip("name:N", title="City"),
            alt.Tooltip("pop:Q", title="Population", format=","),
        ],
    )
)

# Keep existing instruction label
instruction_label = (
    alt.Chart(pd.DataFrame({"text": ["Scroll to zoom  ·  Click & drag to pan"]}))
    .mark_text(
        align="left",
        baseline="bottom",
        fontSize=13,
        fontWeight="bold",
        fontStyle="italic",
        dx=-530,
        dy=290,
        color="#333333",
    )
    .encode(text="text:N")
)

# Assembly
# Combine geographic layers into one "camera" view
layered_map = (
    (map_chart + cities_chart + instruction_label)
    .add_params(
        hover,
        zoom_param,
        pan_x_param,
        pan_y_param,
    )
    .project(
        type="mercator",
        scale=alt.expr("zoom_scale"),
        translate=alt.expr("[pan_x, pan_y]"),
    )
    .properties(width=650, height=550, title="2026 Population Map of Europe")
)

# Get the bar chart from the other file
bar_chart = get_bar_chart(n=10)

# Combine Map and Bar Chart side-by-side
combined = alt.hconcat(layered_map, bar_chart, spacing=30)

# Global Configuration & Saving
final_output = (
    combined.configure(background="#7eadf5")
    .configure_view(stroke=None)
    .configure_legend(
        titleColor="black",
        labelColor="black",
        orient="bottom-right",
        padding=10,
        fillColor="#ffffffaa",
    )
    .configure_title(color="black", fontSize=18, anchor="start")
)

# Save and Run the JS Workaround
final_output.save("map_europe.html")
inject_mouse_controls("map_europe.html")
logger.info(
    "Map + chart created successfully with mouse zoom/pan! Check map_europe.html."
)
