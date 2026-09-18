import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Para ti, Magui 💛",
    page_icon="🌻",
    layout="centered"
)

# Estilos visuales automatizados (Fondo oscuro, flores amarillas y animación)
custom_css = """
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: #ffffff;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

@keyframes fallingPetals {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0.2; }
}

.petal {
    position: fixed;
    top: -10px;
    color: #facc15;
    font-size: 24px;
    user-select: none;
    z-index: 1000;
    pointer-events: none;
    animation: fallingPetals 6s linear infinite;
}

.p1 { left: 10%; animation-duration: 7s; animation-delay: 0s; }
.p2 { left: 25%; animation-duration: 5s; animation-delay: 1s; }
.p3 { left: 45%; animation-duration: 8s; animation-delay: 2s; }
.p4 { left: 65%; animation-duration: 6s; animation-delay: 0.5s; }
.p5 { left: 85%; animation-duration: 7.5s; animation-delay: 1.5s; }

.title {
    color: #facc15;
    font-size: 2.2rem;
    font-weight: bold;
    text-shadow: 0 0 15px rgba(250, 204, 21, 0.4);
    margin-bottom: 5px;
    text-align: center;
}

.subtitle {
    color: #cbd5e1;
    font-size: 1rem;
    margin-bottom: 20px;
    text-align: center;
}

.message-box {
    background: rgba(250, 204, 21, 0.08);
    border: 1px dashed rgba(250, 204, 21, 0.4);
    border-radius: 16px;
    padding: 20px;
    color: #fef08a;
    font-size: 1.05rem;
    line-height: 1.7;
    text-align: left;
    margin-top: 20px;
}
</style>

<div class="petal p1">🌻</div>
<div class="petal p2">✨</div>
<div class="petal p3">🌼</div>
<div class="petal p4">🌻</div>
<div class="petal p5">💛</div>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# 1. Encabezado
st.markdown('<div class="title">Para ti, Magui 🌻💛</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">21 de Septiembre · Un detalle a la distancia</div>', unsafe_allow_html=True)

# 2. Foto de Magui
foto_url = "https://lh3.googleusercontent.com/d/1jj0Kqm9tlZFgMwYLq22jxeTFRvXJdiqI"
st.image(foto_url, use_container_width=True, caption="Magui 👑")

# 3. Reproductor de Música Automático (Perfect - Ed Sheeran)
st.markdown("### 🎵 Nuestra Canción - Perfect")
st.components.v1.html(
    """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/08mG3Y1vM1R1KG2xM4L939?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """,
    height=160,
)

# 4. Carta de Amor
mensaje = """
Magui, fuiste la primera persona que amé y con el tiempo entendí que también eres la única que mi corazón sigue eligiendo. Aunque hoy la distancia no me permita estar cerca de ti, quiero que sepas que pienso en ti más de lo que imaginas. El tiempo me ha enseñado que hay amores que, aunque estén lejos, nunca dejan de sentirse. Y yo sé que te amaré siempre. Un beso y abrazo a la distancia mi reyna 👑💛
"""

st.markdown(f'<div class="message-box">{mensaje}</div>', unsafe_allow_html=True)
