import sqlite3

# Create & Connect to Database
conn = sqlite3.connect("face_database.db")
cursor = conn.cursor()

# Create Users Table (if it doesn't already exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    address TEXT,
    image_path TEXT
)
""")

# Insert Data for 20 Users
users = [
    ("Maneesh Rajpoot", 21, "Jalesar, Etah", "faces/maneeshrajpoot.jpg"),
    ("Manish Gautam", 22, "Agra, UP", "faces/manishgautam.jpg"),
    ("Manoj Nigam", 23, "Agra, sector14", "faces/manojnigam.jpg"),
    ("Md Billal", 20, "KatgharLohamandi, Agra", "faces/mdbillal.jpg"),
    ("Tilak Rajpoot", 19, "Etah, UP82", "faces/tilakrajpoot.jpg"),
    ("Vievk Kumar", 19.5, "Veernagar, Jalesar", "faces/vivekkumar.jpg"),
    ("Vivek Sharma", 24, "Sadabad, Hathras", "faces/viveksharma.jpg"),
    ("Alok Tiwari", 27, "Lucknow, India", "faces/alok.jpg"),
    ("Pooja Singh", 23, "Jaipur, India", "faces/pooja.jpg"),
    ("Vikas Chauhan", 32, "Noida, India", "faces/vikas.jpg"),
    ("Ritu Sharma", 26, "Nagpur, India", "faces/ritu.jpg"),
    ("Manoj Joshi", 29, "Indore, India", "faces/manoj.jpg"),
    ("Anjali Nair", 31, "Kerala, India", "faces/anjali.jpg"),
    ("Sahil Arora", 34, "Ahmedabad, India", "faces/sahil.jpg"),
    ("Kavita Das", 28, "Patna, India", "faces/kavita.jpg"),
    ("Rohan Malhotra", 22, "Chandigarh, India", "faces/rohan.jpg"),
    ("Sunita Mishra", 36, "Bhopal, India", "faces/sunita.jpg"),
    ("Deepak Thakur", 30, "Surat, India", "faces/deepak.jpg"),
    ("Meenal Jain", 25, "Udaipur, India", "faces/meenal.jpg"),
    ("Yashwant Rao", 38, "Raipur, India", "faces/yashwant.jpg")
]

cursor.executemany("INSERT INTO users (name, age, address, image_path) VALUES (?, ?, ?, ?)", users)
conn.commit()
conn.close()

print("✅ Database Created Successfully!")