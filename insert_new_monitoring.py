from database.connection import cursor, conn

def insert_monitoring(date, water_consumption, energy_consumption, non_recycable_trash, valid_recycable, used_transport, transportation_sustentability_classification, recycable_sustentabilty_classification, energy_sustentabilty_classification, water_sustentabilty_classification):
    try:
        cursor.execute("INSERT INTO monitoring"
                    "(Date, WaterConsumption, EnergyConsumption, NonRecycable, ValidRecycable, UsedTransport)"
                    "VALUES"
                    "(%s, %s, %s, %s, %s, %s);", (date, water_consumption, energy_consumption, non_recycable_trash, valid_recycable, used_transport))
        
        conn.commit()

        cursor.execute("INSERT INTO monitoring_classifications"
                       "(Date, WaterSustentabilty, EnergySustentabilty, RecycableSustentabilty, TransportationSustentability)"
                       "VALUES"
                       "(%s, %s, %s, %s, %s);", (date, water_sustentabilty_classification, energy_sustentabilty_classification, recycable_sustentabilty_classification, transportation_sustentability_classification))
        
        conn.commit()
    
    except:
        print("[ Houve um erro ao tentar inserir o novo monitoramento no banco de dados! Verique a integridade do servidor MySQL. ]")

        return False

    else:
        return True