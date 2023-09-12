DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,

    groups_id INT,
    FOREIGN KEY (groups_id) REFERENCES groups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)  NOT NULL,
    teachers_id INT,
    FOREIGN KEY ( teachers_id) REFERENCES  teachers (id)
       ON DELETE SET NULL
       ON UPDATE CASCADE
);

DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    student_id INT,
    subject_id INT,
    date_of TIMESTAMP DEFAULT CURRENT_TIMESTAMP  NOT NULL,
    grade  INTEGER,

    FOREIGN KEY (student_id) REFERENCES  students (id)
    FOREIGN KEY (subject_id) REFERENCES  subjects (id)
      ON DELETE SET NULL

);

