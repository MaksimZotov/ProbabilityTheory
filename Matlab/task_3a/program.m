% 1.1
N = 12200;
parts = 10;
diagramSteps = 40;
n = N / parts;

X = dlmread('Task_3a.txt');

Xperm = X(randperm(length(X)));
Xpodv = zeros(parts, n);

for i = 1 : parts
    Xpodvt = Xperm(1 + (i - 1) * N / 10 : i * N / 10);
    for j = 1 : n
        Xpodv(i, j) = Xpodvt(j);
    end
end

% 1.2.1
figure; cdfplot(X);

% 1.2.2
maximum = max(X);
minimum = min(X);

step = (maximum - minimum) / diagramSteps;
intervals = minimum : step : maximum;

figure; histogram(X, intervals);
figure; histogram(X, intervals, 'Normalization', 'probability');

% 1.2.3
xMean = mean(X);
xD = mean((X - xMean).^2);
x_sqrt_D = sqrt(xD);

Xsort = sort(X);

P_KDE_gauss = zeros(1, N);
h_gauss = 1.06 * sqrt(xD) * N^(-0.2);

P_KDE_exp = zeros(1, N);
h_exp = h_gauss;

P_KDE_cauchy = zeros(1, N);
h_cauchy = h_gauss;

for i = 1 : N
    sigma_gauss = 0;
    sigma_exp = 0;
    sigma_cauchy = 0;
    for j = 1 : N
        arg_gauss = (Xsort(i) - Xsort(j)) / h_gauss;
        gauss_distribution_arg = exp(- arg_gauss^2 / 2) / sqrt(2 * pi);
        sigma_gauss = sigma_gauss + gauss_distribution_arg;
        
        arg_exp = (Xsort(i) - Xsort(j)) / h_exp;
        exp_distribution_arg = exp(-abs(arg_exp)) / 2;
        sigma_exp = sigma_exp + exp_distribution_arg;
        
        arg_cauchy = (Xsort(i) - Xsort(j)) / h_cauchy;
        cauchy_distribution_arg = 1 / (pi * (1 + arg_cauchy^2));
        sigma_cauchy = sigma_cauchy + cauchy_distribution_arg;
    end
    P_KDE_gauss(i) = sigma_gauss / (N * h_gauss);
    P_KDE_exp(i) = sigma_exp / (N * h_exp);
    P_KDE_cauchy(i) = sigma_cauchy / (N * h_cauchy);
end
figure; plot(Xsort, P_KDE_gauss);
figure; plot(Xsort, P_KDE_exp);
figure; plot(Xsort, P_KDE_cauchy);

% 1.3.1
xMedian = median(Xsort(N / 2));
xMid = (maximum - minimum) / 2;

moment_center_3 = mean((X - xMean).^3);
moment_center_4 = mean((X - xMean).^4);

xMod = 0;
for i = 2 : N
    if P_KDE_gauss(i) < P_KDE_gauss(i - 1)
        xMod = Xsort(i);
        break;
    end
end

% 1.3.2
xSkewness = skewness(X);
xKurtosis = kurtosis(X);

% 1.3.3
P = 0.95;
left_quantile_0_95 = quantile(X, (1 - P) / 2);
right_quantile_0_95 = quantile(X, (1 + P) / 2);

% 1.3.4
Xmean = zeros(1, parts);
Xmedian = zeros(1, parts);
Xmid = zeros(1, parts);
Xd = zeros(1, parts);
X_sqrt_d = zeros(1, parts);
X_moment_center_3 = zeros(1, parts);
X_moment_center_4 = zeros(1, parts);
Xskewness = zeros(1, parts);
Xkurtosis = zeros(1, parts);

for i = 1 : parts
   for j = 1 : n
       Xpodvt(j) = Xpodv(i, j);
   end
   Xmean(i) = mean(Xpodvt);
   Xmedian(i) = median(Xpodvt);
   Xmid(i) = (max(Xpodvt) - min(Xpodvt)) / 2;
   Xd(i) = mean((Xpodvt - Xmean(i)).^2);
   X_sqrt_d(i) = sqrt(Xd(i));
   X_moment_center_3(i) = mean((Xpodvt - Xmean(i)).^3);
   X_moment_center_4(i) = mean((Xpodvt - Xmean(i)).^4);
   Xskewness(i) = skewness(Xpodvt);
   Xkurtosis(i) = kurtosis(Xpodvt);
end

% 1.4
Q = 0.8;

tin = tinv((1 + Q) / 2, N - 1);
xMean_left_Q_0_8 = xMean - (sqrt(xD / N)) * tin;
xMean_right_Q_0_8 = xMean + (sqrt(xD / N)) * tin;

xD_left_Q_0_8  = xD * (N - 1) / chi2inv((1 + Q) / 2 , N - 1);
xD_right_Q_0_8 = xD * (N - 1) / chi2inv((1 - Q) / 2 , N - 1);

