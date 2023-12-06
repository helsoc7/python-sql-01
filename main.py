import sqlite3

# Datenbank und Tabellen erstellen
def create_datenbank():
    # Mit der Datenbank verbinden
    connection = sqlite3.connect("Schulung.db")
    cursor = connection.cursor()

    # Führe SQL-Befehl aus
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Teilnehmer(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100),
            Age INTEGER,
            Email VARCHAR(100)
        )'''
    )

    # Führe den Befehl aus
    connection.commit()

    # Verbindung wieder schließen
    connection.close()

# Teilnehmer hinzufügen
def insert_tn(name, age, email):
    # Mit der Datenbank verbinden
    connection = sqlite3.connect("Schulung.db")
    cursor = connection.cursor()

    # Führe SQL-Befehl aus
    cursor.execute(
        '''
        INSERT INTO Teilnehmer(Name, Age, Email) VALUES (?,?,?)
        ''',
        (name, age, email)
    )

    # Führe den Befehl aus
    connection.commit()

    # Schließe Verbindung
    connection.close()

# Gib uns alle Datensätze der Tabelle aus
def select_tn():
    connection = sqlite3.connect("Schulung.db")
    cursor = connection.cursor()

    # Definiere SQL-Befehl
    cursor.execute(
        '''
        SELECT * FROM Teilnehmer;
        '''
    )

    teilnehmer = cursor.fetchall()

    for i in teilnehmer:
        print(i)

    connection.commit()
    
    connection.close()

create_datenbank()
#name = input("Bitte gib deinen Namen ein: ")
#age_str = input("Bitte gib dein Alter ein: ")
#age = int(age_str)
#email = input("Bitte gib deine E-Mail-Adresse ein: ")
#insert_tn(name, age, email)
select_tn()




