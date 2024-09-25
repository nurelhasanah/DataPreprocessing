#1. Memuat Data
#a. Import library yang diperlukan yaitu Pandas
import pandas as pd

#b. Memuat data dari file CSV kedalam Data Frame
df = pd.read_csv('C:/Users/Asus/Downloads/movie_sample_dataset.csv')

#2. Memeriksa Data
#a. Tampilkan beberapa baris pertama dari dataset untuk memahami struktur data
print("Tampilan beberapa baris pertama dari dataset untuk memahami struktur data")
print("                     ")
print(df.head())

#b. Periksa informasi umum tentang dataset, termasuk tipe data dan nilai yang hilang
import numpy as np
# Mengganti "nan" dengan " "
df['director_name'] = df['director_name'].replace(['Nan', 'Null'], '', regex=True)

# Memeriksa jumlah missing values di setiap kolom
print("Tampilan jumlah missing values di setiap kolom")
print("                     ")
print(df.isnull().sum())

#3. Membersihkan Data
#a. Menghapus baris dengan missing values pada kolom "gross"
df_cleaned1 = df.dropna(subset=["gross"], axis=0, inplace=True)

# Reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#b. Menghapus baris dengan missing values pada kolom "budget"
df_cleaned2 = df.dropna(subset=["budget"], axis=0, inplace=True)

# Reset index setelah menghapus baris
df.reset_index(drop=True, inplace=True)

#c. Atasi nilai yang tidak konsisten atau kesalahan penulisan di kolom
# seperti perbedaan antara "Color" dan "color" serta "USA" dan "usa"
# Mengatasi perbedaan antara "Color" dan "color" atau inkonsistensi serupa pada kolom.
# Misalnya, kita akan mengubah nilai dalam kolom "color" menjadi huruf kecil semua
if 'color' in df.columns:
    df['color'] = df['color'].str.lower()  # Ubah semua nilai di kolom "color" menjadi huruf kecil
print(df.head())

# Selanjutnya, kita akan mengubah nilai dalam kolom "usa" menjadi huruf "USA"
if 'country' in df.columns:
    df['country'] = df['country'].str.upper()  # Ubah semua nilai di kolom "usa" menjadi "USA"
print(df.head())

#d. Ubah atau hapus nilai-nilai yang tidak standar
# seperti nilai negatif atau "NaN"
# Mengubah nilai negatif pada kolom 'duration' dan 'imdb_score'
# Mengganti nilai negatif dengan NaN
df['duration'] = df['duration'].apply(lambda x: x if x >= 0 else np.nan)
df['imdb_score'] = df['imdb_score'].apply(lambda x: x if x >= 0 else np.nan)

# Mengganti dengan frekuensi pada kolom 'color', 'director name', dan 'genres', duration', dan 'imdb_score'
for column in ['color', 'director_name', 'genres', 'duration', 'imdb_score']:

    # Menentukan nilai yang paling sering muncul (mode)
    mode_value = df[column].mode()[0]

    # Mengganti nilai N/A dengan nilai yang paling sering muncul
    df[column].fillna(mode_value, inplace=True)
    mode_value = df['director_name'].mode()[0]  # Mendapatkan nilai yang paling sering muncul
    df['director_name'].replace('', mode_value, inplace=True)  # Mengganti string kosong dengan mode

#4. Transformasi Data
#a. Ubah tipe data kolom menjadi tipe data yang sesuai
print(df.dtypes)
df['genres'] = df['genres'].astype(str)
print(df['genres'])


#Tidak ada yang diubah karena tipe data sudah sesuai
#Variabel numerik (int atau float) dan variabel kategorik (string atau object)

#b. Normalisasi teks untuk memastikan konsistensi
# (misalnya mengubah teks menjadi huruf kecil)
# Melakukan normalisasi teks untuk kolom 'color', 'director_name', 'genres', 'movie_title',
# 'language', 'country', dan 'actors'
columns_to_normalize = ['color', 'director_name', 'genres', 'movie_title', 'language', 'country', 'actors']

for column in columns_to_normalize:
    df[column] = df[column].str.lower()  # Mengubah teks menjadi huruf kecil
    df[column] = df[column].str.strip()  # Menghapus spasi di awal dan akhir teks

#5. Penyimpanan Data
df.to_csv('C:/Users/Asus/Downloads/movie_dataset_cleaned.csv', index=False)