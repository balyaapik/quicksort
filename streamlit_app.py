import streamlit as st
import matplotlib.pyplot as plt
import random
import time

# Fungsi untuk menampilkan array sebagai bar chart dengan warna indikator
def plot_array(arr, pivot_idx=None, i_idx=None, j_idx=None):
    colors = []
    for idx in range(len(arr)):
        if idx == pivot_idx:
            colors.append("red")     # pivot
        elif idx == j_idx:
            colors.append("yellow")  # j
        elif idx == i_idx:
            colors.append("green")   # i
        else:
            colors.append("blue")    # lainnya
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=colors)
    st.pyplot(fig)
    plt.close(fig)

# Fungsi untuk menukar elemen
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# QuickSort dengan visualisasi
def quick_sort_visual(arr, kiri, kanan, delay):
    if kiri >= kanan:
        return

    pivot = arr[kanan]
    i = kiri - 1
    pivot_idx = kanan

    for j in range(kiri, kanan):
        plot_array(arr, pivot_idx=pivot_idx, i_idx=i, j_idx=j)
        time.sleep(delay)

        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
            plot_array(arr, pivot_idx=pivot_idx, i_idx=i, j_idx=j)
            time.sleep(delay)

    swap(arr, i + 1, kanan)
    partisi = i + 1
    plot_array(arr, pivot_idx=partisi)
    time.sleep(delay)

    quick_sort_visual(arr, kiri, partisi - 1, delay)
    quick_sort_visual(arr, partisi + 1, kanan, delay)

# Streamlit UI
st.title("🔀 Visualisasi QuickSort Interaktif")

array_size = st.slider("Ukuran Array", 5, 20, 10)
kecepatan = st.slider("Kecepatan Animasi (detik)", 0.1, 1.0, 0.5, step=0.1)

if st.button("Mulai Visualisasi"):
    arr = random.sample(range(1, 100), array_size)
    st.write("📦 Array Awal:", arr)

    quick_sort_visual(arr, 0, len(arr) - 1, kecepatan)

    st.success("✅ QuickSort selesai!")
    st.write("📈 Array Terurut:", arr)
