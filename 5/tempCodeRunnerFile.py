    if string.startswith("fertilizer"):
        processMap(fertilizer_to_water_map,strings,i)

    if string.startswith("water"):
        processMap(water_to_light_map,strings,i)

    if string.startswith("light"):
        processMap(light_to_temperature_map,strings,i)

    if string.startswith("temperature"):
        processMap(temperature_to_humudity_map,strings,i)