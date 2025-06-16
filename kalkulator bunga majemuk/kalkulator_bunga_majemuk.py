import streamlit as st
import time

def calculate_compound_interest(principal, annual_rate, compounding_frequency, years):
    """
    Menghitung bunga majemuk.
    Args:
        principal (float): Modal awal (pokok).
        annual_rate (float): Tingkat bunga tahunan dalam persentase.
        compounding_frequency (int): Frekuensi penggabungan bunga per tahun.
        years (int): Jangka waktu investasi dalam tahun.
    Returns:
        tuple: Jumlah akhir dan total bunga yang diperoleh.
    """
    # Konversi tingkat bunga tahunan menjadi desimal
    r = annual_rate / 100
    # Hitung jumlah periode compounding
    n = compounding_frequency
    # Hitung total tahun
    t = years

    # Rumus bunga majemuk: A = P * (1 + r/n)^(n*t)
    # Perbaikan: Menggunakan ** untuk pangkat
    amount = principal * (1 + r / n)**(n * t)
    interest_earned = amount - principal
    return amount, interest_earned

def main():
    st.set_page_config(page_title="Kalkulator Bunga Majemuk", page_icon="💰", layout="centered")

    st.title("💰 Kalkulator Bunga Majemuk 💰")
    st.markdown("""
        <p style='text-align: center; font-size: 18px;'>
            Lihat bagaimana uang Anda bertumbuh dengan kekuatan bunga majemuk!
        </p>
    """, unsafe_allow_html=True)

    st.sidebar.header("Input Investasi Anda")

    # Input Modal Awal
    principal = st.sidebar.number_input(
        "Modal Awal (Rp)",
        min_value=100_000,
        max_value=1_000_000_000,
        value=10_000_000,
        step=100_000,
        help="Jumlah uang awal yang diinvestasikan atau dipinjam."
    )
    # Input Tingkat Bunga Tahunan
    annual_rate = st.sidebar.number_input(
        "Tingkat Bunga Tahunan (%)",
        min_value=0.1,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.1f",
        help="Tingkat bunga per tahun dalam persentase."
    )
    # Input Frekuensi Penggabungan Bunga
    # Menggunakan dictionary untuk pemetaan yang jelas
    compounding_options = {
        "Tahunan (1x/tahun)": 1,
        "Semi-Tahunan (2x/tahun)": 2,
        "Kuartalan (4x/tahun)": 4,
        "Bulanan (12x/tahun)": 12,
        "Harian (365x/tahun)": 365
    }
    selected_compounding_text = st.sidebar.selectbox(
        "Frekuensi Penggabungan Bunga",
        list(compounding_options.keys()),
        help="Seberapa sering bunga dihitung dan ditambahkan ke pokok."
    )
    compounding_frequency = compounding_options[selected_compounding_text]

    # Input Jangka Waktu
    years = st.sidebar.number_input(
        "Jangka Waktu (Tahun)",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        help="Lama waktu investasi dalam tahun."
    )

    st.markdown("---")

    if st.button("Hitung Bunga Majemuk"):
        with st.spinner("Menghitung potensi pertumbuhan uang Anda..."):
            time.sleep(1) # Mengurangi waktu sleep agar tidak terlalu lama saat testing

        final_amount, interest_earned = calculate_compound_interest(
            principal, annual_rate, compounding_frequency, years
        )

        st.subheader("🎉 Hasil Perhitungan 🎉")

        st.info(f"Modal Awal Anda: *Rp {principal:,.0f}*")
        st.info(f"Tingkat Bunga Tahunan: *{annual_rate:.1f}%*")
        st.info(f"Jangka Waktu: *{years} tahun*")
        st.success(f"Jumlah Akhir Setelah {years} Tahun: *Rp {final_amount:,.0f}*")
        st.success(f"Total Bunga yang Diperoleh: *Rp {interest_earned:,.0f}*")

        st.markdown("---") # Perbaikan: Menambahkan st.markdown("") untuk garis pemisah
        st.subheader("Visualisasi Pertumbuhan (Animasi Sederhana)")

        # Placeholder untuk animasi
        animation_placeholder = st.empty()

        # Animasi pertumbuhan bunga tahun per tahun (visualisasi sederhana)
        # Note: Ini adalah simulasi visual, bukan perhitungan tahunan yang presisi dari rumus bunga majemuk.
        # Tujuannya untuk menunjukkan progres pertumbuhan.
        current_display_amount = float(principal)
        progress_bar = st.progress(0) # Menambahkan progress bar untuk visualisasi yang lebih baik

        for year_num in range(1, years + 1):
            # Perkiraan pertumbuhan untuk visualisasi
            # Asumsi bunga ditambahkan setiap tahun untuk tujuan visual
            # Menggunakan bunga majemuk sederhana per tahun untuk visualisasi
            current_display_amount *= (1 + (annual_rate / 100))

            # Tentukan emoji berdasarkan pertumbuhan
            # Kriteria emoji yang lebih realistis dan tidak terlalu banyak
            growth_emoji = '📈'
            if year_num % 5 == 0: # Tambahkan emoji ekstra setiap 5 tahun
                growth_emoji += '✨'

            # Update progress bar
            progress_bar.progress(int((year_num / years) * 100))

            # Batasi tampilan agar tidak terlalu cepat jika jangka waktu panjang
            # Tampilkan setiap tahun jika <10 tahun, atau setiap 2 tahun, atau tahun terakhir
            if years <= 10 or year_num % 2 == 0 or year_num == years:
                animation_placeholder.markdown(
                    f"<h3 style='text-align: center;'>Tahun {year_num}: Rp {current_display_amount:,.0f} {growth_emoji}</h3>",
                    unsafe_allow_html=True
                )
                time.sleep(0.1) # Atur kecepatan animasi
            
        # Setelah loop selesai, kosongkan placeholder animasi dan tampilkan pesan akhir
        animation_placeholder.empty()
        st.success("Perhitungan dan visualisasi selesai! Selamat merencanakan keuangan Anda! ✨")
        
        st.markdown("---") # Garis pemisah setelah animasi

        st.subheader("Mengapa Bunga Majemuk Itu Penting?")
        st.markdown("""
            Bunga majemuk sering disebut sebagai *"keajaiban dunia kedelapan"* karena kemampuannya membuat uang Anda bertumbuh secara eksponensial dari waktu ke waktu.
            Bunga yang Anda peroleh ditambahkan ke modal awal Anda, dan kemudian bunga di periode berikutnya dihitung dari jumlah yang lebih besar tersebut. Ini menciptakan efek bola salju yang dapat sangat menguntungkan dalam jangka panjang.
            Semakin awal Anda memulai, semakin besar potensi pertumbuhan investasi Anda!
        """)


if __name__ == "__main__": # Perbaikan: __name__
    main()
