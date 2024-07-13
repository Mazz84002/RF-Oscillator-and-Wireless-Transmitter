% Assuming data is saved in S11.txt with columns: Frequency (GHz), S11 Magnitude
data = readtable('S11.txt');
frequency = table2array(data(:, 1));  % Frequency values in GHz
S11_mag = table2array(data(:, 2));    % S11 magnitude values

% Plot S11
figure();
set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the figure size as needed
plot(frequency, S11_mag, 'LineWidth', 1.5);
hold on;

xlabel('Frequency (GHz)');
ylabel('S11 Magnitude');
title('S11 Plot with Lines');
legend('S11 Magnitude', 'y = -10', 'Location', 'best');
grid on;

% Save plot as PNG
saveas(gcf, 'S11_with_lines.png');



%%
% Read data from file
data = readtable('FF.txt', 'Delimiter', ' ', 'MultipleDelimsAsOne', true);

% Extract columns
Theta_deg = table2array(data(:, 2));  % Assuming the exact column name in your data
Realized_gain_dBi = table2array(data(:, 4));  % Assuming the exact column name in your data
phi = table2array(data(:, 3));  % Assuming the exact column name in your data

%indices1 = (phi >= 0) & (phi <= 90);
%indices2 = (phi > 90) & (phi <= 270);

%Theta_deg = [Theta_deg(indices1), 360-Theta_deg(indices2)];
%Realized_gain_dBi = [Realized_gain_dBi(indices1) Realized_gain_dBi(indices2)];

% Identify the index where Theta_degree is 180
index_180 = find(Theta_deg == 180, 1); % Find the first occurrence of 180

% Check if the index is found
if isempty(index_180)
    error('Theta_degree does not contain the value 180.');
else
    % Perform 360 - value for all indices after the identified index
    Theta_deg((index_180 + 1):end) = 360 - Theta_deg((index_180 + 1):end);
end

% Plotting
figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed
plot((Theta_deg), Realized_gain_dBi, 'LineWidth', 1.5);
xlabel('Angle(deg)');
ylabel('Realised Gain(dBi)');
title('Realized Gain Plot');
xlim([0 360]);
grid on;

saveas(gcf, 'FF.png');

%% 

theta = table2array(data(:, 2));  % Assuming the exact column name in your data
phi = table2array(data(:, 3));  % Assuming the exact column name in your data
abs_grlz = table2array(data(:, 4));  % Assuming the exact column name in your data


% Convert theta to radians for polar plot
theta_rad = deg2rad(Theta_deg);

% Create polar plot
figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed
polarplot(theta_rad, abs_grlz, 'LineWidth', 1);
ax = gca;  % Get current axes handle
ax.Box = 'on';  % Display the axes box
hold on;

% Add additional elements (e.g., markers or additional plots)
% polarplot(theta_rad, abs_theta, 'b--', 'LineWidth', 2);
% polarplot(theta_rad, abs_phi, 'g:', 'LineWidth', 2);

% Add legend
%legend('farfield (f=3.5)');

% Add title and labels
title('Farfield Realized Gain Abs (Phi=90)');
ax = gca;
ax.ThetaTickLabel = {'0', '30', '60', '90', '120', '150', '180', '210', '240', '270', '300', '330'};
ax.RLim = [-30 10];  % Adjust radial limits as needed

% Display text annotations
dim = [0.05, 0.05, 0.3, 0.3];  % Adjust the left position to move the box to the left
%str = {'Frequency = 3.5 GHz', 'Main lobe magnitude = 6.22 dBi', 'Main lobe direction = 0.0 deg.', 'Angular width (3 dB) = 79.9 deg.', 'Side lobe level = -15.6 dBi'};
%annotation('textbox', dim, 'String', str, 'FitBoxToText', 'on');

% Adjust the plot for better visualization
set(gca, 'ThetaDir', 'clockwise');
set(gca, 'ThetaZeroLocation', 'top');

saveas(gcf, 'FF_p.png');