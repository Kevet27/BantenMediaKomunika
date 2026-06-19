import streamlit as st
import sqlite3
import hashlib

# ================= DATABASE =================

conn = sqlite3.connect("tilas_raos.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS produk(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nama TEXT,
harga INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS keranjang(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
produk TEXT,
harga INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS pesanan(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
alamat TEXT,
pembayaran TEXT
)
""")

conn.commit()


# ================= DATA PRODUK =================

produk_awal=[
("Kaos Premium",75000),
("Hoodie Casual",150000),
("Kemeja Fashion",120000)
]

for p in produk_awal:
    c.execute(
    "SELECT * FROM produk WHERE nama=?",
    (p[0],)
    )

    if not c.fetchone():

        c.execute(
        "INSERT INTO produk(nama,harga) VALUES(?,?)",
        p
        )

conn.commit()


# ================= SESSION =================

if "login" not in st.session_state:
    st.session_state.login=False

if "user" not in st.session_state:
    st.session_state.user=""



def hash_password(p):

    return hashlib.sha256(
        p.encode()
    ).hexdigest()



# ================= LOGIN =================

def login_page():

    st.title("👕 TILAS BUT RAOS")

    menu=st.selectbox(
        "Menu",
        ["Login","Register"]
    )

    if menu=="Register":

        user=st.text_input("Username")
        pw=st.text_input(
            "Password",
            type="password"
        )

        if st.button("Daftar"):

            c.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (
            user,
            hash_password(pw)
            )
            )

            conn.commit()

            st.success("Akun berhasil dibuat")

    else:

        user=st.text_input("Username")
        pw=st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (
            user,
            hash_password(pw)
            )
            )

            data=c.fetchone()

            if data:

                st.session_state.login=True
                st.session_state.user=user

                st.success("Login berhasil")

                st.rerun()

            else:

                st.error("Login gagal")




# ================= BERANDA =================

def home():

    st.title("🏠 Beranda TILAS BUT RAOS")

    data=c.execute(
    "SELECT * FROM produk"
    ).fetchall()

    for p in data:

        st.subheader(p[1])

        st.write(
        "Harga : Rp",
        p[2]
        )

        if st.button(
            "Tambah Keranjang",
            key=p[0]
        ):

            c.execute(
            """
            INSERT INTO keranjang
            (user,produk,harga)
            VALUES(?,?,?)
            """,
            (
            st.session_state.user,
            p[1],
            p[2]
            )
            )

            conn.commit()

            st.success(
            "Masuk keranjang"
            )



# ================= CART =================

def cart():

    st.title("🛒 Keranjang")

    data=c.execute(
    """
    SELECT produk,harga 
    FROM keranjang
    WHERE user=?
    """,
    (st.session_state.user,)
    ).fetchall()

    total=0

    for x in data:

        st.write(
        x[0],
        "- Rp",
        x[1]
        )

        total+=x[1]

    st.write(
    "Total : Rp",
    total
    )

    if st.button("Checkout"):

        st.session_state.checkout=True




# ================= CHECKOUT =================

def checkout():

    st.title("📦 Checkout")

    alamat=st.text_area(
        "Alamat Pembeli"
    )

    bayar=st.selectbox(
        "Pembayaran",
        [
        "Transfer Bank",
        "Dana",
        "OVO"
        ]
    )

    if st.button("Bayar"):

        c.execute(
        """
        INSERT INTO pesanan
        (user,alamat,pembayaran)
        VALUES(?,?,?)
        """,
        (
        st.session_state.user,
        alamat,
        bayar
        )
        )

        conn.commit()

        st.success(
        "Pembayaran berhasil"
        )




# ================= MAIN =================

if not st.session_state.login:

    login_page()

else:

    menu=st.sidebar.selectbox(
        "Menu",
        [
        "Beranda",
        "Keranjang",
        "Checkout",
        "Logout"
        ]
    )

    if menu=="Beranda":
        home()

    elif menu=="Keranjang":
        cart()

    elif menu=="Checkout":
        checkout()

    else:

        st.session_state.login=False
        st.rerun()

