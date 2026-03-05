
# LIBRERÍAS --------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Configuración inicial (debe ir antes de cualquier st.*)
st.set_page_config(layout="wide")


# MENÚ LATERAL --------------------------------------------------
st.sidebar.title("☎️ SISTEMA TELCO")

opcion = st.sidebar.selectbox(
    "-------------------",
    ["🛖 Home", "✨ Dataset", "✅ Conclusiones"])


# CLASE (POO) --------------------------------------------
class Analyzer:

    def __init__(self, df):
        self.df = df

    def info_general(self):
        df_types = pd.DataFrame({
            "Variable": self.df.columns,
            "Tipo de Dato": self.df.dtypes.values
        })
        return df_types

    def valores_nulos(self):
        df_nulls = pd.DataFrame({
            "Variable": self.df.columns,
            "Valores Nulos": self.df.isnull().sum().values
        })
        return df_nulls

    def clasificar_variables(self):
        numericas = self.df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        categoricas = self.df.select_dtypes(include=["string"]).columns.tolist()
        return numericas, categoricas

    def estadisticas(self):
        return self.df.describe()

    def media(self, col):
        return self.df[col].mean()

    def mediana(self, col):
        return self.df[col].median()

    def moda(self, col):
        return self.df[col].mode()[0]
    
    def rango(self, col):
        return self.df[col].max() - self.df[col].min()

    def varianza(self, col):
        return self.df[col].var(ddof=1)

    def desviacion_estandar(self, col):
        return self.df[col].std(ddof=1)

    def desviacion_media(self, col):
        return (abs(self.df[col] - self.df[col].mean())).mean()

    def iqr(self, col):
        return self.df[col].quantile(0.75) - self.df[col].quantile(0.25)

    def coeficiente_variacion(self, col):
        return (self.df[col].std(ddof=1) / self.df[col].mean()) * 100


    
    
# MÓDULO 1 - HOME ---------------------------------------

if opcion == "🛖 Home":

    st.image(
        "https://images.pexels.com/photos/534216/pexels-photo-534216.jpeg",
        use_container_width=True
    )

    st.title("Trabajo Final Python for Analytics - DMC")
    st.subheader("Análisis de Información sobre Telecomunicaciones")
    st.markdown("---")

    st.markdown("""
    Este trabajo consiste en analizar el archivo TelcoCustomerChurn.csv,
    que contiene información sobre los clientes, los servicios que tienen
    contratados, su facturación y su tiempo en la empresa.
    """)

    st.markdown("**🙋🏻‍♂️ | Autor:** Kevin Piscoche")
    st.markdown("**📗 | Curso:** Especialización en Python for Analytics")
    st.markdown("**📅 | Año:** 2026")

    st.markdown("""
    El dataset contiene información de 7,043 clientes
    incluyendo servicios contratados, facturación mensual
    y tiempo de permanencia. También indica si el cliente
    continúa activo o si se dio de baja (churn).
    """)

    st.markdown("**Herramientas utilizadas:** 🐍 Python | 🚀 Streamlit | 📊 Pandas")