Xmean_interval_Q_0_8 = zeros(10, 2);
Xd_interval_Q_0_8 = zeros(10, 2);
left_denominator = chi2inv((1 + Q) / 2 , n - 1);
right_denominator = chi2inv((1 - Q) / 2 , n - 1);
for i = 1 : parts
   Xmean_interval_Q_0_8(i, 1) = Xmean(i) - (sqrt(Xd(i) / n)) * tin;
   Xmean_interval_Q_0_8(i, 2) = Xmean(i) + (sqrt(Xd(i) / n)) * tin;
   Xd_interval_Q_0_8(i, 1) = Xd(i) * (n - 1) / left_denominator;
   Xd_interval_Q_0_8(i, 2) = Xd(i) * (n - 1) / right_denominator;
end


k = 590;
left = Xsort(k / 2);
right = Xsort(N - k / 2);

k_n_P_Q = 1.96;
borders = zeros(parts, 2);
for i = 1 : parts
    borders(i, 1) = Xmean(i) - k_n_P_Q * X_sqrt_d(i);
    borders(i, 2) = Xmean(i) + k_n_P_Q * X_sqrt_d(i);
end

% 2.2
k_mm = (xMean / x_sqrt_D)^2;
O_mm = xD / xMean;
mle_gamma = mle(Xsort, 'pdf', @gampdf, 'start', [1 1]);
k_mle = mle_gamma(1);
O_mle = mle_gamma(2);
figure;
ksdensity(Xsort);
grid on; hold on;
Y_mle = gampdf(Xsort, k_mle, O_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = gampdf(Xsort, k_mm, O_mm);
plot(Xsort, Y_mm, 'r');
legend({'Gamma - KDE', 'Gamma - MLE', 'Gamma - MM'});

figure;
cdfplot(Xsort);
grid on; hold on;
Y_mle = gamcdf(Xsort, k_mle, O_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = gamcdf(Xsort, k_mm, O_mm);
plot(Xsort, Y_mm, 'r');
legend({'Gamma - KDE', 'Gamma - MLE', 'Gamma - MM'});


M_mm = xMean;
sqrt_D_mm = x_sqrt_D;
mle_mormal = mle(Xsort, 'pdf', @normpdf, 'start', [1 1]);
M_mle = mle_mormal(1);
sqrt_D_mle = mle_mormal(2);
figure;
ksdensity(Xsort);
grid on; hold on;
Y_mle = normpdf(Xsort, M_mle, sqrt_D_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = normpdf(Xsort, M_mm, sqrt_D_mm);
plot(Xsort, Y_mm, 'r');
legend({'Normal - KDE', 'Normal - MLE', 'Normal - MM'});

figure;
cdfplot(Xsort);
grid on; hold on;
Y_mle = normcdf(Xsort, M_mle, sqrt_D_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = normcdf(Xsort, M_mm, sqrt_D_mm);
plot(Xsort, Y_mm, 'r');
legend({'Normal - KDE', 'Normal - MLE', 'Normal - MM'});


laplace_pdf = @(X, c, a)(a / 2 * exp(-a * abs(X - c)) * (a > 0) + 1e-10);
M_mm = xMean;
lambda_mm = sqrt(2 / xD);
mle_laplace = mle(Xsort, 'pdf', laplace_pdf, 'start', [1 1]);
M_mle = mle_laplace(1);
lambda_mle = mle_laplace(2);
figure;
ksdensity(Xsort);
grid on; hold on;
Y_mle = laplace_pdf(Xsort, M_mle, lambda_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = laplace_pdf(Xsort, M_mm, lambda_mm);
plot(Xsort, Y_mm, 'r');
legend({'Laplace - KDE', 'Laplace - MLE', 'Laplace - MM'});

laplace_cdf = @(X, c, a)((0.5 * exp(a * (X - c))).*(X <= c) + (1 - 0.5 * exp(-a * (X - c))).*(X > c));
figure;
cdfplot(Xsort);
grid on; hold on;
Y_mle = laplace_cdf(Xsort, M_mle, lambda_mle);
plot(Xsort, Y_mle, 'g');
Y_mm = laplace_cdf(Xsort, M_mm, lambda_mm);
plot(Xsort, Y_mm, 'r');
legend({'Laplace - KDE', 'Laplace - MLE', 'Laplace - MM'});


% 2.3
Y_hist = zeros(1, length(intervals) - 1);
interval_left = 1;
for i = 1 : N
    if (Xsort(i) >= intervals(interval_left)) && (Xsort(i) < intervals(interval_left + 1))
        Y_hist(interval_left) = Y_hist(interval_left) + 1;
    else
        Y_hist(interval_left) = Y_hist(interval_left);
        interval_left = interval_left + 1;
    end
end

xi_criteria = chi2inv((1 + Q) / 2, length(intervals) - 2);
xi_gamma_mm = 0;
xi_gamma_mle = 0;
xi_normal_mm = 0;
xi_normal_mle = 0;
xi_laplace_mm = 0;
xi_laplace_mle = 0;
for i = 2 : length(intervals)
    pk = gamcdf(intervals(i), k_mm, O_mm) - gamcdf(intervals(i - 1), k_mm, O_mm);
    xi_gamma_mm = xi_gamma_mm + (N * pk - Y_hist(i - 1))^2 / pk;
    pk = gamcdf(intervals(i), k_mle, O_mle) - gamcdf(intervals(i - 1), k_mle, O_mle);
    xi_gamma_mle = xi_gamma_mle + (N * pk - Y_hist(i - 1))^2 / pk;
    
    pk = normcdf(intervals(i), M_mm, sqrt_D_mm) - normcdf(intervals(i - 1), M_mm, sqrt_D_mm);
    xi_normal_mm = xi_normal_mm + (N * pk - Y_hist(i - 1))^2 / pk;
    pk = normcdf(intervals(i), M_mle, sqrt_D_mle) - normcdf(intervals(i - 1), M_mle, sqrt_D_mle);
    xi_normal_mle = xi_normal_mle + (N * pk - Y_hist(i - 1))^2 / pk;
    
    pk = laplace_cdf(intervals(i), M_mm, lambda_mm) - laplace_cdf(intervals(i - 1), M_mm, lambda_mm);
    xi_laplace_mm = xi_laplace_mm + (N * pk - Y_hist(i - 1))^2 / pk;
    pk = laplace_cdf(intervals(i), M_mle, lambda_mle) - laplace_cdf(intervals(i - 1), M_mle, lambda_mle);
    xi_laplace_mle = xi_laplace_mle + (N * pk - Y_hist(i - 1))^2 / pk;
end
xi_gamma_mm = xi_gamma_mm / N;
xi_gamma_mle = xi_gamma_mle / N;
xi_normal_mm = xi_normal_mm / N;
xi_normal_mle = xi_normal_mle / N;
xi_laplace_mm = xi_laplace_mm / N;
xi_laplace_mle = xi_laplace_mle / N;

alpha = 1 - Q;
kolmogorov_smirnov_criteria = sqrt(- 1 * log(0.5 * alpha) / (2 * N)) - 1 / (6 * N);
D_gamma_mm = 0;
D_gamma_mle = 0;
D_normal_mm = 0;
D_normal_mle = 0;
D_laplace_mm = 0;
D_laplace_mle = 0;
for i = 1 : N
   D_mm = abs(gamcdf(Xsort(i), k_mm, O_mm) - i / N);
   if D_mm > D_gamma_mm
       D_gamma_mm = D_mm;
   end
   D_mle = abs(gamcdf(Xsort(i), k_mle, O_mle) - i / N);
   if D_mle > D_gamma_mle
       D_gamma_mle = D_mle;
   end
   
   D_mm = abs(normcdf(Xsort(i), M_mm, lambda_mm) - i / N);
   if D_mm > D_normal_mm
       D_normal_mm = D_mm;
   end
   D_mle = abs(normcdf(Xsort(i), M_mle, lambda_mle) - i / N);
   if D_mle > D_normal_mle
       D_normal_mle = D_mle;
   end
   
   D_mm = abs(laplace_cdf(Xsort(i), M_mm, lambda_mm) - i / N);
   if D_mm > D_laplace_mm
       D_laplace_mm = D_mm;
   end
   D_mle = abs(laplace_cdf(Xsort(i), M_mle, lambda_mle) - i / N);
   if D_mle > D_laplace_mle
       D_laplace_mle = D_mle;
   end
end

mises_criteria = 0.2415;
start_value = 1 / (12 * N);
nw_gamma_mm = start_value;
nw_gamma_mle = start_value;
nw_normal_mm = start_value;
nw_normal_mle = start_value;
nw_laplace_mm = start_value;
nw_laplace_mle = start_value;
for i = 1 : N
   sub = (2 * i - 1) / (2 * N);
   nw_gamma_mm = nw_gamma_mm + (gamcdf(Xsort(i), k_mm, O_mm) - sub)^2;
   nw_gamma_mle = nw_gamma_mle + (gamcdf(Xsort(i), k_mle, O_mle) - sub)^2;
   
   nw_normal_mm = nw_normal_mm + (normcdf(Xsort(i), M_mm, lambda_mm) - sub)^2;
   nw_normal_mle = nw_normal_mle + (normcdf(Xsort(i), M_mle, lambda_mle) - sub)^2;
   
   nw_laplace_mm = nw_laplace_mm + (laplace_cdf(Xsort(i), M_mm, lambda_mm) - sub)^2;
   nw_laplace_mle = nw_laplace_mle + (laplace_cdf(Xsort(i), M_mle, lambda_mle) - sub)^2;
end