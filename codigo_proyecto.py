# -*- coding: utf-8 -*-
"""codigo proyecto

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h7nTX61nWiFmVz-Qb7dYTl0flaIC8b8i
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(page_title="Análisis de Secuencias", layout="wide")
st.title("🔬 Análisis de Secuencias")
st.markdown("""Este dashboard permite analizar y visualizar datos relacionados con secuencias biológicas.
Utiliza los controles para interactuar con los datos.""")

st.sidebar.title("📂 Carga de Datos y Configuración")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo FASTA o CSV", type=["fasta", "csv"])

if uploaded_file:
    progress_bar = st.progress(0)
    status_text = st.empty()

    if uploaded_file.name.endswith(".fasta"):
        status_text.text("Cargando archivo FASTA...")
        progress_bar.progress(25)

        sequences = uploaded_file.getvalue().decode("utf-8").splitlines()
        sequences = [line.strip() for line in sequences if not line.startswith(">")]
        progress_bar.progress(75)

        st.sidebar.success("Archivo FASTA subido correctamente!")
        st.write(f"### Número de secuencias cargadas: {len(sequences)}")
        progress_bar.progress(100)
        status_text.text("Archivo FASTA procesado con éxito.")

    else:
        status_text.text("Cargando archivo CSV...")
        progress_bar.progress(25)

        data = pd.read_csv(uploaded_file)
        progress_bar.progress(50)

        st.sidebar.success("Archivo CSV subido correctamente!")
        st.write("### Vista Previa de los Datos")
        st.dataframe(data)
        progress_bar.progress(75)

        st.write("### Estadísticas Descriptivas")
        st.dataframe(data.describe())
        progress_bar.progress(100)
        status_text.text("Archivo CSV procesado con éxito.")

st.header("Indicadores Clave de Desempeño")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🔗 Precisión de alineación", value="95.3%")
with col2:
    st.metric(label="📊 Estructuras predecidas", value="128")
with col3:
    st.metric(label="🔍 Motivos encontrados", value="78")
with col4:
    st.metric(label="📈 Correlación estadística", value="0.87", delta="0.02")

st.header("Herramientas Interactivas")
selected_tool = st.radio("Elige una herramienta para analizar tus secuencias:",
                         options=["Alineación", "Predicción de estructuras", "Búsqueda de motivos", "Análisis estadístico"])

if selected_tool == "Alineación":
    st.subheader("Alineación de Secuencia")
    st.text("Ejemplo: Resultado del algoritmo Needleman-Wunsch")
    st.code("""
    Seq1: AGCTAGC
    Seq2: AGCTG-C
    Puntuación de alineación: 92
    """)
elif selected_tool == "Predicción de estructuras":
    st.subheader("Predicción de Estructuras Proteicas")
    st.text("Estructura 3D prevista (Placeholder):")
    st.image("https://via.placeholder.com/300", caption="Estructura 3D prevista")
elif selected_tool == "Búsqueda de motivos":
    st.subheader("Búsqueda de Motivos")
    st.text("Buscando motivos comunes en secuencia...")
    st.write("**Motivos encontrados:** ATG, TATA, CCGG")
elif selected_tool == "Análisis estadístico":
    st.subheader("Análisis de Correlación Estadística")
    data = {"Contenido": ["Contenido GC", "Contenido AT", "Longitud de la secuencia"],
            "Correlación con el objetivo": [0.87, -0.56, 0.45]}
    st.table(pd.DataFrame(data))

st.header("Visualizaciones")
tab1, tab2 = st.tabs(["Frecuencia del Motivo", "Distribución de Contenido GC"])

with tab1:
    motifs = ["ATG", "TATA", "CCGG"]
    frequencies = [25, 15, 10]
    fig = px.bar(x=motifs, y=frequencies, labels={'x': "Motivos", 'y': "Frecuencia"},
                 title="Frecuencia de Motivos", color_discrete_sequence=['violet'])
    st.plotly_chart(fig)

with tab2:
    lengths = np.random.normal(loc=1500, scale=300, size=100)
    fig = px.histogram(x=lengths, nbins=20, labels={'x': "Contenido GC (%)", 'y': "Frecuencia"},
                       title="Distribución de Contenido GC", color_discrete_sequence=['lightgreen'])
    st.plotly_chart(fig)

if uploaded_file and not uploaded_file.name.endswith(".fasta"):
    st.sidebar.markdown("---")
    st.sidebar.write("📥 Descarga de Resultados")
    csv = data.to_csv(index=False)
    st.sidebar.download_button(label="Descargar resultados", data=csv, file_name="resultados.csv", mime="text/csv")

st.sidebar.markdown("---")
st.sidebar.write("💻 Desarrollado por [Yoleth Barrios y Lucero Ramos]")