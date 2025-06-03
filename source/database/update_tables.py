from database.connection import cursor, conn

def update_monitoring_table(date, water_consumption_update, energy_consumption_update, non_recycable_trash_update, valid_recycable_update, used_transport_update, transportation_sustentability_classification_update, recycable_sustentabilty_classification_update, energy_sustentabilty_classification_update, water_sustentabilty_classification_update):
    try:
        cursor.execute("""UPDATE monitoring
                    SET WaterConsumption = %s,
                    EnergyConsumption = %s,
                    NonRecycable = %s,
                    ValidRecycable = %s,  
                    UsedTransport = %s WHERE Date=%s;""", (water_consumption_update, energy_consumption_update, non_recycable_trash_update, valid_recycable_update, used_transport_update, date))
        
        conn.commit()

        cursor.execute("""UPDATE monitoring_classifications
                       SET WaterSustentabilty = %s,
                       EnergySustentabilty = %s,
                       RecycableSustentabilty = %s,
                       TransportationSustentability = %s
                       WHERE Date = %s;
                    """, (water_sustentabilty_classification_update, energy_sustentabilty_classification_update, recycable_sustentabilty_classification_update, transportation_sustentability_classification_update, date))
        
        conn.commit()

    except:
        return False

    else:
        return True