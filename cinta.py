<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pesan Rahasia Untukmu ❤️</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            text-align: center;
            padding: 20px;
        }

        .card {
            background: rgba(255, 255, 255, 0.92);
            padding: 40px 30px;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(255, 105, 135, 0.25);
            max-width: 420px;
            width: 100%;
            position: relative;
            z-index: 10;
            transition: transform 0.3s ease;
        }

        .emoji {
            font-size: 64px;
            margin-bottom: 15px;
            animation: detak 1.2s infinite;
        }

        @keyframes detak {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
        }

        h1 {
            color: #d6336c;
            font-size: 24px;
            margin-bottom: 12px;
        }

        p {
            color: #555;
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 28px;
        }

        .btn-group {
            display: flex;
            justify-content: center;
            gap: 15px;
            min-height: 50px;
        }

        button {
            padding: 12px 26px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        #btn-mau {
            background-color: #ff477e;
            color: white;
            box-shadow: 0 5px 15px rgba(255, 71, 126, 0.4);
        }

        #btn-mau:hover {
            background-color: #e03165;
            transform: scale(1.08);
        }

        #btn-nggak {
            background-color: #e2e8f0;
            color: #475569;
            position: relative;
        }

        /* Animasi Hujan Hati saat diterima */
        .heart {
            position: fixed;
            top: -10vh;
            font-size: 24px;
            animation: jatuh linear forwards;
            z-index: 1;
            pointer-events: none;
        }

        @keyframes jatuh {
            to {
                transform: translateY(110vh) rotate(360deg);
            }
        }
    </style>
</head>
<body>

    <div class="card" id="kartu">
        <div class="emoji" id="emoji-utama">🥺👉👈</div>
        <h1 id="judul">Hai Kamu...</h1>
        <p id="pesan">
            Aku udah coba <i>debugging</i> perasaanku berkali-kali, tapi hasilnya tetap sama: <b>kamu adalah error terindah yang bikin sistem hidupku jalan terus.</b><br><br>
            Mau nggak jadi partner hidupku selamanya?
        </p>

        <div class="btn-group">
            <button id="btn-mau" onclick="terimaCinta()">Mau Banget! ❤️</button>
            <button id="btn-nggak" onmouseover="kabur()" ontouchstart="kabur()">Nggak Mau 😝</button>
        </div>
    </div>

    <script>
        const daftarAlasan = [
            "Eits, nggak kena! 😜",
            "Tombolnya lagi error tuh!",
            "Yakin nolak? Coba pikir lagi deh!",
            "Error 404: Penolakan tidak ditemukan!",
            "Udah klik yang pink aja biar kelar 😂",
            "Wlee, kejar terus kalau bisa!"
        ];
        let hitungKabur = 0;

        function kabur() {
            const btnNggak = document.getElementById('btn-nggak');
            const pesan = document.getElementById('pesan');
            
            // Ubah posisi tombol menjadi fixed agar bebas lari ke seluruh layar
            btnNggak.style.position = 'fixed';
            
            // Hitung koordinat acak di dalam layar
            const maxX = window.innerWidth - btnNggak.offsetWidth - 20;
            const maxY = window.innerHeight - btnNggak.offsetHeight - 20;
            
            const randomX = Math.max(10, Math.floor(Math.random() * maxX));
            const randomY = Math.max(10, Math.floor(Math.random() * maxY));
            
            btnNggak.style.left = randomX + 'px';
            btnNggak.style.top = randomY + 'px';

            // Ganti teks tombol dengan alasan lucu
            btnNggak.innerText = daftarAlasan[hitungKabur % daftarAlasan.length];
            hitungKabur++;
        }

        function terimaCinta() {
            const emoji = document.getElementById('emoji-utama');
            const judul = document.getElementById('judul');
            const pesan = document.getElementById('pesan');
            const btnNggak = document.getElementById('btn-nggak');
            const btnMau = document.getElementById('btn-mau');

            emoji.innerText = "🥰💖🎉";
            judul.innerText = "Yeay! Resmi Jadian Nih! ❤️";
            pesan.innerHTML = "Terima kasih sudah menerima <i>pull request</i> cintaku!<br>Mulai detik ini, status hubungan kita resmi: <b>NUR PUTRI DUYUNGKUUU!</b> 😘✨";
            
            btnNggak.style.display = 'none';
            btnMau.innerText = "Love You Full! 💕";
            btnMau.onclick = null;

            // Jalankan efek hujan hati
            setInterval(buatHati, 200);
        }

        function buatHati() {
            const hati = document.createElement('div');
            hati.classList.add('heart');
            const pilihanEmoji = ['❤️', '💖', '💕', '💘', '🥰', '🌹'];
            hati.innerText = pilihanEmoji[Math.floor(Math.random() * pilihanEmoji.length)];
            
            hati.style.left = Math.random() * 100 + 'vw';
            hati.style.animationDuration = (Math.random() * 2 + 2) + 's';
            
            document.body.appendChild(hati);

            setTimeout(() => {
                hati.remove();
            }, 4000);
        }
    </script>

</body>
</html>