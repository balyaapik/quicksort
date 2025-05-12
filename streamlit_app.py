import streamlit as st
import matplotlib.pyplot as plt
import random
import time

# Fungsi untuk menampilkan array dengan warna berdasarkan peran indeks
def plot_array(arr, pivot_idx=None, i_idx=None, j_idx=None):
    colors = []
    for idx in range(len(arr)):
        if idx == pivot_idx:
            colors.append("red")     # Pivot
        elif idx == j_idx:
            colors.append("yellow")  # J
        elif idx == i_idx:
            colors.append("green")   # I
        else:
            colors.append("blue")    # Default
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=colors)
    st.pyplot(fig)
    plt.close(fig)

# Fungsi swap
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Algoritma QuickSort dengan visualisasi
def quick_sort_visual(arr, kiri, kanan):
    if kiri >= kanan:
        return

    pivot = arr[kanan]
    i = kiri - 1
    pivot_idx = kanan

    for j in range(kiri, kanan):
        plot_array(arr, pivot_idx=pivot_idx, i_idx=i, j_idx=j)
        time.sleep(0.5)

        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
            plot_array(arr, pivot_idx=pivot_idx, i_idx=i, j_idx=j)
            time.sleep(0.5)

    swap(arr, i + 1, kanan)
    partisi = i + 1
    plot_array(arr, pivot_idx=partisi)
    time.sleep(0.5)

    quick_sort_visual(arr, kiri, partisi - 1)
    quick_sort_visual(arr, partisi + 1, kanan)

# Streamlit UI
st.title("🔀 Visualisasi QuickSort Interaktif")

array_size = st.slider("Ukuran Array", 5, 20, 10)
kecepatan = st.slider("Kecepatan Animasi (detik)", 0.1, 1.0, 0.5, step=0.1)

if st.button("Mulai Visualisasi"):
    arr = random.sample(range(1, 100), array_size)
    st.write("📦 Array Awal:", arr)
    
    # Set kecepatan global
    time.sleep = lambda x: time.sleep(kecepatan)
    
    quick_sort_visual(arr, 0, len(arr) - 1)
    
    st.success("✅ QuickSort selesai!")
    st.write("📈 Array Terurut:", arr)
