# Final_DMC_Kevin_Piscoche

📊 DESCRIPCIÓN DEL PROYECTO:

El sistema está organizado en menú lateral con navegación estructurada:

🛖 Home
✨ Dataset
✅ Conclusiones

Dentro del módulo Dataset se desarrolla un EDA completo en 10 pestañas.

📂 1. Home

Presentación del proyecto
Objetivo del análisis
Imagen representativa
Información del autor
Contexto del dataset
Herramientas utilizadas

📊 2. Dataset + EDA Completo (10 Tabs)

1️⃣ Información General ----------------------

Tipos de datos organizados
Conteo de valores nulos
Dimensiones del dataset
Vista previa

2️⃣ Clasificación Automática ----------------

Identificación automática de:
Variables numéricas
Variables categóricas
Conteo por tipo
Listado detallado

3️⃣ Estadísticas Descriptivas ---------------

Incluye:
.describe()
Media
Mediana
Moda
Comparación de tendencia central

4️⃣ Análisis de Valores Faltantes -----------

Conteo por variable
Gráfico de barras horizontal
Etiquetas numéricas visibles
Discusión analítica

5️⃣ Distribución de Variables Numéricas ------

Histogramas personalizados
Degradado de color
Etiquetas de frecuencia sobre barras
Identificación visual de asimetrías
Variables clave:
tenure
MonthlyCharges
TotalCharges

6️⃣ Variables Categóricas --------------------

Conteo proporcional (%)
Gráficos de barras
Etiquetas porcentuales visibles
Exclusión de variables técnicas como customerID
Variables analizadas:
Contract
InternetService
PaymentMethod
PaperlessBilling
TechSupport
StreamingTV
StreamingMovies

7️⃣ Numérico vs Categórico (Churn) ----------

Comparación de:
MonthlyCharges vs Churn
tenure vs Churn
Incluye:
Boxplots
Medianas visibles
Media como punto rojo
Comparación visual clara entre grupos

8️⃣ Categórico vs Categórico -----------------

Tablas cruzadas normalizadas:
Contract vs Churn
InternetService vs Churn
Incluye:
Gráficos apilados
Proporciones
Etiquetas internas en cada barra
Análisis comparativo de riesgo

9️⃣ Análisis Dinámico Interactivo ------------

Implementa widgets:
st.slider
st.selectbox
Filtro dinámico por rango
Histograma con KDE
Permite:
Filtrar por permanencia (tenure)
Analizar distribución en tiempo real
Observar cambios según rango seleccionado
Visualizar registros filtrados

🔟 Hallazgos Clave ----------------------------

Principales insights estratégicos:
Clientes con contrato mensual presentan mayor churn
Menor tenure se asocia con mayor abandono
MonthlyCharges altos incrementan riesgo
Servicios adicionales reducen probabilidad de fuga
Métodos automáticos de pago muestran menor abandono

📈 Variables Analizadas
·customerID
·SeniorCitizen
·gender
·Partner
·Dependents
·tenure
·PhoneService
·MultipleLines
·InternetService
·OnlineSecurity
·OnlineBackup
·DeviceProtection
·TechSupport
·StreamingTV
·StreamingMovies
·Contract
·PaperlessBilling
·PaymentMethod
·MonthlyCharges
·TotalCharges
·Churn

📊 Conceptos Estadísticos Aplicados

Media
Mediana
Moda
Rango
Varianza
Desviación estándar
Desviación media
IQR
Coeficiente de variación
Distribución
Comparación de grupos
Tablas cruzadas
Proporciones
Segmentación dinámica

🛠️ Tecnologías Utilizadas

Python 3.x
Streamlit
Pandas
NumPy
Matplotlib
Seaborn

📊 CAPTURAS DEL PROYECTO:

-------------------------------------- Vista Prinpal --------------------------------------
<img width="1206" height="1089" alt="image" src="https://github.com/user-attachments/assets/721d07e9-c28f-4212-bca6-e4d73e63cba9" />

-------------------------------------- Menú --------------------------------------
<img width="290" height="265" alt="image" src="https://github.com/user-attachments/assets/93da99e6-8ccb-4a5e-9cb7-0866343aedd7" />


-------------------------------------- Carga de BD --------------------------------------
<img width="1166" height="654" alt="image" src="https://github.com/user-attachments/assets/477ae153-0807-40ed-a17e-5ade76d688d5" />


-------------------------------------- Ejercicio 6 --------------------------------------
<img width="852" height="893" alt="image" src="https://github.com/user-attachments/assets/1bd39dc8-24c6-4494-b4d8-95425b2bbfa5" />


-------------------------------------- Ejercicio 8 --------------------------------------
<img width="865" height="613" alt="image" src="https://github.com/user-attachments/assets/6b751592-36e9-4ca0-9d2d-3e4c59d3bd42" />


📊 LINKS DEL PROYECTO:
· Streamlit: https://finaldmckevinpiscoche.streamlit.app/
