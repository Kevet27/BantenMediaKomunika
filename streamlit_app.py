```python
import streamlit as st
import sqlite3
import hashlib

# ================= DATABASE =================

conn = sqlite3.connect("tilas_raos.db", check_same_thread=False)
c = conn.cursor()

# ================= TABEL =================

c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
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
pembayaran TEXT,
total INTEGER
)
""")

conn.commit()

# ================= DATA AWAL PRODUK =================

produk_awal = [
    ("Kaos Premium", 75000),
    ("Hoodie Casual", 150000),
    ("Kemeja Fashion", 120000)
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
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = ""

if "checkout" not in st.session_state:
    st.session_state.checkout = False


# ================= PASSWORD HASH =================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ================= LOGIN =================

def login_page():

    st.title("👕 TILAS BUT RAOS")

    menu = st.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    # REGISTER
    if menu == "Register":

        user = st.text_input("Username")
        pw = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Daftar"):

            c.execute(
                "SELECT * FROM users WHERE username=?",
                (user,)
            )

            if c.fetchone():
                st.error("Username sudah digunakan")

            else:
                c.execute(
                    "INSERT INTO users(username,password) VALUES(?,?)",
                    (
                        user,
                        hash_password(pw)
                    )
                )

                conn.commit()

                st.success("Akun berhasil dibuat")

    # LOGIN
    else:

        user = st.text_input("Username")
        pw = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            c.execute(
                """
                SELECT * FROM users
                WHERE username=? AND password=?
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

                st.success("Login berhasil")
                st.rerun()

            else:
                st.error("Login gagal")


# ================= BERANDA =================

def home():

    st.title("🏠 Beranda TILAS BUT RAOS")

    data = c.execute(
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
                INSERT INTO keranjang(user,produk,harga)
                VALUES(?,?,?)
                """,
                (
                    st.session_state.user,
                    p[1],
                    p[2]
                )
            )

            conn.commit()

            st.success("Produk masuk keranjang")


# ================= KERANJANG =================

def cart():

    st.title("🛒 Keranjang")

    data = c.execute(
        """
        SELECT id,produk,harga
        FROM keranjang
        WHERE user=?
        """,
        (st.session_state.user,)
    ).fetchall()

    total = 0

    for x in data:

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(
                x[1],
                "- Rp",
                x[2]
            )

        with col2:
            if st.button(
                "Hapus",
                key=x[0]
            ):

                c.execute(
                    """
                    DELETE FROM keranjang
                    WHERE id=?
                    """,
                    (x[0],)
                )

                conn.commit()
                st.rerun()

        total += x[2]

    st.subheader(
        f"Total : Rp {total}"
    )


# ================= CHECKOUT =================

def checkout():

    st.title("📦 Checkout")

    alamat = st.text_area(
        "Alamat Pembeli"
    )

    bayar = st.selectbox(
        "Metode Pembayaran",
        [
            "Transfer Bank",
            "DANA",
            "OVO"
        ]
    )

    data = c.execute(
        """
        SELECT harga
        FROM keranjang
        WHERE user=?
        """,
        (st.session_state.user,)
    ).fetchall()

    total = 0

    for x in data:
        total += x[0]

    st.write("Total Belanja : Rp", total)

    if st.button("Bayar"):

        c.execute(
            """
            INSERT INTO pesanan
            (user,alamat,pembayaran,total)
            VALUES(?,?,?,?)
            """,
            (
                st.session_state.user,
                alamat,
                bayar,
                total
            )
        )

        conn.commit()

        c.execute(
            """
            DELETE FROM keranjang
            WHERE user=?
            """,
            (st.session_state.user,)
        )

        conn.commit()

        st.success(
            "Pesanan berhasil dibuat"
        )


# ================= RIWAYAT PESANAN =================

def riwayat():

    st.title("📋 Riwayat Pesanan")

    data = c.execute(
        """
        SELECT alamat,pembayaran,total
        FROM pesanan
        WHERE user=?
        """,
        (st.session_state.user,)
    ).fetchall()

    if len(data) == 0:
        st.info("Belum ada pesanan")

    else:

        for x in data:

            st.write("Alamat :", x[0])
            st.write("Pembayaran :", x[1])
            st.write("Total :", "Rp", x[2])

            st.divider()


# ================= ADMIN PRODUK =================

def admin_produk():

    st.title("⚙ Admin Produk")

    nama = st.text_input(
        "Nama Produk"
    )

    harga = st.number_input(
        "Harga Produk",
        min_value=1000
    )

    if st.button("Tambah Produk"):

        c.execute(
            """
            INSERT INTO produk(nama,harga)
            VALUES(?,?)
            """,
            (
                nama,
                harga
            )
        )

        conn.commit()

        st.success(
            "Produk berhasil ditambahkan"
        )

    st.subheader("Daftar Produk")

    data = c.execute(
        "SELECT * FROM produk"
    ).fetchall()

    for p in data:

        col1, col2 = st.columns([3,1])

        with col1:
            st.write(
                p[1],
                "- Rp",
                p[2]
            )

        with col2:
            if st.button(
                "Hapus",
                key="hapus"+str(p[0])
            ):

                c.execute(
                    """
                    DELETE FROM produk
                    WHERE id=?
                    """,
                    (p[0],)
                )

                conn.commit()

                st.rerun()


# ================= MAIN =================

if not st.session_state.login:

    login_page()

else:

    if st.session_state.user == "admin":

        menu = st.sidebar.selectbox(
            "Menu",
            [
                "Beranda",
                "Keranjang",
                "Checkout",
                "Riwayat",
                "Admin Produk",
                "Logout"
            ]
        )

    else:

        menu = st.sidebar.selectbox(
            "Menu",
            [
                "Beranda",
                "Keranjang",
                "Checkout",
                "Riwayat",
                "Logout"
            ]
        )

    if menu == "Beranda":
        home()

    elif menu == "Keranjang":
        cart()

    elif menu == "Checkout":
        checkout()

    elif menu == "Riwayat":
        riwayat()

    elif menu == "Admin Produk":
        admin_produk()

    elif menu == "Logout":

        st.session_state.login = False
        st.session_state.user = ""

        st.rerun()
```