# MÓDULO 2 - DATASET + EDA ----------------------------------
elif opcion == "✨ Dataset":

    st.title("Paso 1: Carga de archivo CSV")

    archivo = st.file_uploader(
        "Sube tu archivo CSV",
        type=["csv"]          )

    if archivo is not None:

        try:
            df = pd.read_csv(archivo)

            # CONVERSIONES, DE TIPO OBJECT A TIPO STRING ------------------------
            df["customerID"] = df["customerID"].astype("string")
            df["gender"] = df["gender"].astype("string")
            df["SeniorCitizen"] = df["SeniorCitizen"].astype("string")
            df["Partner"] = df["Partner"].astype("string")
            df["Dependents"] = df["Dependents"].astype("string")
            df["PhoneService"] = df["PhoneService"].astype("string")
            df["MultipleLines"] = df["MultipleLines"].astype("string")
            df["InternetService"] = df["InternetService"].astype("string")
            df["OnlineSecurity"] = df["OnlineSecurity"].astype("string")
            df["OnlineBackup"] = df["OnlineBackup"].astype("string")
            df["DeviceProtection"] = df["DeviceProtection"].astype("string")
            df["TechSupport"] = df["TechSupport"].astype("string")
            df["StreamingTV"] = df["StreamingTV"].astype("string")
            df["StreamingMovies"] = df["StreamingMovies"].astype("string")
            df["Contract"] = df["Contract"].astype("string")
            df["PaperlessBilling"] = df["PaperlessBilling"].astype("string")
            df["PaymentMethod"] = df["PaymentMethod"].astype("string")
            df["Churn"] = df["Churn"].astype("string")
            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

            # Instanciar clase -----
            analizador = Analyzer(df)

            st.success("✅ Archivo cargado correctamente")

            # Vista previa -----
            st.subheader("🔎 Vista previa del dataset")
            st.dataframe(df.head())

            # Dimensiones -----
            filas, columnas = df.shape
            st.subheader("📏 Dimensiones del dataset")
            st.write(f"Filas: {filas}")
            st.write(f"Columnas: {columnas}")

          
            # TABS EDA --------------------------------
            
            tabs = st.tabs([
                "1. 1.Información General",
                "2. 2.Clasificación",
                "3. 3.Estadísticas",
                "4. 4.Valores Faltantes",
                "5. 5.Distribución Numéricas",
                "6. 6.Variables Categóricas",
                "7. 7.Num vs Cat",
                "8. 8.Cat vs Cat",
                "9. 9.Análisis Dinámico",
                "10. 10.Hallazgos"
            ])

            # ITEM 1 -----------------------------------------------------------------
            with tabs[0]:
                st.subheader("📊 Tipos de Datos")
                st.dataframe(analizador.info_general())

                st.subheader("❗ Valores Nulos")
                st.dataframe(analizador.valores_nulos())

            # ITEM 2 -----------------------------------------------------------------
            with tabs[1]:
                numericas, categoricas = analizador.clasificar_variables()

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"Variables numéricas: {len(numericas)}")
                    st.write(numericas)

                with col2:
                    st.write(f"Variables categóricas: {len(categoricas)}")
                    st.write(categoricas)

            # ITEM 3 ----------------------------------------------------------------
            with tabs[2]:
                st.dataframe(analizador.estadisticas())

                numericas, _ = analizador.clasificar_variables()
                col = st.selectbox("Selecciona variable numérica", numericas)

                st.write(f"La media de los valores es:  {analizador.media(col):.2f}")
                st.write(f"La Mediana de los valores: {analizador.mediana(col):.2f}")
                st.write(f"El valor que más se repite(Moda) en el registro es{analizador.moda(col):.2f}")

            # ITEM 4 ----------------------------------------------------------------
            with tabs[3]:
                nulls = df.isnull().sum()

                fig, ax = plt.subplots()
                nulls.plot(kind="barh", ax=ax, color="#5CAD5C")
                # 🔢 Agregar valores al final de cada barra
                for container in ax.containers:
                    ax.bar_label(container, fmt="%d", padding=3)
                st.pyplot(fig)
                
                st.write("Discusión: Los valores faltantes corresponden a la columna TotalCharges, con una cantidad de 11 campos ")
            # ITEM 5 ----------------------------------------------------------------
            with tabs[4]:
                numericas, _ = analizador.clasificar_variables()
                col = st.selectbox("Histograma de:", numericas)

                fig, ax = plt.subplots()

                # Crear histograma manual para poder aplicar degradado
                counts, bins, patches = ax.hist(df[col], bins=20)

                # Aplicar degradado
                cmap = plt.cm.viridis
                colors = cmap(np.linspace(0.2, 1, len(patches)))

                for patch, color in zip(patches, colors):
                    patch.set_facecolor(color)

                 # Mostrar valores encima de cada barra
                for count, patch in zip(counts, patches):
                    if count > 0:
                        ax.text(
                            patch.get_x() + patch.get_width() / 2,
                            count,
                            int(count),
                            ha='center',
                            va='bottom',
                            fontsize=9,
                            fontweight='bold'
                        )

                ax.set_title(f"Distribución de {col}")
                ax.set_xlabel(col)
                ax.set_ylabel("Frecuencia")

                st.pyplot(fig)

            # ITEM 6 ------------------------------------------------------------
            with tabs[5]:
                _, categoricas = analizador.clasificar_variables()
            
                excluir = ["customerID"]   # agrega aquí la que quieras quitar
                categoricas = [c for c in categoricas if c not in excluir]
                col = st.selectbox("Variable categórica:", categoricas)

                fig, ax = plt.subplots()
                
                porcentajes = df[col].value_counts(normalize=True) * 100

                porcentajes.plot(kind="bar", ax=ax, colormap="Set2")

                # 🔢 Agregar porcentaje encima de cada barra
                for i, v in enumerate(porcentajes):
                    ax.text(i, v, f"{v:.1f}%",
                            ha="center",
                            va="bottom",
                            fontsize=9,
                            fontweight="bold")

                st.pyplot(fig)

            # ITEM 7 -------------------------------------------------------------
            with tabs[6]:

                col1, col2 = st.columns(2)

                with col1:
                    fig, ax = plt.subplots()
                    sb.boxplot(x="Churn", y="MonthlyCharges", data=df, ax=ax, palette="Set2")

                    # Calcular medianas
                    medianas = df.groupby("Churn")["MonthlyCharges"].median()

                    # Agregar valor de mediana encima de cada caja
                    for i, med in enumerate(medianas):
                        ax.text(i, med, f"{med:.2f}", 
                                horizontalalignment='center',
                                color='black',
                                fontsize=9,
                                fontweight='bold')

                    # Mostrar media como punto rojo
                    medias = df.groupby("Churn")["MonthlyCharges"].mean()
                    ax.scatter(range(len(medias)), medias, 
                            color="red", zorder=3, label="Media")

                    ax.legend()
                    st.pyplot(fig)

                with col2:
                    fig, ax = plt.subplots()
                    sb.boxplot(x="Churn", y="tenure", data=df, ax=ax, palette="Set2")

                    medianas = df.groupby("Churn")["tenure"].median()

                    for i, med in enumerate(medianas):
                        ax.text(i, med, f"{med:.2f}",
                                horizontalalignment='center',
                                color='black',
                                fontsize=9,
                                fontweight='bold')

                    medias = df.groupby("Churn")["tenure"].mean()
                    ax.scatter(range(len(medias)), medias,
                            color="red", zorder=3, label="Media")

                    ax.legend()
                    st.pyplot(fig)

            # ITEM 8 -------------------------------------------------------------
            with tabs[7]:

                col1, col2 = st.columns(2)

                with col1:
                    tabla = pd.crosstab(df["Contract"], df["Churn"], normalize="index")
                    fig, ax = plt.subplots()
                    tabla.plot(kind="bar", stacked=True, ax=ax, colormap="Paired")
                    ax.set_title("Proporción de Churn por Tipo de Contrato")

                    # Agregar etiquetas
                    for container in ax.containers:
                        ax.bar_label(container, fmt="%.2f", label_type="center", fontsize=8, color="black")

                    st.pyplot(fig)   # ✅ Solo una vez

                with col2:
                    tabla2 = pd.crosstab(df["InternetService"], df["Churn"], normalize="index")
                    fig, ax = plt.subplots()
                    tabla2.plot(kind="bar", stacked=True, ax=ax, colormap="tab20b")
                    ax.set_title("Proporción de Churn por Tipo de Internet")

                    # Agregar etiquetas
                    for container in ax.containers:
                        ax.bar_label(container, fmt="%.2f", label_type="center", fontsize=8, color="black")

                    st.pyplot(fig)   

            # ITEM 9 -------------------------------------------------------------
            with tabs[8]:
                numericas, _ = analizador.clasificar_variables()

                col = st.selectbox("Seleccione Columna:", numericas)

                rango = st.slider(
                    "Meses de Permanencia (Tenure)",
                    float(df[col].min()),
                    float(df[col].max()),
                    (float(df[col].min()), float(df[col].max()))
                )

                df_filtrado = df[(df[col] >= rango[0]) & (df[col] <= rango[1])]

                st.write(f"Registros filtrados: {df_filtrado.shape[0]}")
                
                fig, ax = plt.subplots()
                sb.histplot(df_filtrado[col], kde=True, ax=ax, color= "blue")
                st.pyplot(fig)

            # ITEM 10 --------------------------------------------------------------
            with tabs[9]:
                st.markdown("""
                ### Hallazgos Clave

                - Clientes con contrato mensual presentan mayor churn.
                - Clientes con menor tenure abandonan más rápido.
                - MonthlyCharges altos muestran mayor tasa de fuga.
                - Servicios adicionales reducen el churn.
                - Métodos automáticos de pago muestran menor abandono.
                """)

        except Exception as e:
            st.error("❌ Error al cargar el archivo.")
            st.exception(e)

    else:
        st.warning("Primero cargue un archivo CSV para continuar.")



