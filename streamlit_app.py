import sqlite3

DB_NAME = "kasir.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


conn = get_connection()
cur = conn.cursor()

# tabel user
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT DEFAULT 'user'
)
""")

# tabel barang
cur.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    nama_barang TEXT,
    harga INTEGER,
    stok INTEGER
)
""")

# tabel transaksi
cur.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total INTEGER
)
""")

# detail transaksi
cur.execute("""
CREATE TABLE IF NOT EXISTS transaction_detail(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER,
    product_id INTEGER,
    qty INTEGER,
    subtotal INTEGER
)
""")

conn.commit()

# admin default
try:
    cur.execute(
        "INSERT INTO users(username,password,role) VALUES(?,?,?)",
        ("admin","admin123","admin")
    )
    conn.commit()
except:
    pass

import streamlit as st
from database import get_connection

conn = get_connection()
cur = conn.cursor()

st.set_page_config(
    page_title="Kasir UMKM",
    layout="wide"
)

if "login" not in st.session_state:
    st.session_state.login = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "role" not in st.session_state:
    st.session_state.role = ""


def login():
    st.title("LOGIN KASIR UMKM")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cur.fetchone()

        if user:
            st.session_state.login = True
            st.session_state.user_id = user["id"]
            st.session_state.role = user["role"]
            st.success("Login berhasil")
            st.rerun()
        else:
            st.error("Username atau password salah")


def register():
    st.subheader("Daftar Akun")

    user = st.text_input("Username Baru")
    pw = st.text_input("Password Baru", type="password")

    if st.button("Daftar"):
        try:
            cur.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (user,pw)
            )
            conn.commit()
            st.success("Akun berhasil dibuat")
        except:
            st.error("Username sudah digunakan")


if st.session_state.login == False:
    tab1, tab2 = st.tabs(["Login","Register"])

    with tab1:
        login()

    with tab2:
        register()

else:
    st.title("Kasir UMKM")
    st.success("Login berhasil")

    st.write("Silakan gunakan menu di sidebar")

    if st.button("Logout"):
        st.session_state.login = False
        st.session_state.user_id = None
        st.session_state.role = ""
        st.rerun()

