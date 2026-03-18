import streamlit as st

# 1. Configuración de Marca Pro (SEO Friendly)
st.set_page_config(page_title="Ofertas Chile - El mejor precio en un clic", page_icon="🛍️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1a1f4d 0%, #0a0e27 100%); }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: linear-gradient(rgba(138, 43, 226, 0.1) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(138, 43, 226, 0.1) 1px, transparent 1px);
        background-size: 50px 50px; pointer-events: none;
    }
    h1, h2, h3, p, label { color: #ffffff !important; text-shadow: 0px 0px 10px rgba(138, 43, 226, 0.5); }
    
    /* Botones Neón Morados */
    a[data-testid="stLinkButton"] {
        background-color: #8a2be2 !important; color: white !important;
        border: 2px solid #bc13fe !important; border-radius: 15px !important;
        padding: 10px 20px !important; font-weight: bold !important;
        text-decoration: none !important; display: inline-flex !important;
        box-shadow: 0px 0px 15px rgba(188, 19, 254, 0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Contenido Multicategoría
st.title("🛍️ Ofertas Chile")
st.write("### Encuentra lo mejor en Tecnología, Ropa y más al precio más bajo.")

# Cambiamos el placeholder para que la gente sepa que puede buscar de todo
busqueda = st.text_input("¿Qué buscas hoy?", placeholder="Ej: iPhone 15, Zapatillas Nike, Polerón North Face...")

if busqueda:
    st.markdown(f"## 🔥 Mejores opciones para: {busqueda}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🛒 Mercado Libre")
        st.caption("Envío rápido a todo Chile.")
        link_ml = f"https://www.mercadolibre.cl/jm/search?as_word={busqueda.replace(' ', '%20')}"
        st.link_button("🚀 Ver Ofertas en ML", link_ml)

    with col2:
        st.write("### 📊 SoloTodo / Google")
        st.caption("Compara precios en todo Chile.")
        # SoloTodo es mejor para tech, pero para ropa Google Shopping es el rey
        link_google = f"https://www.google.com/search?q={busqueda.replace(' ', '+')}+precio+chile&tbm=shop"
        st.link_button("🔍 Comparar Precios", link_google)

    st.markdown("---")
    st.write("### 🙋‍♂️ ¿Necesitas ayuda con tu talla o modelo?")
    msg = f"Hola! Busco {busqueda} y necesito asesoría para comprar."
    ws_link = f"https://wa.me/569XXXXXXXX?text={msg.replace(' ', '%20')}"
    st.link_button("💬 Hablar con un Experto", ws_link)

st.sidebar.title("GangaClick Pro")
st.sidebar.info("Busca Celulares, Ropa, Computación y más. ¡Todo en un solo lugar!")
