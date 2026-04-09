# file name: app.py
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoNav-AI", layout="wide")
st.title("🌱 EcoNav-AI: Green Route Planner")

# Sidebar
st.sidebar.header("Navigation Settings")
origin = st.sidebar.text_input("Enter Origin:", "Point A")
destination = st.sidebar.text_input("Enter Destination:", "Point B")
show_graph = st.sidebar.checkbox("Show Graph Visualization", True)

# Graph creation (example)
G = nx.Graph()
G.add_edges_from([
    ("Point A", "Point B", {"weight": 5}),
    ("Point A", "Point C", {"weight": 2}),
    ("Point B", "Point C", {"weight": 1}),
    ("Point B", "Point D", {"weight": 2}),
    ("Point C", "Point D", {"weight": 3}),
])

# Compute shortest path
try:
    path = nx.shortest_path(G, source=origin, target=destination, weight="weight")
    st.success(f"Optimal Route: {' → '.join(path)}")
except nx.NetworkXNoPath:
    st.error("No path found between the selected points.")

# Show graph
if show_graph:
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)

# Optional: Add more inputs for eco-friendly preferences
eco_mode = st.sidebar.checkbox("Eco-Friendly Route Mode", False)
if eco_mode:
    st.info("Eco mode active: prioritizing less CO2 emissions routes.")

st.sidebar.markdown("---")
st.sidebar.markdown("Developed by EcoNav-AI Team 🌿")