import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['lines.linewidth'] = 0.7

def plot_from_csv(input_csv, output_plot):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['V(OUTPUT)'])  
    plt.xlabel('Time')
    plt.ylabel('V(OUTPUT)')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig(output_plot.replace('.svg', '_full.svg'))

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'][7000:7300], df['V(OUTPUT)'][7000:7300])  
    plt.xlabel('Time')
    plt.ylabel('V(OUTPUT)')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig(output_plot)

    zoom_df = df.iloc[7000:8000]
    signal = zoom_df['V(OUTPUT)']
    fft_result = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), d=(zoom_df['Time'].iloc[1] - zoom_df['Time'].iloc[0]))

    mask = (freq>1e9) & (freq<5e9)
    freq_pos = freq[mask]
    fft_result_pos = fft_result[mask]

    plt.figure(figsize=(10, 6))
    plt.plot(freq_pos, np.abs(fft_result_pos))  
    plt.xlabel('f')
    plt.ylabel('FFT')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig(output_plot.replace('.svg', '_fft.svg'))

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_csv output_plot")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_plot = sys.argv[2]
    plot_from_csv(input_csv, output_plot)