import sqlite3
import json

# JSON data
data = '''
[
    {"dishName": "Jeera Rice", "dishId": "1", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg", "isPublished": true},
    {"dishName": "Paneer Tikka", "dishId": "2", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg", "isPublished": true},
    {"dishName": "Rabdi", "dishId": "3", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg", "isPublished": true},
    {"dishName": "Chicken Biryani", "dishId": "4", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg", "isPublished": true},
    {"dishName": "Alfredo Pasta", "dishId": "5", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg", "isPublished": true}
]
'''

# Parse JSON data
dishes = json.loads(data)

# Connect to SQLite database
conn = sqlite3.connect('dishes.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    dishId INTEGER PRIMARY KEY,
    dishName TEXT NOT NULL,
    imageUrl TEXT NOT NULL,
    isPublished BOOLEAN NOT NULL
)
''')

# Insert data
for dish in dishes:
    cursor.execute ( '''
        [
{
"dishName": "Jeera Rice",
"dishId": "1",
"imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg",
"isPublished": true 
 } ,
{
"dishName": "Paneer Tikka",
"dishId": "2",
"imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg",
"isPublished": true
},
{
"dishName": "Rabdi",
"dishId": "3",
"imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg",
"isPublished": true
},
{
"dishName": "Chicken Biryani",
"dishId": "4",
"imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg",
"isPublished": true
},
{
"dishName": "Alfredo Pasta",
"dishId": "5",
"imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg",
"isPublished": true
}
]
   ''')


conn.commit()
conn.close()
