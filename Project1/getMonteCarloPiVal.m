%% Section 3: Function to provide pi value of specified precision
%

function monteCarloValue = getMonteCarloPiVal(desiredSigFigs)
    % Create parameter arrays for a circle to draw on graph
    theta = linspace(0, 2*pi(), 256);
    circleX = cos(theta)+1;
    circleY = sin(theta)+1;

    % Initialize point arrays for Monte Carlo calculations
    generatedPoints=[rand(2,1)];
    pointsInCircle = [[1;1]];
    pointsOutsideCircle = [[0;0]];
    piVal = 0;
    
    % Create plots and set axes/datasets
    figure;

    circlePlot = plot(pointsInCircle(1,:), pointsInCircle(2,:), 'xb', pointsOutsideCircle(1,:), pointsOutsideCircle(2,:), 'xr', circleX, circleY, '-k');
    
    xlim([0,2]);
    ylim([0,2]);
    axis square;

    % While the provided pi value does not possess the desired number of
    % sig figs:
    %   - generate a new point and add it to the array of random points,
    %   - re-calculate a pi value based on the updated array,
    %   - check if sig figs are met or if maximum attempts have been
    %   expended
    %   - update the plot of generated values
    while ~meetsSigFigs(desiredSigFigs, piVal)
        generatedPoints = cat(2, generatedPoints, 2*rand(2,1));
        [piVal, pointsInCircle, pointsOutsideCircle]  = getPiValFromCoords(generatedPoints, pointsInCircle, pointsOutsideCircle);
        if meetsSigFigs(desiredSigFigs, piVal)
            break;
        elseif numel(generatedPoints(1,:)) > 10^8
            disp('maximum tries expended')
            break;
        end
        
        delete(findall(gcf, 'type', 'annotation'));
        set(circlePlot(1), 'XData', pointsInCircle(1,:), 'YData', pointsInCircle(2,:));
        set(circlePlot(2), 'XData', pointsOutsideCircle(1,:), 'YData', pointsOutsideCircle(2,:));
        set(circlePlot(3), 'XData', circleX, 'YData', circleY);
        annotation('textbox', [0,0,.3,.3], 'String', string(piVal), 'FitBoxToText', 'on');
        drawnow;
    end
    
    % Perform final update of chart and write output in console, assign
    % generated value to return variable 
    delete(findall(gcf, 'type', 'annotation'));
    annotation('textbox', [0,0,.3,.3], 'String', string(piVal), 'FitBoxToText', 'on');
    drawnow;
    fprintf('Pi value with %d significant figure(s): %f \n', desiredSigFigs, piVal);
    fprintf('Number of points required for %d significant figure(s): %d \n', desiredSigFigs, numel(generatedPoints(1,:)));
    monteCarloValue = piVal;
end

%% Helper functions
% 

% Function to check whether the provided pi value matches pi up to the
% desired quantity of significant figures - WILL LIKELY BE REPLACED
function hasFigs = meetsSigFigs(sigfigs, value)
    expVal = value * 10^sigfigs;
    actualVal = pi() * 10^sigfigs;
    if abs(expVal-actualVal) < 1
        hasFigs = true;
    else
        hasFigs = false;
    end
end

% Function that accepts an array of randomly generated coordinates
% and provides a pi value based on the number that fall within
% a circle, as well as two arrays of points inside and outside the circle
function [valueToReturn, withinCircle, outsideCircle] = getPiValFromCoords(coordArray, currentInsideCircle, currentOutsideCircle)
    intCount = 0.0;
    for coord = 1:numel(coordArray(1,:))
        if distanceToCenter([coordArray(1,coord),coordArray(2,coord)]) <= 1
            intCount = intCount + 1;
            withinCircle = cat(2, currentInsideCircle, [coordArray(1,coord);coordArray(2,coord)]);
            outsideCircle = currentOutsideCircle;
        else
            outsideCircle = cat(2, currentOutsideCircle, [coordArray(1,coord);coordArray(2,coord)]);
            withinCircle = currentInsideCircle;
        end
    end
    proportion = intCount/numel(coordArray(1,:));
    valueToReturn = proportion*4;
end


% calculates distance between point argument (treated as [x;x]) 
% and center of square, taken to be [0.5;0.5]
function dist = distanceToCenter(point)
    dist = sqrt((1-point(1))^2 + (1-point(2))^2);
end