% My Harris detector
% The code calculates
% the Harris Feature/Interest Points (FP or IP) 
% 
% When u execute the code, the test image file opened
% and u have to select by the mouse the region where u
% want to find the Harris points, 
% then the code will print out and display the feature
% points in the selected region.
% You can select the number of FPs by changing the variables 
% max_N & min_N


%%%
%corner : significant change in all direction for a sliding window
%%%


%%
% parameters
% corner response related
sigma=2;
n_x_sigma = 6;
alpha = 0.04;
% maximum suppression related
Thrshold=20;  % should be between 0 and 1000
r=6; 


%%
% filter kernels
dx = [-1 0 1; -1 0 1; -1 0 1]; % horizontal gradient filter 
dy = dx'; % vertical gradient filter
g = fspecial('gaussian',max(1,fix(2*n_x_sigma*sigma)), sigma); % Gaussien Filter: filter size 2*n_x_sigma*sigma


%% load 'Im.jpg'
frame = imread('data/Im2.jpg');
I = double(frame);
figure(1);
imagesc(frame);
[xmax, ymax, ch] = size(I);
xmin = 1;
ymin = 1;


%%%%%%%%%%%%%%Intrest Points %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%
% get image gradient
% [Your Code here] 
% calculate Ix
% calcualte Iy
I = I(:,:,1);
Ix = conv2( I,dx, 'same');
Iy = conv2( I,dy, 'same');
%%%%%
% get all components of second moment matrix M = [[Ix2 Ixy];[Iyx Iy2]]; note Ix2 Ixy Iy2 are all Gaussian smoothed
% [Your Code here] 
% calculate Ix2  
% calculate Iy2
% calculate Ixy
Ix2 = conv2((Ix.^2),g,  'same');
Iy2 = conv2((Iy.^2),g,  'same');
Ixy = conv2((Ix.*Iy),g,  'same');
M = [[Ix2 Ixy];[Ixy Iy2]];
%%%%%

%% visualize Ixy
figure(2);
imagesc(Ixy);

%%%%%%% Demo Check Point -------------------


%%%%%
% get corner response function R = det(M)-alpha*trace(M)^2 
% [Your Code here] 
% calculate R
for x=1:xmax,
   for y=1:ymax,
       H = [Ix2(x, y) Ixy(x, y); Ixy(x, y) Iy2(x, y)];
       R(x,y) = det(H) - alpha * (trace(H) ^ 2);
   end
end
%R = ((Ix2.*Iy2) - (Ixy.^2));
%%%%%

%% make max R value to be 1000
R=(1000/max(max(R)))*R; % be aware of if max(R) is 0 or not

%%%%%
%% using B = ordfilt2(A,order,domain) to complment a maxfilter
sze = 2*r+1; % domain width 
% [Your Code here] 
% calculate MX
MX = ordfilt2(R, sze.^2, ones(sze));
%%%%%

%%%%%
% find local maximum.
% [Your Code here] 
% calculate RBinary
RBinary = (R == MX) & (R > Thrshold);
%%%%%


%% get location of corner points not along image's edges
offe = r-1;
count=sum(sum(RBinary(offe:size(RBinary,1)-offe,offe:size(RBinary,2)-offe))); % How many interest points, avoid the image's edge   
R=R*0;
R(offe:size(RBinary,1)-offe,offe:size(RBinary,2)-offe)=RBinary(offe:size(RBinary,1)-offe,offe:size(RBinary,2)-offe);
[r1,c1] = find(R);


%% Display
I = double(frame);
figure(3)
imagesc(uint8(I));
hold on;
plot(c1,r1,'or');
return;
