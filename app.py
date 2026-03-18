import streamlit as st

# 1. Configuración de Marca y Diseño Pro
st.set_page_config(page_title="Ofertas Mobile Chile", page_icon="📲", layout="centered")

st.markdown("""
    <style>
    /* Fondo Azul Profundo con efecto de profundidad */
    .stApp {
        background: radial-gradient(circle, #1a1f4d 0%, #0a0e27 100%);
    }
    
    /* Líneas Moradas de Neón en el fondo */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(138, 43, 226, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(138, 43, 226, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
    }

    /* Títulos en Blanco Brillante */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(138, 43, 226, 0.5);
    }

    /* BOTONES MORADOS VIBRANTES */
    .stButton>button, .stDownloadButton>button, .stElementAction>a, a[data-testid="stLinkButton"] {
        background-color: #8a2be2 !important;
        color: white !important;
        border: 2px solid #bc13fe !important;
        border-radius: 15px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: inline-flex !important;
        box-shadow: 0px 0px 15px rgba(188, 19, 254, 0.6) !important;
    }

    /* Efecto al pasar el mouse */
    .stButton>button:hover, a[data-testid="stLinkButton"]:hover {
        background-color: #bc13fe !important;
        box-shadow: 0px 0px 30px rgba(188, 19, 254, 1) !important;
        transform: scale(1.02);
    }

    /* Cajas de productos (Cards) */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(138, 43, 226, 0.3);
        border-radius: 15px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Contenido de la Web
st.title("📲 Ofertas Mobile Chile")
st.write("### Buscador de Tecnología en Tiempo Real")

modelo = st.text_input("¿Qué celular buscas hoy?", placeholder="Ej: iPhone 15 Pro, Galaxy S24...")

if modelo:
    st.markdown(f"## 🔥 Oportunidades para: {modelo}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🛒 Mercado Libre")
        ml_link = f"https://www.mercadolibre.cl/jm/search?as_word={modelo.replace(' ', '%20')}"
        st.link_button("🚀 Ver en ML Chile", ml_link)

    with col2:
        st.write("### 📊 SoloTodo")
        st_link = f"https://www.solotodo.cl/search?search={modelo.replace(' ', '+')}"
        st.link_button("🔍 Comparar Precios", st_link)

    st.markdown("---")
    
    # Sección de Asesoría
    st.write("### 🙋‍♂️ ¿Necesitas ayuda experta?")
    msg = f"Hola! Busco un {modelo} y quiero asesoría."
    # Pon tu número real aquí:
    ws_link = f"https://wa.me/569XXXXXXXX?text={msg.replace(' ', '%20')}"
    st.link_button("💬 Hablar por WhatsApp", ws_link)

st.sidebar.title("GangaClick CL")
st.sidebar.info("Modo Cyber-Grid Activado")