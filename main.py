import pandas as pd
import os

METADATA_CSV_PATH = "metadata.csv"

metadata_csv_data = pd.read_csv(METADATA_CSV_PATH)

def process_discharge_data(data_list):
    """
    Process discharge data from a list of strings and convert them into a dictionary.
    
    Args:
        data_list (list): List of strings representing discharge data, where each entry is comma-separated.
    
    Returns:
        dict: Dictionary of discharge data categorized by the respective column headers.
    """
    all_columns = data_list[0].split(",")
    
    voltage_measured = all_columns[0]
    current_measured = all_columns[1]
    temperature_measured = all_columns[2]
    current_load = all_columns[3]
    voltage_load = all_columns[4]
    time = all_columns[5]

    discharge_dict = {
        voltage_measured: [],
        current_measured: [],
        temperature_measured: [],
        current_load: [],
        voltage_load: [],
        time: []
    }

    for data in data_list[1:]:
        voltage, current, temp, load, voltage_l, time_val = data.split(",")
        discharge_dict[voltage_measured].append(voltage)
        discharge_dict[current_measured].append(current)
        discharge_dict[temperature_measured].append(temp)
        discharge_dict[current_load].append(load)
        discharge_dict[voltage_load].append(voltage_l)
        discharge_dict[time].append(time_val)
    
    return discharge_dict

def process_charge_data(data_list):
    """
    Process charge data from a list of strings and convert them into a dictionary.
    
    Args:
        data_list (list): List of strings representing charge data, where each entry is comma-separated.
    
    Returns:
        dict: Dictionary of charge data categorized by the respective column headers.
    """
    voltage_measured, current_measured, temperature_measured, current_charge, voltage_charge, time = data_list[0].split(",")
    
    charge_dict = {
        voltage_measured: [],
        current_measured: [],
        temperature_measured: [],
        current_charge: [],
        voltage_charge: [],
        time: []
    }

    for data in data_list[1:]:
        voltage, current, temp, charge, voltage_l, time_val = data.split(",")
        charge_dict[voltage_measured].append(voltage)
        charge_dict[current_measured].append(current)
        charge_dict[temperature_measured].append(temp)
        charge_dict[current_charge].append(charge)
        charge_dict[voltage_charge].append(voltage_l)
        charge_dict[time].append(time_val)
    
    return charge_dict

discharge_graph_dict = {}
charge_graph_dict = {}

def get_graphs():
    global discharge_graph_dict, charge_graph_dict
    for _, row in metadata_csv_data.iterrows():
        op_type = row["type"]
        battery_id = row["battery_id"]
        file_name = row["filename"]
        file_path = os.path.join("data", file_name)

        if op_type == "discharge":
            if battery_id not in discharge_graph_dict:
                discharge_graph_dict[battery_id] = []
            with open(file_path, "r") as f:
                file_data = f.readlines()
            
            discharge_data_dict = process_discharge_data(file_data)
            voltage_measured = [float(v) for v in discharge_data_dict["Voltage_measured"] if v.strip()]
            current_measured = [float(i) for i in discharge_data_dict["Current_measured"] if i.strip()]
            
            V1, V2 = voltage_measured[0], voltage_measured[1]
            I1, I2 = current_measured[0], current_measured[1]
            
            Re = (V2 - V1) / abs(I2 - I1)
            Voc = voltage_measured[0]
            Vss = sum(voltage_measured) / len(voltage_measured)
            Iss = sum(current_measured) / len(current_measured)

            dVss = Voc - Vss
            Rct = dVss / Iss
            battery_impedance = Re - Rct

            discharge_graph_dict[battery_id].append([Re, Rct, battery_impedance])

        elif op_type == "charge":
            if battery_id not in charge_graph_dict:
                charge_graph_dict[battery_id] = []
            with open(file_path, "r") as f:
                file_data = f.readlines()
            
            charge_data_dict = process_charge_data(file_data)
            voltage_measured = [float(v) for v in charge_data_dict["Voltage_measured"] if v.strip()]
            current_measured = [float(i) for i in charge_data_dict["Current_measured"] if i.strip()]
            
            V1, V2 = voltage_measured[0], voltage_measured[1]
            I1, I2 = current_measured[0], current_measured[1]
            
            Re = (V2 - V1) / abs(I2 - I1)
            Voc = voltage_measured[0]
            Vss = sum(voltage_measured) / len(voltage_measured)
            Iss = sum(current_measured) / len(current_measured)

            dVss = Voc - Vss
            Rct = dVss / Iss
            battery_impedance = Re - Rct

            charge_graph_dict[battery_id].append([Re, Rct, battery_impedance])

    return discharge_graph_dict, charge_graph_dict
