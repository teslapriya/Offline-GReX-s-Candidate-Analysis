import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

# NetCDF files
file_paths = [
    '/hdd/data/voltages/grex_dump-241003aaao.nc',  
    '/hdd/data/voltages/grex_dump-241003aaap.nc',  
    '/hdd/data/voltages/grex_dump-241003aaan.nc',
    '/hdd/data/voltages/grex_dump-241003aaas.nc',
    '/hdd/data/voltages/grex_dump-241003aaat.nc',
]

freq_threshold = 1500
plt.figure(figsize=(12, 6))

highlight_color = '#ff7f0e'  # Bright blue for highlighting
light_color = '#1f77b4'  # Light blue for others
alpha_highlight = 1.0  # Opaque for highlighted
alpha_light = 0.5  

for file_path in file_paths:
    data = nc.Dataset(file_path)
    freq = data.variables['freq'][:]  # Shape (2048,)
    voltage = data.variables['voltages'][:]  # Shape (262144, 2, 2048, 2)

    # Calculate Stokes I
    V_H = voltage[:, 0, :, :]  # Horizontal polarization (H)
    V_V = voltage[:, 1, :, :]  # Vertical polarization (V)

    # intensity for both polarizations
    I_H = np.sqrt(V_H[..., 0]**2 + V_H[..., 1]**2)  
    I_V = np.sqrt(V_V[..., 0]**2 + V_V[..., 1]**2)  

    stokes_I = np.mean(I_H**2 + I_V**2, axis=0)  # Average over time

    mask = freq <= freq_threshold
    filtered_freq = freq[mask]
    filtered_stokes_I = stokes_I[mask]

    if "241003aaao" in file_path:
        plt.plot(filtered_freq, filtered_stokes_I, label=f'{file_path.split("/")[-1]}', 
                 color=highlight_color, alpha=alpha_highlight, linewidth=2)
    else:
        plt.plot(filtered_freq, filtered_stokes_I, label=f'{file_path.split("/")[-1]}', 
                 color=light_color, alpha=alpha_light, linewidth=1)

plt.xlabel('Frequency (MHz)', fontsize=14)
plt.ylabel('Power (Stoke I)', fontsize=14)
plt.title('Power(Stoke I) vs Frequency', fontsize=16)
plt.legend(fontsize=10)
plt.grid()
plt.tight_layout() 
plt.show()
