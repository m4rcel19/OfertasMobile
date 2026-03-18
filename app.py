import streamlit as st

# 1. Configuración de Marca y SEO (Optimizado para Chile)
st.set_page_config(page_title="Ofertas Chile - El Mejor Precio Directo", page_icon="🛍️", layout="centered")

st.markdown("""
    <style>
    /* Diseño Azul con Grid Morado */
    .stApp { background: radial-gradient(circle, #1a1f4d 0%, #0a0e27 100%); }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(138, 43, 226, 0.1) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(138, 43, 226, 0.1) 1px, transparent 1px);
        background-size: 50px 50px; pointer-events: none;
    }
    
    /* Títulos y textos */
    h1, h2, h3, p, label { color: #ffffff !important; text-shadow: 0px 0px 10px rgba(138, 43, 226, 0.5); }

    /* Botones Morados Neón que resaltan */
    div.stButton > button:first-child, a[data-testid="stLinkButton"] {
        background-color: #8a2be2 !important; color: white !important;
        border: 2px solid #bc13fe !important; border-radius: 15px !important;
        padding: 12px 24px !important; font-weight: bold !important;
        text-decoration: none !important; display: inline-flex !important;
        box-shadow: 0px 0px 20px rgba(188, 19, 254, 0.6) !important;
        width: 100%; transition: 0.3s;
    }

    a[data-testid="stLinkButton"]:hover {
        background-color: #bc13fe !important;
        box-shadow: 0px 0px 35px rgba(188, 19, 254, 1) !important;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Tu Portal de Ofertas
st.title("🛍️ Ofertas Chile")
st.write("### Encuentra Celulares, Ropa y Tecnología al mejor precio del país.")

# Buscador Multicategoría
busqueda = st.text_input("¿Qué quieres comprar hoy?", placeholder="Ej: iPhone 15, Zapatillas Nike, Macbook...")

if busqueda:
    st.markdown(f"## 🔥 Oportunidades Directas para: {busqueda}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### 🛒 Mercado Libre Chile")
        st.caption("Envío rápido y cuotas sin interés.")
        # Link directo de búsqueda en ML
        ml_link = f"https://www.mercadolibre.cl/jm/search?as_word={busqueda.replace(' ', '%20')}"
        st.link_button("🚀 Ver en Mercado Libre", ml_link)

    with col2:
        st.write("#### 🌐 Grandes Tiendas Chile")
        st.caption("Falabella, Ripley, París y más.")
        # Usamos Google Shopping Chile directamente (sin intermediarios)
        google_link = f"https://www.google.cl/search?q={busqueda.replace(' ', '+')}+precio&tbm=shop"
        st.link_button("🔍 Ver en Tiendas Líderes", google_link)

    st.markdown("---")
    
    # Sección de Cierre: Tu Asesoría Personal
    st.write("### 🙋‍♂️ ¿No sabes cuál elegir?")
    st.write("Dinos qué buscas y te enviamos la mejor oferta del día por WhatsApp.")
    msg = f"Hola! Busco el mejor precio para {busqueda} y necesito ayuda."
    # RECUERDA CAMBIAR EL NÚMERO ABAJO
    ws_link = f"https://wa.me/569XXXXXXXX?text={msg.replace(' ', '%20')}"
    st.link_button("💬 Consultar con un Experto", ws_link)

st.sidebar.title("GangaClick Chile")
st.sidebar.info("Buscador independiente. Sin intermediarios, solo las mejores ofertas.")
