import tkinter as tk
from tkinter import simpledialog, messagebox

sozluk = {
    "Ocean": "Okyanus",
    "River": "Nehir",
    "Lake": "Göl",
    "Mountain": "Dağ",
    "Valley": "Vadi",
    "Forest": "Orman",
    "Desert": "Çöl",
    "Island": "Ada",
    "Beach": "Plaj",
    "Hill": "Tepe",
    "Cave": "Mağara",
    "Volcano": "Volkan",
    "Glacier": "Buzul",
    "Peninsula": "Yarımada",
    "Bay": "Körfez",
    "Strait": "Boğaz",
    "Canal": "Kanal",
    "Plateau": "Plato",
    "Fjord": "Fiyort",
    "Tundra": "Tundra",
    "Marsh": "Bataklık",
    "Swamp": "Sazlık",
    "Stream": "Akarsu",
    "Creek": "Dere",
    "Ridge": "Sırt",
    "Peak": "Zirve",
    "Cliff": "Uçurum",
    "Dune": "Kumul",
    "Prairie": "Çayır",
    "Meadow": "Mera",
    "Savanna": "Savanna",
    "Steppe": "Bozkır",
    "Jungle": "Orman",
    "Rainforest": "Yağmur Ormanı",
    "Reef": "Mercan Kayalığı",
    "Oasis": "Vaha",
    "Gulf": "Körfez",
    "Sea": "Deniz",
    "Archipelago": "Takımada",
    "Atoll": "Mercan Adası",
    "Lagoon": "Lagün",
    "Delta": "Delta",
    "Estuary": "Estuary",
    "Firth": "Firth",
    "Harbor": "Liman",
    "Sound": "Ses",
    "Bight": "Koy",
    "Cove": "Koy",
    "Inlet": "Giriş",
    "Narrows": "Darlık",
    "Channel": "Kanal",
    "Tributary": "Nehir",
    "Brook": "Çay",
    "Spring": "Kaynak",
    "Waterfall": "Şelale",
    "Geyser": "Gayzer",
    "Pond": "Gölet",
    "Reservoir": "Baraj",
    "Aqueduct": "Su Kemeri",
    "Dam": "Baraj",
    "Levee": "Set",
    "Dike": "Set",
    "Slough": "Slough",
    "Wetland": "Sulak Alan",
    "Bog": "Bataklık",
    "Fen": "Fen",
    "Moor": "Moor",
    "Peatland": "Turba Alanı",
    "Quagmire": "Bataklık",
    "Mire": "Çamur",
    "Silt": "Çamur",
    "Mud": "Çamur",
    "Sand": "Kum",
    "Gravel": "Çakıl",
    "Rock": "Kaya",
    "Stone": "Taş",
    "Boulder": "Büyük Kaya",
    "Ledge": "Kaya Çıkıntısı",
    "Outcrop": "Kaya Oluşumu",
    "Bedrock": "Ana Kayası"

}




# Arama fonksiyonu
def kelime_ara():
    giris = simpledialog.askstring("Kelime Girişi", "Aranacak kelimeyi giriniz:")
    if giris in sozluk:
        messagebox.showinfo("Sonuç", f"'{giris}' kelimesinin anlamı: {sozluk[giris]}")
    else:
        messagebox.showwarning("Uyarı", "Girdiğiniz kelime sözlükte bulunamadı.")


root = tk.Tk()
root.geometry("300x200")
root.title("Sözlük Uygulaması")


ara_butonu = tk.Button(root, text="Kelime Ara", command=kelime_ara)
ara_butonu.pack(pady=20)


root.mainloop()
