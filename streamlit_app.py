import streamlit as st

# =========================================
# CONFIG
# =========================================

app_name = "EduTech Media"

st.set_page_config(
    page_title=app_name,
    layout="wide"
)

# =========================================
# DATA MENU
# =========================================

menus = [
    "Home",
    "Profil",
    "Portfolio",
    "Tentang Kami",
    "Kontak"
]

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #f5f5f5;
}

/* NAVBAR */
.navbar {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 30px;
}

.nav-title {
    color: white;
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 15px;
}

/* TITLE */
.title {
    text-align: center;
    color: #1e293b;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 20px;
}

/* CARD */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.portfolio-title {
    color: #1e293b;
    font-size: 25px;
    font-weight: bold;
}

/* KONTAK */
.contact-box {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# NAVBAR ATAS
# =========================================

st.markdown(f"""
<div class="navbar">
    <div class="nav-title">{app_name}</div>
</div>
""", unsafe_allow_html=True)

# MENU BERBARIS KE SAMPING
menu = st.radio(
    "Navigasi Menu",
    menus,
    horizontal=True
)

st.write("")

# =========================================
# HOME
# =========================================

if menu == "Home":

    st.markdown(f"""
    <div class="title">
        {app_name}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        Website media komunikasi modern menggunakan Streamlit
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.image(
        "https://picsum.photos/1200/400",
        use_container_width=True
    )

    st.write("")

    st.markdown("""
    ### Tentang Website

    Website ini dibuat menggunakan Python dan Streamlit
    untuk menampilkan profil, portfolio, dan media komunikasi.
    """)

# =========================================
# PROFIL
# =========================================

elif menu == "Profil":

    st.title("👤 Profil")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image(
            "https://picsum.photos/300/300",
            use_container_width=True
        )

    with col2:

        st.subheader("Nama Anda")

        st.write("""
        Saya adalah mahasiswa yang sedang belajar
        web development dan pengembangan media digital.
        """)

        st.write("### Skill")

        st.write("""
        - HTML & CSS
        - Python
        - Streamlit
        - JavaScript
        - UI/UX Design
        """)

# =========================================
# PORTFOLIO
# =========================================

elif menu == "Portfolio":

    st.title("💼 Portfolio")

    portfolios = [

        {
            "title": "Website Company Profile",
            "desc": "Membuat website modern dan responsive.",
            "image": "https://picsum.photos/400/200?1"
        },

        {
            "title": "Media Pembelajaran",
            "desc": "Media pembelajaran interaktif berbasis digital.",
            "image": "https://picsum.photos/400/200?2"
        },

        {
            "title": "Sistem Informasi Sekolah",
            "desc": "Aplikasi pengolahan data sekolah berbasis web.",
            "image": "https://picsum.photos/400/200?3"
        }

    ]

    cols = st.columns(3)

    for index, item in enumerate(portfolios):

        with cols[index % 3]:

            st.image(
                item["image"],
                use_container_width=True
            )

            st.markdown(f"""
            <div class="card">

            <div class="portfolio-title">
                {item["title"]}
            </div>

            <br>

            <p>
                {item["desc"]}
            </p>

            </div>
            """, unsafe_allow_html=True)

# =========================================
# TENTANG KAMI
# =========================================

elif menu == "Tentang Kami":

    st.title("ℹ️ Tentang Kami")

    st.write(f"""
    {app_name} dibuat sebagai media komunikasi digital
    modern yang responsif dan mudah dikembangkan.
    """)

    st.write("")

    st.write("""
    ### Tujuan Website

    - Media informasi
    - Menampilkan portfolio
    - Branding digital
    - Media komunikasi
    - Pengembangan project mahasiswa
    """)

# =========================================
# KONTAK
# =========================================

elif menu == "Kontak":

    st.title("📞 Kontak")

    with st.container():

        st.markdown("""
        <div class="contact-box">
        """, unsafe_allow_html=True)

        with st.form("contact_form"):

            nama = st.text_input("Nama Lengkap")

            email = st.text_input("Email")

            pesan = st.text_area("Pesan")

            submit = st.form_submit_button("Kirim Pesan")

            if submit:

                st.success("Pesan berhasil dikirim!")

                st.write("### Data Pesan")

                st.write(f"**Nama:** {nama}")
                st.write(f"**Email:** {email}")
                st.write(f"**Pesan:** {pesan}")

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.write("### Social Media")

    st.write("""
    - Instagram
    - GitHub
    - LinkedIn
    """)

# =========================================
# FOOTER
# =========================================

st.write("")
st.write("---")
st.caption(f"© 2026 {app_name} - Streamlit Version")
