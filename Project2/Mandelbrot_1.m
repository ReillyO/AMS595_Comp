%% Project 2: Mandelbrot Fractal

N = 1000;
mandelbrotPoints = zeros(N, N);
displayGrid = zeros(N,N);

x = linspace(-2, 1, N);
y = linspace(-1, 1, N);
[X, Y] = meshgrid(x, y);

mandelbrotPoints = X + Y * 1i;

% figure will display white pixels if coordinate converges and black/grey pixels
% if the coordinate diverges
for valX = 1:N
    for valY = 1:N
       iters = fractalIterationsToDivergence(mandelbrotPoints(valY, valX));
       if iters == -1
           displayGrid(valY, valX) = 200;
       else
           displayGrid(valY, valX) = iters;
       end
    end
end

% figure;
% imshow(displayGrid, [0 200], "InitialMagnification", 400);

% s = bisection(indicatorFunctionForCol(-1.1), 0, 1);
% disp(s);

boundCoords = [numel(x)];
for column = 1:numel(x)
    boundCoords(column) = bisection(indicatorFunctionForCol(x(column)), 0, 1);
end
figure;
scatter(x, boundCoords, 'or');

%% fractal function
% will return -1 if c converges and the number of iterations if it
% diverges
function iterations = fractalIterationsToDivergence(c)
    CUTOFF_ITER = 100;
    FRACTAL_BOUND = 2;
    iterations = 0;
    z = c;
    while iterations < CUTOFF_ITER && abs(z)^2 < FRACTAL_BOUND
        z = z^2 + c;
        iterations = iterations + 1;
    end
    if iterations == CUTOFF_ITER
        iterations = -1;
    end
end

% Function to define the indicator function for a particular column
% provided as the input parameter
% Anonymous function returns -1 if divergent and 1 if convergent
function fn = indicatorFunctionForCol(xval)
    fn = @(yval) (fractalIterationsToDivergence(xval + 1i * yval) >= 0) * 2 - 1;
end

% Function that uses a binary search algorithm structure to find the point
% at which complex values switch from being outside to inside the
% Mandelbrot set on a particular X-value
function m = bisection(fn_f, s, e)
    m = e;
    m0 = s;
    mt = 0;
    while fn_f(m) == fn_f(m+1/1000) %not at boundary, 1/N
        fprintf('function return: %f\n', fractalIterationsToDivergence(1 + 1i * m));
        fprintf('m: %f\nfn_f(m): %f \nm0: %f\n', m, fn_f(m), m0)
        mt = m;
        if fn_f(m) < 0 % diverges
            m = m + 0.5*(abs(m0 - m));
        elseif m < 1/1000
            m = 0;
            break;
        else % converges
            m = m - 0.5*(abs(m - m0));
        end
        m0 = mt;
    end
    fprintf('\n=====\nEND\n=====\nfn_f(m): %f\nfn_f(m+1/1000): %f\nm: %f\n', fn_f(m), fn_f(m+1/1000), m);
end