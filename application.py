# Import necessary libraries
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Page 1: Team Description
def page_1():
    st.title("About the Team")
    st.write("""
    This project was created by a group of passionate developers focused on data visualization and graph theory.
    Our goal is to build an interactive web application to visualize different graph structures and geographical data.
    """)

# Page 2: Direct/Undirected Graph Visualization
def page_2():
    st.title("Graph Visualization")
    graph_type = st.radio("Choose Graph Type", ("Undirected", "Directed"))
    G = nx.Graph() if graph_type == "Undirected" else nx.DiGraph()

    # Add some nodes and edges (example)
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

    # Visualize the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    st.pyplot()

# Page 3: Cities in a Java Province Graph
def page_3():
    st.title("Graph of Cities in a Java Province")
    cities = {
        "Bandung": ["Jakarta", "Surabaya", "Yogyakarta"],
        "Jakarta": ["Bandung", "Surabaya"],
        "Surabaya": ["Bandung", "Jakarta", "Yogyakarta"],
        "Yogyakarta": ["Surabaya", "Bandung"]
    }
    G = nx.Graph()
    for city, neighbors in cities.items():
        for neighbor in neighbors:
            G.add_edge(city, neighbor)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="green")
    st.pyplot()

# Streamlit page configuration
pages = {
    "Team Description": page_1,
    "Graph Visualization": page_2,
    "Cities in Java Province": page_3,
}

# Navigation and page selection
page = st.sidebar.radio("Select a Page", list(pages.keys()))
pages[page]()
