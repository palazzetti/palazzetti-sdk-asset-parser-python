class AssetCapabilities(object):

    def __init__(self, props):
        self._flag_has_ecostart = props.get("flag_modalita_ecostart", False)
        self._flag_has_time_sync = props.get("flag_sincronizzazione_orario", False)
        self._flag_has_chrono = props.get("flag_presenza_chrono", False)
        self._flag_has_setpoint = props.get("flag_impostazione_setpoint", False)
        self._flag_has_switch_on_off = props.get("flag_accensione_macchina", False)
        self._flag_error_status = props.get("flag_presenza_errore_macchina", False)

        self._flag_has_switch_on_multifire_pellet = props.get("flag_prenotazione_accensione_pellet", False)
        self._flag_is_air = props.get("flag_tipologia_aria", False)
        self._flag_is_hydro = props.get("flag_tipologia_idro", False)
        self._flag_has_fan = props.get("flag_presenza_ventilatore", False)
        self._value_fan_function_first = props.get("value_fan_function_first", None)
        
        self._flag_has_fan_zero_speed_fan = props.get("flag_presenza_zero_speed_fan", False)
        self._flag_has_fan_mode_auto = props.get("flag_presenza_ventilatore_mod_auto", False)
        self._flag_has_fan_mode_high = props.get("flag_presenza_ventilatore_mod_high", False)
        self._flag_has_fan_mode_prop = props.get("flag_presenza_ventilatore_mod_prop", False)
        self._flag_has_fan_main = props.get("flag_presenza_primo_ventilatore", False)
        self._flag_has_fan_second = props.get("flag_presenza_secondo_ventilatore", False)
        self._flag_has_fan_third = props.get("flag_presenza_terzo_ventilatore", False)
        self._flag_has_pellet_sensor_leveltronic = props.get("flag_presenza_sensore_pellet_leveltronic", False)
        self._flag_has_pellet_sensor_capacitive = props.get("flag_presenza_sensore_pellet_capacitivo", False)
        
        self._value_leveltronic_min = props.get("value_leveltronic_minimo", None)
        self._value_leveltronic_treshold = props.get("value_leveltronic_soglia", None)
        self._value_leveltronic_level = props.get("value_leveltronic_level", None)
        
        self._flag_has_temp_combustion = props.get("flag_presenza_temperatura_combustione", False)
        self._flag_has_door_control = props.get("flag_presenza_porta", False)
        self._flag_has_light_control = props.get("flag_presenza_luci", False)
        
        self._value_product_type = props.get("value_tipologia_macchina", None)
        self._value_product_is_on = props.get("value_accensione_macchina", None)
        self._value_temp_air_description = props.get("value_descrizione_temperatura_aria", None)
        self._value_temp_hydro_description = props.get("value_descrizione_temperatura_idro", None)
        self._value_temp_hydro_t1_description = props.get("value_descrizione_sonda_t1_idro", None)
        
        self._value_temp_main = props.get("value_temperatura_sonda_principale", None)
        self._value_temp_main_description = props.get("value_descrizione_sonda_principale", None)
        
        self._value_temp_hydro_t1 = props.get("value_temperatura_sonda_t1_idro", None)
        self._value_temp_hydro_t2 = props.get("value_temperatura_sonda_t2_idro", None)
        self._value_temp_wood_combustion = props.get("value_temperatura_sonda_combustione_legna", None)
        
        self._value_power_current = props.get("value_power_rilevato", None)
        self._value_setpoint_min = props.get("value_setpoint_minimo", None)
        self._value_setpoint_max = props.get("value_setpoint_massimo", None)
        self._value_setpoint = props.get("value_setpoint_impostato", None)
        self._value_power = props.get("value_power_impostato", None)
        
        self._value_fan_main = props.get("value_fan_first", None)
        self._value_fan_second = props.get("value_fan_second", None)
        self._value_fan_third = props.get("value_fan_third", None)
        self._value_fan_limits = props.get("value_fan_limits", None)
        
        self._value_door_status = props.get("value_apertura_porta", None)
        self._value_light_status = props.get("value_accensione_luce", None)

    @property
    def flag_has_ecostart(self):
        return self._flag_has_ecostart

    @property    
    def flag_has_time_sync(self):
        return self._flag_has_time_sync

    @property    
    def flag_has_chrono(self):
        return self._flag_has_chrono

    @property    
    def flag_has_setpoint(self):
        return self._flag_has_setpoint

    @property    
    def flag_has_switch_on_off(self):
        return self._flag_has_switch_on_off

    @property    
    def flag_error_status(self):
        return self._flag_error_status

    @property    
    def flag_has_switch_on_multifire_pellet(self):
        return self._flag_has_switch_on_multifire_pellet

    @property    
    def flag_is_air(self):
        return self._flag_is_air

    @property    
    def flag_is_hydro(self):
        return self._flag_is_hydro

    @property    
    def flag_has_fan(self):
        return self._flag_has_fan

    @property    
    def value_fan_function_first(self):
        return self._value_fan_function_first

    @property    
    def flag_has_fan_zero_speed_fan(self):
        return self._flag_has_fan_zero_speed_fan

    @property    
    def flag_has_fan_mode_auto(self):
        return self._flag_has_fan_mode_auto

    @property    
    def flag_has_fan_mode_high(self):
        return self._flag_has_fan_mode_high

    @property    
    def flag_has_fan_mode_prop(self):
        return self._flag_has_fan_mode_prop

    @property    
    def flag_has_fan_main(self):
        return self._flag_has_fan_main

    @property    
    def flag_has_fan_second(self):
        return self._flag_has_fan_second

    @property    
    def flag_has_fan_third(self):
        return self._flag_has_fan_third

    @property    
    def flag_has_pellet_sensor_leveltronic(self):
        return self._flag_has_pellet_sensor_leveltronic

    @property    
    def flag_has_pellet_sensor_capacitive(self):
        return self._flag_has_pellet_sensor_capacitive

    @property    
    def value_leveltronic_min(self):
        return self._value_leveltronic_min

    @property    
    def value_leveltronic_treshold(self):
        return self._value_leveltronic_treshold

    @property    
    def value_leveltronic_level(self):
        return self._value_leveltronic_level

    @property    
    def flag_has_temp_combustion(self):
        return self._flag_has_temp_combustion

    @property    
    def flag_has_door_control(self):
        return self._flag_has_door_control

    @property    
    def flag_has_light_control(self):
        return self._flag_has_light_control

    @property    
    def value_product_type(self):
        return self._value_product_type

    @property    
    def value_product_is_on(self):
        return self._value_product_is_on

    @property    
    def value_temp_air_description(self):
        return self._value_temp_air_description

    @property    
    def value_temp_hydro_description(self):
        return self._value_temp_hydro_description

    @property    
    def value_temp_hydro_t1_description(self):
        return self._value_temp_hydro_t1_description

    @property    
    def value_temp_main(self):
        return self._value_temp_main

    @property    
    def value_temp_main_description(self):
        return self._value_temp_main_description

    @property    
    def value_temp_hydro_t1(self):
        return self._value_temp_hydro_t1

    @property    
    def value_temp_hydro_t2(self):
        return self._value_temp_hydro_t2

    @property    
    def value_temp_wood_combustion(self):
        return self._value_temp_wood_combustion

    @property    
    def value_power_current(self):
        return self._value_power_current

    @property    
    def value_setpoint_min(self):
        return self._value_setpoint_min

    @property    
    def value_setpoint_max(self):
        return self._value_setpoint_max

    @property    
    def value_setpoint(self):
        return self._value_setpoint

    @property    
    def value_power(self):
        return self._value_power

    @property    
    def value_fan_main(self):
        return self._value_fan_main

    @property    
    def value_fan_second(self):
        return self._value_fan_second

    @property    
    def value_fan_third(self):
        return self._value_fan_third

    @property    
    def value_fan_limits(self):
        return self._value_fan_limits

    @property    
    def value_door_status(self):
        return self._value_door_status

    @property    
    def value_light_status(self):
        return self._value_light_status