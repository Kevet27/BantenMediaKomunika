<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Website Media Komunikasi</title>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family: Arial, sans-serif;
    }

    body{
      background:#f4f4f4;
      color:#333;
      scroll-behavior:smooth;
    }

    /* HEADER */
    header{
      background:#1e293b;
      padding:15px 30px;
      position:sticky;
      top:0;
      z-index:1000;
    }

    nav{
      display:flex;
      justify-content:space-between;
      align-items:center;
    }

    .logo{
      color:white;
      font-size:24px;
      font-weight:bold;
    }

    .menu{
      display:flex;
      list-style:none;
      gap:20px;
    }

    .menu li a{
      text-decoration:none;
      color:white;
      transition:0.3s;
      font-weight:bold;
    }

    .menu li a:hover{
      color:#38bdf8;
    }

    /* HERO */
    .hero{
      height:90vh;
      display:flex;
      justify-content:center;
      align-items:center;
      flex-direction:column;
      text-align:center;
      background:linear-gradient(to right, #0f172a, #1e3a8a);
      color:white;
      padding:20px;
    }

    .hero h1{
      font-size:50px;
      margin-bottom:20px;
    }

    .hero p{
      font-size:20px;
      max-width:700px;
      margin-bottom:30px;
    }

    .btn{
      background:#38bdf8;
      color:white;
      padding:12px 25px;
      border:none;
      border-radius:5px;
      text-decoration:none;
      transition:0.3s;
    }

    .btn:hover{
      background:#0ea5e9;
    }

    /* SECTION */
    section{
      padding:80px 10%;
    }

    .section-title{
      text-align:center;
      margin-bottom:50px;
      font-size:35px;
      color:#1e293b;
    }

    /* PROFIL */
    .profil{
      display:flex;
      flex-wrap:wrap;
      gap:30px;
      align-items:center;
    }

    .profil img{
      width:300px;
      border-radius:10px;
    }

    .profil-text{
      flex:1;
    }

    /* PORTFOLIO */
    .portfolio-container{
      display:grid;
      grid-template-columns:repeat(auto-fit, minmax(250px,1fr));
      gap:20px;
    }

    .card{
      background:white;
      border-radius:10px;
      overflow:hidden;
      box-shadow:0 4px 10px rgba(0,0,0,0.1);
      transition:0.3s;
    }

    .card:hover{
      transform:translateY(-5px);
    }

    .card img{
      width:100%;
      height:200px;
      object-fit:cover;
    }

    .card-content{
      padding:20px;
    }

    /* TENTANG */
    .tentang{
      text-align:center;
      line-height:1.8;
    }

    /* KONTAK */
    .kontak-container{
      display:flex;
      justify-content:center;
    }

    .kontak-form{
      background:white;
      padding:30px;
      border-radius:10px;
      width:100%;
      max-width:500px;
      box-shadow:0 4px 10px rgba(0,0,0,0.1);
    }

    .kontak-form input,
    .kontak-form textarea{
      width:100%;
      padding:12px;
      margin-bottom:15px;
      border:1px solid #ccc;
      border-radius:5px;
      font-size:16px;
    }

    .kontak-form button{
      width:100%;
      background:#1e293b;
      color:white;
      padding:12px;
      border:none;
      border-radius:5px;
      cursor:pointer;
      transition:0.3s;
      font-size:16px;
    }

    .kontak-form button:hover{
      background:#0f172a;
    }

    .social-media{
      text-align:center;
      margin-top:20px;
    }

    .social-media a{
      text-decoration:none;
      margin:0 10px;
      color:#1e293b;
      font-weight:bold;
    }

    .social-media a:hover{
      color:#38bdf8;
    }

    /* FOOTER */
    footer{
      background:#1e293b;
      color:white;
      text-align:center;
      padding:20px;
      margin-top:50px;
    }

    /* RESPONSIVE */
    @media(max-width:768px){

      .hero h1{
        font-size:35px;
      }

      .hero p{
        font-size:18px;
      }

      .menu{
        gap:10px;
        font-size:14px;
      }

      .profil{
        flex-direction:column;
        text-align:center;
      }

      .profil img{
        width:250px;
      }
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <nav>
      <div class="logo">Banten Media Komunika</div>

      <!-- MENU DINAMIS -->
      <ul class="menu" id="menu"></ul>
    </nav>
  </header>

  <!-- HERO -->
  <section class="hero" id="home">
    <h1>Selamat Datang</h1>

    <p>
      Website media komunikasi modern untuk menampilkan profil,
      portfolio, dan informasi secara profesional.
    </p>

    <a href="#portfolio" class="btn">
      Lihat Portfolio
    </a>
  </section>

  <!-- PROFIL -->
  <section id="profil">
    <h2 class="section-title">Profil</h2>

    <div class="profil">

      <img src="https://picsum.photos/300/300" alt="profil">

      <div class="profil-text">

        <h3>Nama Anda</h3>

        <br>

        <p>
          Saya adalah mahasiswa yang sedang belajar web development
          dan pengembangan media komunikasi digital.
        </p>

        <br>

        <h4>Skill:</h4>

        <ul>
          <li>HTML & CSS</li>
          <li>JavaScript</li>
          <li>UI/UX Design</li>
          <li>Web Development</li>
        </ul>

      </div>
    </div>
  </section>

  <!-- PORTFOLIO -->
  <section id="portfolio">

    <h2 class="section-title">Portfolio</h2>

    <div class="portfolio-container">

      <div class="card">
        <img src="https://picsum.photos/400/200?1" alt="">
        <div class="card-content">
          <h3>Project Website</h3>
          <p>Membuat website company profile modern.</p>
        </div>
      </div>

      <div class="card">
        <img src="https://picsum.photos/400/200?2" alt="">
        <div class="card-content">
          <h3>UI Design</h3>
          <p>Desain antarmuka aplikasi mobile dan web.</p>
        </div>
      </div>

      <div class="card">
        <img src="https://picsum.photos/400/200?3" alt="">
        <div class="card-content">
          <h3>Media Pembelajaran</h3>
          <p>Membuat media pembelajaran interaktif digital.</p>
        </div>
      </div>

    </div>
  </section>

  <!-- TENTANG -->
  <section id="tentang">

    <h2 class="section-title">Tentang Kami</h2>

    <div class="tentang">

      <p>
        Website ini dibuat sebagai media komunikasi dan informasi
        digital yang modern, responsif, dan mudah dikembangkan.
      </p>

      <br>

      <p>
        Tujuan utama website ini adalah memberikan pengalaman
        pengguna yang nyaman dan profesional.
      </p>

    </div>
  </section>

  <!-- KONTAK -->
  <section id="kontak">

    <h2 class="section-title">Kontak</h2>

    <div class="kontak-container">

      <form class="kontak-form">

        <input type="text" placeholder="Nama Lengkap" required>

        <input type="email" placeholder="Email" required>

        <textarea rows="5" placeholder="Tulis pesan Anda..." required></textarea>

        <button type="submit">
          Kirim Pesan
        </button>

      </form>

    </div>

    <!-- SOCIAL MEDIA -->
    <div class="social-media">

      <p>Follow Me</p>

      <br>

      <a href="#">Instagram</a>
      <a href="#">GitHub</a>
      <a href="#">LinkedIn</a>

    </div>

  </section>

  <!-- FOOTER -->
  <footer>
    <p>© 2026 MyWebsite | All Rights Reserved</p>
  </footer>

  <!-- JAVASCRIPT -->
  <script>

    /*
      MENU DINAMIS
      Tambahkan menu baru cukup di array berikut
    */

    const menus = [
      {
        name: "Home",
        link: "#home"
      },
      {
        name: "Profil",
        link: "#profil"
      },
      {
        name: "Portfolio",
        link: "#portfolio"
      },
      {
        name: "Tentang Kami",
        link: "#tentang"
      },
      {
        name: "Kontak",
        link: "#kontak"
      }

      // Tambahkan menu baru di sini
    ];

    const menuContainer = document.getElementById("menu");

    menus.forEach(menu => {

      const li = document.createElement("li");

      li.innerHTML = `
        <a href="${menu.link}">
          ${menu.name}
        </a>
      `;

      menuContainer.appendChild(li);

    });

  </script>

</body>
</html>
