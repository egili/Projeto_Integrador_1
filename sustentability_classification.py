
def define_sustentabilty_classification(consumption: float, first_range: int, second_range: int) -> str:
    if consumption <= first_range:
        return 'Alta sustentabilidade'
    elif consumption <= second_range:
        return 'Média sustentabilidade'
    else:
        return 'Baixa sustentabilidade'

def define_water_sustentabilty_classification(water_consumption: float) -> str:
    return define_sustentabilty_classification(water_consumption, 150, 200)
        
def define_energy_sustentabilty_classification(energy_consumption: float) -> str:
    return define_sustentabilty_classification(energy_consumption, 5, 10)
        
def define_recycable_sustentabilty_classification(non_recycable_trash: float) -> str:
    if non_recycable_trash <= 20:
        return 'Baixa sustentabilidade'
    elif non_recycable_trash <=50:
        return 'Média sustentabilidade'
    else:
        return 'Alta sustentabilidade'

def define_transportation_sustentability_classification(used_transport: int) -> str:
    if used_transport == 1 or used_transport == 2 or used_transport == 3 or used_transport == 5:
        return 'Alta sustentabilidade'
    elif used_transport == 5 or used_transport == 6:
        return 'Média sustentabilidade'
    else:
        return 'Baixa sustentabilidade'
