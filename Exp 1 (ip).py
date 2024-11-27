#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt
# Parameters
A = 1 # Amplitude
f = 10 # Frequency of the continuous signal (Hz)
fs1 = 60 # Sampling frequency below Nyquist rate (Hz)
fs2 = 20 # Sampling frequency at Nyquist rate (Hz)
fs3 = 12 # Sampling frequency above Nyquist rate (Hz)
t = np.linspace(0, 1, 1000) # Continuous time vector
# Continuous-time signal
x_t = A * np.sin (2 * np.pi * f * t)
# Sampling intervals
n1 = np.arange(0, 1, 1/fs1)
n2 = np.arange(0, 1, 1/fs2)
n3 = np.arange(0, 1, 1/fs3)
# Discrete-time signals
x_n1 = A * np.sin(2 * np.pi * f * n1)
x_n2 = A * np.sin(2 * np.pi * f * n2)
x_n3 = A * np.sin(2 * np.pi * f * n3)
# Plotting
plt.figure (figsize=(15, 8))
# Continuous-time signal

plt.subplot(3, 1, 1)
plt.plot(t, x_t, label='Continuous-time signal')
plt.stem(n1, x_n1, 'r', markerfmt='ro', basefmt=" ", label='Sampled signal (fs = 8 Hz)')
plt.title('Sampling below Nyquist rate (Aliasing)')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, x_t, label= 'Continuous-time signal')
plt.stem(n2, x_n2, 'g', markerfmt='go', basefmt=" ", label='Sampled signal (fs = 10 Hz)')
plt.title("Sampling at Nyquist rate")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, x_t, label='Continuous-time signal')
plt.stem(n3, x_n3, 'b', markerfmt='bo', basefmt=" ", label='Sampled signal (fs = 20 Hz)')
plt.title('Sampling above Nyquist rate')
plt.legend()

plt.tight_layout()
plt.show()


# In[ ]:




