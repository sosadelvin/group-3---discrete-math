pip install streamlit networkx pandas matplotlib
# Import pustaka yang diperlukan
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Halaman 1: Deskripsi Tim
def page_1():
    st.title("Tentang Tim")
    st.write("""
    Proyek ini dibuat oleh sekelompok pengembang yang bersemangat yang fokus pada visualisasi data dan teori graf.
    Tujuan kami adalah membangun aplikasi web interaktif untuk memvisualisasikan berbagai struktur graf dan data geografis.
    """)

# Halaman 2: Visualisasi Graf Direktif/Tidak Direktif
def page_2():
    st.title("Visualisasi Graf")
    graph_type = st.radio("Pilih Jenis Graf", ("Tidak Direktif", "Direktif"))
    G = nx.Graph() if graph_type == "Tidak Direktif" else nx.DiGraph()

    # Menambahkan beberapa simpul dan sisi (contoh)
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

    # Visualisasikan graf
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    st.pyplot()

# Halaman 3: Kota di Provinsi Jawa
def page_3():
    st.title("Graf Kota di Provinsi Jawa")
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

# Konfigurasi halaman Streamlit
pages = {
    "Deskripsi Tim": page_1,
    "Visualisasi Graf": page_2,
    "Kota di Provinsi Jawa": page_3,
}

# Navigasi dan pemilihan halaman
page = st.sidebar.radio("Pilih Halaman", list(pages.keys()))
pages[page]()
