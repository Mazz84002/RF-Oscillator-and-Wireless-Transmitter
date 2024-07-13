% Load the data from VCO_trans.matlab
VCO_trans = readmatrix('VCO_trans.matlab', 'FileType', 'text');

% Extract x and y values
x = VCO_trans(:, 1); % First column
y = VCO_trans(:, 2); % Second column

figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed
% Plot the data
plot(x, y); % '-o' connects points with lines and marks data points with circles

% Add labels and title
xlabel('t[sec]');
ylabel('V_{out}');
title('Transient Analysis of Oscillator + Matching Network');

% Add grid
grid on;
saveas(gcf, 'VCO_trans.png');


%% ------------------------


% Filter data 
indices = (x >= 13e-9) & (x <= 14e-9);
x = x(indices);
y = y(indices);

figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust the numbers as needed
% Plot the data
plot(x, y); % '-o' connects points with lines and marks data points with circles

% Add labels and title
xlabel('t[sec]');
ylabel('V_{out}');
title('Transient Analysis of Oscillator + Matching Network(Zoomed)');

% Add grid
grid on;
saveas(gcf, 'VCO_trans_zoom.png');


%% --------------------------

% Load the data from VCO_trans.matlab
VCO_spec = readmatrix('VCO_spec.matlab', 'FileType', 'text');
VCO_spec_low = readmatrix('VCO_spec_low.matlab', 'FileType', 'text');
VCO_spec_high = readmatrix('VCO_spec_high.matlab', 'FileType', 'text');

% Extract x and y values
x = VCO_spec(:, 1); % First column
y = VCO_spec(:, 2); % Second column
x_low = VCO_spec_low(:, 1); % First column
y_low = VCO_spec_low(:, 2); % Second column
x_high = VCO_spec_high(:, 1); % First column
y_high = VCO_spec_high(:, 2); % Second column

% Filter data where spectrum__net0_X is between [3.3e9, 3.7e9]
indices = (x >= 3e9) & (x <= 4e9);

x = x(indices);
y = y(indices);
x_low = x_low(indices);
y_low = y_low(indices);
x_high = x_high(indices);
y_high = y_high(indices);

% Smooth the data using interpolation
x_interp = linspace(min(x), max(x), 100); % Interpolation points

y_smooth = interp1(x, y, x_interp, 'spline');
y_low_smooth = interp1(x_low, y_low, x_interp, 'spline');
y_high_smooth = interp1(x_high, y_high, x_interp, 'spline');

figure; set(gcf, 'Position', [100, 100, 1200, 800]); % Adjust figure size as needed

% Plot the data with smoothed curves
% Define x_interp and y_smooth, y_low_smooth, y_high_smooth as your data

y_lim = -35;

% Plot the Ideal stems starting from -100
h1 = stem(x_interp, y_smooth, 'DisplayName', 'Ideal'); % Ideal plot with circles marking data points
set(h1, 'BaseValue', y_lim); % Set the base value to -100
hold on;

% Plot the Max low deviation stems starting from -100
h2 = stem(x_interp, y_low_smooth, 'DisplayName', 'Max low deviation'); % Smoothed low deviation plot
set(h2, 'BaseValue', y_lim); % Set the base value to -100

% Plot the Max high deviation stems starting from -100
h3 = stem(x_interp, y_high_smooth, 'DisplayName', 'Max high deviation'); % Smoothed high deviation plot
set(h3, 'BaseValue', y_lim); % Set the base value to -100

%hold off;
%legend;
% Find peaks for each curve
[~, locs_y] = findpeaks(y_smooth);
[~, locs_y_low] = findpeaks(y_low_smooth);
[~, locs_y_high] = findpeaks(y_high_smooth);

% Mark peaks on the plot with data tips
hold on;
dcm_obj = datacursormode(gcf);
set(dcm_obj, 'UpdateFcn', @dataTipCallback);

% Add labels and title
xlabel('f [Hz]');
ylabel('V_{out} [dB]'); ylim([y_lim, 5]);
title('Harmonic Balance of Oscillator + Matching Network');

legend('show', 'Location', 'best', 'Interpreter', 'none');

% Add grid
grid on;

% Save the plot as a .png file
saveas(gcf, 'VCO_spec_smoothed_with_peak_values.png');

function txt = dataTipCallback(~, event)
    pos = get(event, 'Position');
    txt = {sprintf('x: %.2e Hz', pos(1)), ...
           sprintf('y: %.2f dB', pos(2))};
end

