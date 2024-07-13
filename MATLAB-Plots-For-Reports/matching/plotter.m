% Load S-parameter data from the file
filename = 'matching_network.txt';
data = readtable(filename, 'FileType', 'text', 'Delimiter', '\t', 'HeaderLines', 1);

% Extract frequency and S-parameters with magnitude only
frequency = data{:, 1};  % Assuming frequency is the first column

% Initialize S-parameters arrays
S11_dB = zeros(height(data), 1);
S21_dB = zeros(height(data), 1);
S12_dB = zeros(height(data), 1);
S22_dB = zeros(height(data), 1);

% Extract and convert S-parameters to dB, ignoring phase
for i = 1:height(data)
    S11_str = split(data{i, 2}, ',');
    S21_str = split(data{i, 3}, ',');
    S12_str = split(data{i, 4}, ',');
    S22_str = split(data{i, 5}, ',');
    
    S11_dB(i) = str2double(erase(S11_str{1}, 'dB'));
    S21_dB(i) = str2double(erase(S21_str{1}, 'dB'));
    S12_dB(i) = str2double(erase(S12_str{1}, 'dB'));
    S22_dB(i) = str2double(erase(S22_str{1}, 'dB'));
end

% Create subplots
figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed

subplot(2, 2, 1);
plot(frequency, S11_dB);
title('S11 (dB)');
xlabel('Frequency (Hz)');
ylabel('S11 (dB)');
grid on;

subplot(2, 2, 2);
plot(frequency, S21_dB);
title('S21 (dB)');
xlabel('Frequency (Hz)');
ylabel('S21 (dB)');
grid on;

subplot(2, 2, 3);
plot(frequency, S12_dB);
title('S12 (dB)');
xlabel('Frequency (Hz)');
ylabel('S12 (dB)');
grid on;

subplot(2, 2, 4);
plot(frequency, S22_dB);
title('S22 (dB)');
xlabel('Frequency (Hz)');
ylabel('S22 (dB)');
grid on;

% Adjust layout for better visualization
sgtitle('S-parameters in dB');
saveas(gcf, 'matching_S_params.png');


%% 

% Read the data from the file
data = importdata('Input-Impedance.txt'); % Replace 'your_data_file.txt' with your actual file name

% Extract frequency (f) and complex impedance (imp)
f = data(:, 1); % Assuming the first column is frequency
imp = complex(data(:, 2), data(:, 3)); % Assuming the second and third columns are real and imaginary parts of impedance

% Plotting
figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed
subplot(2, 1, 1);
plot(f, real(imp), '-o'); % Plot real part of impedance
xlabel('Frequency (Hz)');
ylabel('Real(imp)');
title('Frequency vs Real(imp)');

subplot(2, 1, 2);
plot(f, imag(imp), '-o'); % Plot imaginary part of impedance
xlabel('Frequency (Hz)');
ylabel('Imag(imp)');
title('Frequency vs Imag(imp)');

% Adjust plot settings if needed
grid on;
saveas(gcf, 'Input_impedance.png');