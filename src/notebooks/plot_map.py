import plotly.express as px
import pandas as pd

# 1. Prepare Data: Filter for Start (2000) and End (2020) Years
# We need country codes for the map, assuming 'code' column exists (e.g., ISO-3)
df_2000 = df[df['year'] == 2000][['entity', 'code', 'sh_alc_pcap_li']].rename(columns={'sh_alc_pcap_li': 'val_2000'})
df_2020 = df[df['year'] == 2020][['entity', 'code', 'sh_alc_pcap_li']].rename(columns={'sh_alc_pcap_li': 'val_2020'})

# 2. Merge to calculate difference
# Inner join to ensure we have data for both years for the country
df_map = pd.merge(df_2000, df_2020, on=['entity', 'code'], how='inner')

# 3. Calculate "Variation" (Difference)
df_map['change_liters'] = df_map['val_2020'] - df_map['val_2000']

# 4. Plot Choropleth Map
fig = px.choropleth(
    df_map,
    locations="code",             # Column with ISO country codes
    color="change_liters",        # Variable to color by
    hover_name="entity",          # Column to hover over
    hover_data=['val_2000', 'val_2020'],
    color_continuous_scale="Blues", # Blue shade colors
    title="Change in Alcohol Consumption per Capita (2000 - 2020)",
    labels={'change_liters': 'Change in Liters (Pure Alcohol)'}
)

fig.update_layout(
    coloraxis_colorbar=dict(
        title="Change (Liters)",
    )
)

fig.show()
