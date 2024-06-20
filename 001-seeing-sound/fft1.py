import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
T = 1      # Duration in seconds
t = np.linspace(0, T, int(T*fs), endpoint=False)

# Create a synthetic complex wave
frequencies = [50, 120, 300]
amplitudes = [1, 0.5, 0.8]
phases = [0, np.pi/4, np.pi/2]

wave = sum(a * np.exp(1j*(2 * np.pi * f * t + p)) for a, f, p in zip(amplitudes, frequencies, phases))

# Compute the Fourier Transform
wave_fft = np.fft.fft(wave)
frequencies = np.fft.fftfreq(len(wave), 1/fs)

# Compute magnitude and phase
magnitude = np.abs(wave_fft)
phase = np.angle(wave_fft)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, wave)
plt.title('Time-domain signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Magnitude Plot of Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, fs/2)  # Only show positive frequencies

plt.subplot(3, 1, 3)
plt.plot(frequencies, phase)
plt.title('Phase Plot of Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [radians]')
plt.xlim(0, fs/2)  # Only show positive frequencies

plt.tight_layout()
# plt.show()
plt.savefig('ft.png', dpi=300)