# MÓDULO 3 - CONCLUSIONES -------------------------------

elif opcion == "✅ Conclusiones":

    st.title("Conclusiones")

    st.markdown("""
    1️⃣ El tipo de contrato influye fuertemente en el churn

    El análisis de proporciones muestra que los clientes con contrato mensual presentan una mayor tasa de abandono en comparación con contratos anuales o bianuales.
    Esto sugiere que la falta de compromiso a largo plazo incrementa el riesgo de cancelación.
    
    2️⃣ La permanencia (tenure) es un factor determinante
    
    Los boxplots evidencian que los clientes con menor tiempo en la empresa tienden a abandonar con mayor frecuencia.
    A mayor antigüedad, menor probabilidad de churn.
    
    3️⃣ Cargos mensuales altos se asocian con mayor abandono
    
    El análisis comparativo entre MonthlyCharges y Churn muestra que los clientes que pagan montos más elevados presentan una media y mediana superiores dentro del grupo que cancela el servicio.
    
    4️⃣ Algunos servicios impactan en la retención
    
    El análisis de variables categóricas indica que clientes con servicios adicionales (como soporte técnico o seguridad en línea) presentan menores proporciones de churn en comparación con quienes no los tienen.
    
    5️⃣ La calidad de los datos es adecuada para análisis
    
    El dataset presenta muy pocos valores nulos (principalmente en TotalCharges), lo que permite realizar análisis estadísticos confiables sin necesidad de imputaciones complejas.

    """)



