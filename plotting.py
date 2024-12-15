import plotly.graph_objects as go
from main import get_graphs

discharge_graph_dict, charge_graph_dict = get_graphs()

final_Re_dict, final_Rct_dict, final_BI_dict = {}, {}, {}
final_charge_Re_dict, final_charge_Rct_dict, final_charge_BI_dict = {}, {}, {}

for battery_id, values in discharge_graph_dict.items():
    final_Re_dict[battery_id] = [data[0] for data in values]
    final_Rct_dict[battery_id] = [data[1] for data in values]
    final_BI_dict[battery_id] = [data[2] for data in values]

for battery_id, values in charge_graph_dict.items():
    final_charge_Re_dict[battery_id] = [data[0] for data in values]
    final_charge_Rct_dict[battery_id] = [data[1] for data in values]
    final_charge_BI_dict[battery_id] = [data[2] for data in values]

def calculate_average(data_dict):
    """
    Calculate the average of each list of values in the dictionary.
    
    Args:
        data_dict (dict): Dictionary containing battery IDs as keys and lists of values as values.
    
    Returns:
        dict: Dictionary with the same keys but the values are the averages of the lists.
    """
    return {battery_id: sum(values) / len(values) for battery_id, values in data_dict.items()}

final_Re_dict = calculate_average(final_Re_dict)
final_Rct_dict = calculate_average(final_Rct_dict)
final_BI_dict = calculate_average(final_BI_dict)

final_charge_Re_dict = calculate_average(final_charge_Re_dict)
final_charge_Rct_dict = calculate_average(final_charge_Rct_dict)
final_charge_BI_dict = calculate_average(final_charge_BI_dict)

sorted_battery_ids = sorted(final_Re_dict.keys())
sorted_Re_values = [final_Re_dict[battery_id] for battery_id in sorted_battery_ids]
sorted_Rct_values = [final_Rct_dict[battery_id] for battery_id in sorted_battery_ids]
sorted_BI_values = [final_BI_dict[battery_id] for battery_id in sorted_battery_ids]
sorted_Re_charge_values = [final_charge_Re_dict[battery_id] for battery_id in sorted_battery_ids]
sorted_Rct_charge_values = [final_charge_Rct_dict[battery_id] for battery_id in sorted_battery_ids]
sorted_BI_charge_values = [final_charge_BI_dict[battery_id] for battery_id in sorted_battery_ids]

layout_settings = dict(
    template='plotly_dark',
    font=dict(family="Arial", size=12, color="white"),
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor="rgba(0, 0, 0, 0.5)"
    ),
    xaxis=dict(
        tickangle=-45,
        title_font=dict(size=14, color="white"),
        gridcolor='gray',
        zerolinecolor='gray'
    ),
    yaxis=dict(
        title_font=dict(size=14, color="white"),
        gridcolor='gray',
        zerolinecolor='gray'
    ),
    plot_bgcolor='black',
    paper_bgcolor='black',
    margin=dict(t=100, l=80, r=80, b=80)
)

def create_individual_plot(title, x, y, name, color):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x,
        y=y,
        name=name,
        marker=dict(color=color, line=dict(width=1, color=color))
    ))
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            y=0.95,
            font=dict(size=20, color="white")
        ),
        xaxis_title="Battery ID",
        yaxis_title="Value",
        **layout_settings
    )
    return fig

def create_combined_plot(title, x, discharge_y, charge_y, discharge_name, charge_name, discharge_color, charge_color):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x,
        y=discharge_y,
        name=discharge_name,
        marker=dict(color=discharge_color, line=dict(width=1, color=discharge_color))
    ))
    fig.add_trace(go.Bar(
        x=x,
        y=charge_y,
        name=charge_name,
        marker=dict(color=charge_color, line=dict(width=1, color=charge_color))
    ))
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            y=0.95,
            font=dict(size=20, color="white")
        ),
        xaxis_title="Battery ID",
        yaxis_title="Value",
        barmode='group',
        **layout_settings
    )
    return fig

fig_Re_discharge = create_individual_plot("Electrolyte Resistance (Re) - Discharge", sorted_battery_ids, sorted_Re_values, "Discharge", '#1f77b4')
fig_Re_charge = create_individual_plot("Electrolyte Resistance (Re) - Charge", sorted_battery_ids, sorted_Re_charge_values, "Charge", '#ff7f0e')

fig_Rct_discharge = create_individual_plot("Charge Transfer Resistance (Rct) - Discharge", sorted_battery_ids, sorted_Rct_values, "Discharge", '#2ca02c')
fig_Rct_charge = create_individual_plot("Charge Transfer Resistance (Rct) - Charge", sorted_battery_ids, sorted_Rct_charge_values, "Charge", '#d62728')

fig_BI_discharge = create_individual_plot("Battery Impedance - Discharge", sorted_battery_ids, sorted_BI_values, "Discharge", '#9467bd')
fig_BI_charge = create_individual_plot("Battery Impedance - Charge", sorted_battery_ids, sorted_BI_charge_values, "Charge", '#8c564b')

fig_Re_combined = create_combined_plot("Electrolyte Resistance (Re) Comparison", sorted_battery_ids, sorted_Re_values, sorted_Re_charge_values, "Discharge", "Charge", '#1f77b4', '#ff7f0e')
fig_Rct_combined = create_combined_plot("Charge Transfer Resistance (Rct) Comparison", sorted_battery_ids, sorted_Rct_values, sorted_Rct_charge_values, "Discharge", "Charge", '#2ca02c', '#d62728')
fig_BI_combined = create_combined_plot("Battery Impedance Comparison", sorted_battery_ids, sorted_BI_values, sorted_BI_charge_values, "Discharge", "Charge", '#9467bd', '#8c564b')

fig_Re_discharge.show()
fig_Re_charge.show()
fig_Rct_discharge.show()
fig_Rct_charge.show()
fig_BI_discharge.show()
fig_BI_charge.show()

fig_Re_combined.show()
fig_Rct_combined.show()
fig_BI_combined.show()
