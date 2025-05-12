import streamlit as st
import matplotlib.pyplot as plt
import time
import random

# Fungsi untuk menggambar array sebagai batang
def plot_array(arr, color_array):
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=color_array)
    plt.xlabel("Index")
    plt.ylabel("Value")
    st.pyplot(fig)
    plt.close(fig)

# Fungsi swap
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Fungsi quicksort dengan visualisasi
def quick_sort_visual(arr, kiri, kanan):
    if kiri >= kanan:
        return

    pivot = arr[kanan]
    i = kiri - 1

    for j in range(kiri, kanan):
        color_array = ['blue'] * len(arr)
        color_array[kanan] = 'red'  # pivot
        color_array[j] = 'yellow'   # current
        plot_array(arr, color_array)
        time.sleep(0.3)

        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, kanan)
    partisi = i + 1

    # Tampilkan array setelah partisi
    color_array = ['green' if x == partisi else 'blue' for x in range(len(arr))]
    plot_array(arr, color_array)
    time.sleep(0.5)

    quick_sort_visual(arr, kiri, partisi - 1)
    quick_sort_visual(arr, partisi + 1, kanan)

# Streamlit App
st.title("Visualisasi QuickSort")
array_size = st.slider("Ukuran Array", min_value=5, max_value=30, value=10)
if st.button("Mulai QuickSort"):
    arr = random.sample(range(1, 100), array_size)
    st.write("Array Awal:", arr)
    quick_sort_visual(arr, 0, len(arr) - 1)
    st.success("Selesai! Array sudah diurutkan.")
    st.write("Array Terurut:", arr)
