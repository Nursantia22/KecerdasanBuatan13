import random

subjects = ["komputer", "internet", "robot", "sensor", "blockchain", "augmented reality", "kecerdasan buatan"]
predicates = ["menghubungkan", "mengatur", "mengendalikan", "mendeteksi", "memudahkan", "memastikan", "membantu", "mengembangkan"]
objects = ["jaringan", "pengguna", "data", "perangkat", "lingkungan", "sistem", "produksi", "komunikasi"]
keterangan = ["dengan cepat", "secara otomatis", "tanpa kabel", "di masa depan", "secara real-time", "dalam industri", "melalui internet", "untuk efisiensi"]

def buat_kalimat():
    s = random.choice(subjects)
    p = random.choice(predicates)
    o = random.choice(objects)
    k = random.choice(keterangan)
    return f"{s.capitalize()} {p} {o} {k}."

print("Kalimat Teknologi yang Dihasilkan:\n")
for i in range(5):
    print(f"{i+1}. {buat_kalimat()}")
