from database.connection import cursor

def create_table_monitoring():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitoring (
            Date DATE NOT NULL PRIMARY KEY,
            WaterConsumption DOUBLE NOT NULL,
            EnergyConsumption DOUBLE NOT NULL,
            NonRecycable DOUBLE NOT NULL,
            ValidRecycable DOUBLE NOT NULL,
            UsedTransport SMALLINT NOT NULL
        );
    """)

def create_table_monitoring_classifications():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitoring_classifications (
            Date DATE NOT NULL PRIMARY KEY,
            WaterSustentabilty VARCHAR(25) NOT NULL,
            EnergySustentabilty VARCHAR(25) NOT NULL,
            RecycableSustentabilty VARCHAR(25) NOT NULL,
            TransportationSustentability VARCHAR(25) NOT NULL,
            FOREIGN KEY (Date) REFERENCES monitoring(Date)
                ON DELETE CASCADE
        );
    """)