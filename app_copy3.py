import plotly.graph_objects as go
import numpy as np
import os

# Check for kaleido package
try:
    import kaleido
except ImportError:
    raise ImportError("You need to install kaleido to export images with Plotly.")

# Create images directory if it doesn't exist
if not os.path.exists("images"):
    os.mkdir("images")

np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

# Commented out to prevent hanging in certain environments
# fig.show()

# Save the figure
#fig.write_image("images/fig1.pdf")
fig.write_image("images/fig1.pdf", format='pdf')