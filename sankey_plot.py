import plotly.graph_objects as go
from collections import Counter

def categorize_price(price, bins):
    """Dynamically categorize a price into a bin based on user-defined bin edges."""
    for i, threshold in enumerate(bins):
        if price < threshold:
            return i  # Assign to the corresponding bin
    return len(bins)  # Assign to the highest bin if greater than all thresholds


def generate_flows(model, asset_name, times, bins):
    """Generates the flow matrix from simulated paths and bin classifications."""
    num_paths = model.dataset["MC"]["PATHS"]
    flows = Counter()

    # Generate asset paths and categorize them into bins
    model.reset()
    for t_idx, t in enumerate(times):
        model.advance(t)
        prices = model.get_value(asset_name)
        categories = [categorize_price(price, bins) for price in prices]

        if t_idx > 0:
            for prev, curr in zip(prev_categories, categories):
                flows[(t_idx - 1, prev, t_idx, curr)] += 1

        prev_categories = categories

    return flows


def plot_sankey(model, asset_name, times, bins):
    """Generates and plots a Sankey diagram based on price path transitions."""
    flows = generate_flows(model, asset_name, times, bins)

    # Find the unique coordinates
    unique_coords = set()
    for t1, b1, t2, b2 in flows.keys():
        unique_coords.add((t1, b1))
        unique_coords.add((t2, b2))
    unique_coords = list(unique_coords)

    # Create a dictionary to map coordinates to indices, and transform the flows into source/target/value lists
    coords_dict = {coord: i for i, coord in enumerate(unique_coords)}
    sources, targets, values = [], [], []
    for (t1, b1, t2, b2), count in flows.items():
        sources.append(coords_dict[(t1, b1)])
        targets.append(coords_dict[(t2, b2)])
        values.append(count)

    # Create labels, x and y positions for nodes
    bin_len = len(bins)

    def label_fn(t, b):
        if b == bin_len:
            return f"S>{bins[-1]:.0f}"
        if b == 0:
            return f"S<{bins[0]:.0f}"
        else:
            return f"{bins[b-1]:.0f}-{bins[b]:.0f}"

    labels = [label_fn(t, b) for (t, b) in unique_coords]
    x = [times[t] for (t, b) in unique_coords]
    y = [1 - b * 0.4 for (t, b) in unique_coords]

    # Plot Sankey diagram
    fig = go.Figure(
        go.Sankey(
            node=dict(
                label=labels,
                x=x,  # Explicitly set x positions
                y=y,  # Explicitly set y positions
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
            ),
        )
    )

    # Annotate the time steps
    for t in times:
        fig.add_annotation(x=t, y=1.0, showarrow=True, text=f"t={t:.1f}")

    fig.update_layout(title_text="SPX Price Transitions", font_size=10, width=800, height=400)
    fig.show()
