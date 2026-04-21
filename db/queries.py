students_table = """
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER NOT NULL,
        sex TEXT NOT NULL,
        major TEXT NOT NULL
    )
"""


insert_student = 'INSERT INTO students (name, surname, age, sex, major) VALUES (?, ?, ?, ?, ?)'


select_student = 'SELECT * FROM students'


update_student = '''
UPDATE students 
SET name = ?, surname = ?, age = ?, sex = ?, major = ? 
WHERE id = ?
'''


delete_student = 'DELETE FROM students WHERE id = ?'
