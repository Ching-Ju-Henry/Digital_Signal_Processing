function imageReduced = reduceImageByMask( image, seamMask, isVertical )
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Removes pixels by input mask
% Removes vertical line if isVertical == 1, otherwise horizontal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if (isVertical)
        imageReduced = reduceImageByMaskVertical(image, seamMask);
    else
        imageReduced = reduceImageByMaskHorizontal(image, seamMask');
    end;
end

function imageReduced = reduceImageByMaskVertical(image, seamMask)
    % Note that the type of the mask is logical and you 
    % can make use of this.
    
    %%%%%%%%%%%%%%%%%%
    % YOUR CODE HERE:
    %%%%%%%%%%%%%%%%%%
    [x, y, z] = size(image);
    imageReduced = zeros(x, y-1, z);
    sz = size(seamMask);
    for i = 1:x
        %i
        %[value, idx] = min(seamMask(i,:));
        imageReduced(i, :, :) = image(i,seamMask(i,:),:);
        %imageReduced(i, idx+1:y-1, :) = ;
    end
    %%%%%%%%%%%%%%%%%%
    % END OF YOUR CODE
    %%%%%%%%%%%%%%%%%%
end

function imageReduced = reduceImageByMaskHorizontal(image, seamMask)
    %%%%%%%%%%%%%%%%%%
    % YOUR CODE HERE:
    %%%%%%%%%%%%%%%%%%
    [x, y, z] = size(image);
    imageReduced = zeros(x-1, y, z);
    sz = size(seamMask);
    for i = 1:y
        %[value, idx] = min(seamMask(:,i));
        %imageReduced(1:1:idx-1, i, :) = image(1:1:idx-1, i, :);
        %imageReduced(idx+1:1:x-1, i, :) = image(idx+1:1:x-1, i, :);
        imageReduced(:, i, :) = image(seamMask(:,i),i,:);
    end
    %%%%%%%%%%%%%%%%%%
    % END OF YOUR CODE
    %%%%%%%%%%%%%%%%%%
end
