import sqlite3  
  
con = sqlite3.connect("sse_resources.db")  
print("Database opened successfully")  
  
con.execute("create table resources (resource_id INTEGER PRIMARY KEY AUTOINCREMENT, \
    resource_name TEXT NOT NULL, resource_description TEXT NOT NULL, \
    resource_details TEXT NOT NULL, pre_sse TEXT NOT NULL, group_1 TEXT NOT NULL, \
    group_2 TEXT NOT NULL, group_3 TEXT NOT NULL, group_4 TEXT NOT NULL, \
    story TEXT NOT NULL, activity TEXT NOT NULL, quote TEXT NOT NULL, \
    life_application TEXT NOT NULL, role_model TEXT NOT NULL, ethical_dilemma TEXT NOT NULL, \
    book TEXT NOT NULL, truth TEXT NOT NULL, right_conduct TEXT NOT NULL, peace TEXT NOT NULL, \
    love TEXT NOT NULL, non_violence TEXT NOT NULL, self_discipline TEXT NOT NULL, \
    forbearance TEXT NOT NULL, duty TEXT NOT NULL, devotion TEXT NOT NULL, discrimination TEXT NOT NULL, \
    determination TEXT NOT NULL, purity TEXT NOT NULL, perseverance TEXT NOT NULL, \
    patience TEXT NOT NULL, selfless_service TEXT NOT NULL, honesty TEXT NOT NULL, \
    compassion TEXT NOT NULL, forgiveness TEXT NOT NULL, kindness TEXT NOT NULL, \
    tolerance TEXT NOT NULL, cleanliness TEXT NOT NULL, contentment TEXT NOT NULL, \
    courage TEXT NOT NULL, gratitude TEXT NOT NULL, sacrifice TEXT NOT NULL, \
    self_confidence TEXT NOT NULL, humility TEXT NOT NULL, self_control TEXT NOT NULL, \
    ceiling_on_desires TEXT NOT NULL, unity_in_thought_word_and_deed TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  
