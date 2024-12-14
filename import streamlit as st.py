import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Title of the App
st.set_page_config(page_title="Streamlit Application", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["About Team", "Visualization of Graph", "City Graph of Java Province"])

# Page 1: About the Team
if selection == "About Team":
    st.title("About the Team")
    st.write("""
        Welcome to our Streamlit Application!
        We are a group of data scientists working on various data visualization projects.
        Our team consists of individuals passionate about machine learning, data analysis, and graph theory.
    """)

# Page 2: Visualization of Undirected or Directed Graph
elif selection == "Visualization of Graph":
    st.title("Visualization of Graph")
    st.write("""
        This page demonstrates the visualization of an undirected or directed graph.
    """)
    graph_type = st.radio("Select graph type", ["Undirected", "Directed"])

    # Create a simple graph for demonstration
    G = nx.Graph() if graph_type == "Undirected" else nx.DiGraph()

    # Add some nodes and edges
    G.add_nodes_from([1, 2, 3, 4])
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=16)
    st.pyplot(plt)

# Page 3: Graph of Cities in Java Province
elif selection == "City Graph of Java Province":
    st.title("City Graph of Java Province")
    st.write("""
        This page visualizes a simple graph representing cities in Java Province.
    """)

    # Cities in Java (example graph)
    cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang"]
    city_graph = nx.Graph()
    city_graph.add_nodes_from(cities)
    city_graph.add_edges_from([("Jakarta", "Bandung"), ("Jakarta", "Surabaya"), ("Bandung", "Yogyakarta"),
                               ("Yogyakarta", "Semarang")])

    # Plotting
    pos = nx.spring_layout(city_graph)
    plt.figure(figsize=(8, 6))
    nx.draw(city_graph, pos, with_labels=True, node_size=700, node_color="lightgreen", font_size=16)
    st.pyplot(plt)
