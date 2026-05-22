import streamlit as st
from PIL import Image
import sqlite3
import os

# =========================================
# CONFIG
# =========================================

app_name = "BANTEN MEDIA KOMUNIKA"

st.set_page_config(
    page_title=app_name,
    layout="wide"
)

# =========================================
# SESSION LOGIN ADMIN
# =========================================

if "admin_login" not in st.session_state:
    st.session_state.admin_login = False

# =========================================
# FOLDER UPLOAD
# =========================================

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# =========================================
# DATABASE SQLITE
# =========================================

conn = sqlite3.connect(
    "portfolio.db",
    check_same_thread=False
)

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT,
    deskripsi TEXT,
    file_path TEXT
)
""")

conn.commit()

# =========================================
# DATA MENU
# =========================================

menus = [
    "Home",
    "Profil",
    "Portfolio",
    "Upload Karya",
    "Admin",
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
# NAVBAR
# =========================================

st.markdown(f"""
<div class="navbar">
    <div class="nav-title">{app_name}</div>
</div>
""", unsafe_allow_html=True)

# =========================================
# MENU
# =========================================

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

    st.markdown("""
    ### Selamat Datang

    Platform media komunikasi digital modern
    untuk menampilkan karya dan informasi.
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

    st.write("Berikut karya yang telah diupload:")

    # AMBIL DATA DATABASE
    c.execute(
        "SELECT * FROM portfolio ORDER BY id DESC"
    )

    data_portfolio = c.fetchall()

    if len(data_portfolio) == 0:

        st.info("Belum ada karya yang diupload.")

    else:

        cols = st.columns(3)

        for index, item in enumerate(data_portfolio):

            with cols[index % 3]:

                id_portfolio = item[0]
                judul = item[1]
                deskripsi = item[2]
                file_path = item[3]

                # TAMPILKAN GAMBAR
                if file_path.endswith(
                    ("png", "jpg", "jpeg")
                ):

                    st.image(
                        file_path,
                        use_container_width=True
                    )

                st.markdown(f"""
                <div class="card">

                <div class="portfolio-title">
                    {judul}
                </div>

                <br>

                <p>{deskripsi}</p>

                </div>
                """, unsafe_allow_html=True)

                # DOWNLOAD FILE
                with open(file_path, "rb") as file:

                    st.download_button(
                        label="⬇ Download File",
                        data=file,
                        file_name=os.path.basename(file_path),
                        key=f"download_{id_portfolio}"
                    )

                # =========================================
                # TOMBOL HAPUS KHUSUS ADMIN
                # =========================================

                if st.session_state.admin_login:

                    if st.button(
                        f"🗑 Hapus Karya",
                        key=f"hapus_{id_portfolio}"
                    ):

                        # HAPUS FILE
                        if os.path.exists(file_path):

                            os.remove(file_path)

                        # HAPUS DATABASE
                        c.execute(
                            "DELETE FROM portfolio WHERE id = ?",
                            (id_portfolio,)
                        )

                        conn.commit()

                        st.success(
                            "Karya berhasil dihapus!"
                        )

                        st.rerun()

# =========================================
# UPLOAD KARYA
# =========================================

elif menu == "Upload Karya":

    st.title("📤 Upload Karya")

    st.write("""
    Silakan upload karya atau project Anda.
    """)

    judul = st.text_input("Judul Karya")

    deskripsi = st.text_area("Deskripsi Karya")

    uploaded_file = st.file_uploader(
        "Upload File Karya",
        type=["png", "jpg", "jpeg", "pdf", "docx", "pptx"]
    )

    if st.button("Simpan Karya"):

        if judul and deskripsi and uploaded_file:

            # SIMPAN FILE
            file_path = os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            )

            with open(file_path, "wb") as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            # SIMPAN DATABASE
            c.execute(
                """
                INSERT INTO portfolio
                (judul, deskripsi, file_path)

                VALUES (?, ?, ?)
                """,
                (
                    judul,
                    deskripsi,
                    file_path
                )
            )

            conn.commit()

            st.success(
                "Karya berhasil diupload dan masuk ke portfolio!"
            )

            # PREVIEW GAMBAR
            if uploaded_file.type.startswith(
                "image"
            ):

                image = Image.open(uploaded_file)

                st.image(
                    image,
                    caption="Preview Karya",
                    use_container_width=True
                )

        else:

            st.error(
                "Harap lengkapi semua data."
            )

# =========================================
# ADMIN LOGIN
# =========================================

elif menu == "Admin":

    st.title("🔐 Login Admin")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login Admin"):

        if username == "admin" and password == "12345":

            st.session_state.admin_login = True

            st.success("Login admin berhasil!")

        else:

            st.error("Username atau password salah")

    # STATUS LOGIN
    if st.session_state.admin_login:

        st.success("Anda login sebagai admin")

        if st.button("Logout"):

            st.session_state.admin_login = False

            st.rerun()

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

# =========================================
# FOOTER
# =========================================

st.write("")
st.write("---")
st.caption(f"© 2026 {app_name} - Streamlit Version")v
