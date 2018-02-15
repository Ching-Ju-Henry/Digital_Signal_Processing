close;
clear;
clc;

%% read image
filename = 'image.jpg';
I = imread(filename);
figure('name', 'source image');
imshow(I);

%% ----- pre-lab ----- %%
% output = function(input1, input2, ...);
% grey_scale function
I2 = grey_scale(I);

%% ----- homework lab ----- %%
% flip function
I3_1 = flip(I,0);
I3_2 = flip(I,1);
I3_3 = flip(I,2);
% rotation function
I4 = rotation(I, pi/3);

%% show image
figure('name', 'grey scale image'),
imshow(I2);
figure('name', 'horizontal flipping'),
imshow(I3_1);
figure('name', 'vertical flipping'),
imshow(I3_2);
figure('name', 'horizontal + vertical flipping'),
imshow(I3_3);
figure('name', 'rotation'),
imshow(I4);
%% write image
% save image for your report
filename2 = 'grey scale image.jpg';
imwrite(I2, filename2);
filename3 = 'horizontal flipping.jpg';
imwrite(I3_1, filename3);
filename4 = 'vertical flipping.jpg';
imwrite(I3_2, filename4);
filename5 = 'horizontal + vertical flipping.jpg';
imwrite(I3_3, filename5);
filename6 = 'rotation 60.jpg';
imwrite(I4, filename6);

