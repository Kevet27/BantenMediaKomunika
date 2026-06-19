import streamlit as st
import sqlite3
import hashlib
import os

# ================= CONFIG =================

st.set_page_config(
    page_title="TILAS BUT RAOS",
    layout="wide"
)

# ================= FOLDER GAMBAR =================

if not os.path.exists("gambar_produk"):
    os.makedirs("gambar_produk")

# ================= DATABASE =================

conn = sqlite3.connect(
    "tilas_raos.db",
    check_same_thread=False
)

c = conn.cursor()

# ================= TABEL USERS =================

c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")

# ================= TABEL PRODUK =================

c.execute("""
CREATE TABLE IF NOT EXISTS produk(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nama TEXT,
harga INTEGER,
gambar TEXT
)
""")

# ================= TABEL KERANJANG =================

c.execute("""
CREATE TABLE IF NOT EXISTS keranjang(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
produk TEXT,
harga INTEGER
)
""")

# ================= TABEL PESANAN =================

c.execute("""
CREATE TABLE IF NOT EXISTS pesanan(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
alamat TEXT,
pembayaran TEXT,
total INTEGER
)
""")

conn.commit()

# ================= SESSION =================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = ""

# ================= HASH PASSWORD =================

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

# ================= LOGIN PAGE =================

def login_page():

    st.title("👕 TILAS BUT RAOS")

    menu = st.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    # REGISTER
    if menu == "Register":

        user = st.text_input(
            "Username"
        )

        pw = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Daftar"):

            c.execute(
                """
                SELECT *
                FROM users
                WHERE username=?
                """,
                (user,)
            )

            if c.fetchone():

                st.error(
                    "Username sudah digunakan"
                )

            else:

                c.execute(
                    """
                    INSERT INTO users
                    (username,password)
                    VALUES(?,?)
                    """,
                    (
                        user,
                        hash_password(pw)
                    )
                )

                conn.commit()

                st.success(
                    "Akun berhasil dibuat"
                )

    # LOGIN
    else:

        user = st.text_input(
            "Username"
        )

        pw = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            c.execute(
                """
                SELECT *
                FROM users
                WHERE username=?
                AND password=?
                """,
                (
                    user,
                    hash_password(pw)
                )
            )

            data = c.fetchone()

            if data:

                st.session_state.login = True
                st.session_state.user = user

                st.success(
                    "Login berhasil"
                )

                st.rerun()

            else:

                st.error(
                    "Username atau password salah"
                )
