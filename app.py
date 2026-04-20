import streamlit as st
import random

st.set_page_config(page_title="Media SPLSV", layout="centered")

st.title("📘 Media Pembelajaran SPLSV")
st.write("Belajar & Berlatih Persamaan Linear Satu Variabel")

# =========================
# SESSION STATE
# =========================
if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "soal" not in st.session_state:
    st.session_state.soal = None

# =========================
# PILIH LEVEL
# =========================
level = st.selectbox("Pilih Level", ["Mudah", "Sedang", "Sulit"])

# =========================
# GENERATE SOAL
# =========================
def generate_soal(level):
    if level == "Mudah":
        a = random.randint(1, 5)
        x = random.randint(1, 10)
        b = random.randint(0, 10)
    elif level == "Sedang":
        a = random.randint(1, 10)
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)
    else:
        a = random.randint(2, 15)
        x = random.randint(-20, 20)
        b = random.randint(-20, 20)

    c = a * x + b
    return a, b, c, x

# =========================
# BUAT SOAL BARU
# =========================
if st.button("🎲 Buat Soal"):
    st.session_state.soal = generate_soal(level)

# =========================
# TAMPILKAN SOAL
# =========================
if st.session_state.soal:
    a, b, c, jawaban = st.session_state.soal

    st.markdown("### Selesaikan:")
    st.latex(f"{a}x + {b} = {c}")

    user_jawab = st.number_input("Masukkan nilai x", step=1.0)

    if st.button("Cek Jawaban"):
        st.session_state.total += 1

        if user_jawab == jawaban:
            st.success("✅ Jawaban Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban yang benar adalah x = {jawaban}")

        # =========================
        # TAMPILKAN LANGKAH
        # =========================
        st.markdown("### Pembahasan:")
        st.write(f"{a}x + {b} = {c}")
        st.write(f"{a}x = {c} - {b}")
        st.write(f"{a}x = {c - b}")
        st.write(f"x = {(c - b)} / {a}")
        st.write(f"x = {jawaban}")

# =========================
# SKOR
# =========================
st.markdown("---")
st.subheader("📊 Skor Kamu")

if st.session_state.total > 0:
    nilai = (st.session_state.score / st.session_state.total) * 100
    st.write(f"Benar: {st.session_state.score}")
    st.write(f"Total Soal: {st.session_state.total}")
    st.write(f"Nilai: {nilai:.2f}")
else:
    st.write("Belum ada soal dikerjakan")

# =========================
# RESET
# =========================
if st.button("🔄 Reset Skor"):
    st.session_state.score = 0
    st.session_state.total = 0
