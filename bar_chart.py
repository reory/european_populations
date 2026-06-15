import altair as alt
import pandas as pd


def get_bar_chart(n: int = 10) -> alt.LayerChart:
    """
    Returns an Altair horizontal bar chart showing the top-N European
    countries by population, styled to match the map.
    """

    # Load & clean — same logic as map.py so both always use identical data
    df = pd.read_csv("country_data.csv")
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=["id", "population", "name"])
    df["id"] = df["id"].astype(int)
    df["population"] = pd.to_numeric(df["population"], errors="coerce")
    df = df.dropna(subset=["population"])

    # Keep only the top-N rows
    top_n = df.nlargest(n, "population").reset_index(drop=True)

    # Chart Shared y-axis sort so bars run largest → smallest (top to bottom)
    y_sort = alt.Sort(field="population", order="descending")

    # Base bar chat
    bars = (
        alt.Chart(top_n)
        .mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4,
        )
        .encode(
            y=alt.Y(
                "name:N",
                sort=y_sort,
                title=None,
                axis=alt.Axis(labelColor="#333333", labelFontSize=12),
            ),
            x=alt.X(
                "population:Q",
                title="Population",
                axis=alt.Axis(
                    format="~s",  # e.g. 80M
                    labelColor="#333333",
                    titleColor="#333333",
                    grid=True,
                    gridColor="#ffffff55",
                ),
            ),
            color=alt.Color(
                "population:Q",
                scale=alt.Scale(scheme="tealblues"),
                legend=None,  # legend already lives on the map
            ),
            tooltip=[
                # show country name as a nominal tooltip
                alt.Tooltip("name:N", title="Country"),
                alt.Tooltip("population:Q", title="Population", format=","),
            ],
        )
    )

    # Value labels at the end of each bar
    labels = (
        alt.Chart(top_n)
        .mark_text(
            align="left",
            dx=4,
            fontSize=11,
            color="#333333",
        )
        .encode(
            y=alt.Y("name:N", sort=y_sort),
            x=alt.X("population:Q"),
            text=alt.Text("population:Q", format="~s"),
        )
    )
    # Final combined chart
    chart = (bars + labels).properties(
        width=340,
        height=550,
        title=f"Top {n} Countries by Population",
    )

    return chart
