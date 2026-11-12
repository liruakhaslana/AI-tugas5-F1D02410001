import json

with open("aturan_cas_hp.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("=" * 55)
print(data["judul"].upper())
print("=" * 55)
print("Metode yang digunakan:", data["metode"])
print("\nJawablah pertanyaan berikut dengan Ya atau Tidak.")
print("-" * 55)

fakta = set()
for gejala in data["gejala"]:
    while True:
        jawaban = input(gejala["pertanyaan"] + " (Ya/Tidak): ").lower().strip()

        if jawaban == "ya":
            fakta.add(gejala["kode"])
            break
        elif jawaban == "tidak":
            break
        else:
            print("Jawaban tidak valid. Masukkan Ya atau Tidak.")


# Proses Forward Chaining
print("\n" + "=" * 55)
print("PROSES IDENTIFIKASI")
print("=" * 55)

aturan_digunakan = []
hasil_diagnosis = []

perubahan = True
while perubahan:
    perubahan = False
    for aturan in data["aturan"]:
        if all(kondisi in fakta for kondisi in aturan["jika"]):
            if aturan["maka"] not in fakta:
                fakta.add(aturan["maka"])
                aturan_digunakan.append(aturan["id"])
                perubahan = True
                print(
                    aturan["id"],
                    "terpenuhi:",
                    "Maka",
                    data["kesimpulan"][aturan["maka"]]
                )
                if aturan["jenis"] == "diagnosis":
                    hasil_diagnosis.append(aturan["maka"])

print("\n" + "=" * 55)
print("HASIL IDENTIFIKASI")
print("=" * 55)

if hasil_diagnosis:
    for kode in hasil_diagnosis:
        print("-", data["kesimpulan"][kode])

    print("\nAturan yang digunakan:", ", ".join(aturan_digunakan))

else:
    print("Belum ditemukan kesimpulan berdasarkan gejala yang diberikan.")
    print("Silakan lakukan pemeriksaan lebih lanjut.")

print("\nCatatan:")
print("Hasil ini merupakan identifikasi awal, bukan diagnosis pasti.")
print("=" * 55)
print("Program selesai.")