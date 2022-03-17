clear;

% ciary=8;
ciary=10;
maxima=[];
body=[];
% img=imread('ach.bmp');
img=imread('ach1.bmp');
img=rgb2gray(img);
figure(1);
imshow(img);
figure(2);
imshow(img);
hold on;

%velkost obrazka
[vyska,sirka]=size(img);

%theta je v rozsahu 1-180
for a=1:1:180
theta(a)=a;
end

%diagonalu vypocitame pomocou pytagorovej vety
diagonala=round(sqrt((sirka*sirka)+(vyska*vyska)));

matica=zeros(diagonala+diagonala,size(theta,2));
pozicia=1;
%hladanie nenulových bodov obrazka
for a=1:vyska
    for b=1:sirka
    if img(a,b)>0
    indexx(pozicia)=b;
    indexy(pozicia)=a;
    pozicia=pozicia+1;
    end
    end
end

for w=1:size(indexx,2)
    for q=1:size(theta,2)
    ro=(indexx(w)*cosd(theta(q))+indexy(w)*sind(theta(q)));
    ro=round(ro,1);
    ro=ro+diagonala;
    ro=round(ro);
    matica(ro,q)=matica(ro,q)+1;
    end
end

hladaniemaxim=matica;

for w=1:ciary 
   [maxi] = max(hladaniemaxim(:));
   [riadok stlpec] = find(hladaniemaxim == maxi);
   maxima=[maxima;riadok stlpec];
   hladaniemaxim(riadok,stlpec)=0;
end

for w=1:size(maxima,1)
    r=maxima(w,1);
    r=r-diagonala;
    theta1=maxima(w,2);
    for x=1:sirka
        for y=1:vyska
            rho=(x*cosd(theta1))+(y*sind(theta1));
                if abs(rho-r)<1
                    body=[body;x,y];
                end
        end
        
    end
   if(isempty(body)==0)
        a=size(body);
        bod1=[body(1,1),body(a(1),1)];
        bod2=[body(1,2),body(a(1),2)];
        body=[];
        figure(2)
        line(bod1,bod2,'Color','red');
        figure(3)
        line(bod1,bod2,'Color','red');
    end 
    set(gca,'YDir','reverse');

end

grafx=[];
grafy=[];
figure(4)
for w=1:size(indexx,2)
    for q=-90:10:90
        ro=+(indexx(w)*cosd(q))+(indexy(w)*sind(q));
        grafx=[grafx q];
        grafy=[grafy ro];
    end
    h=plot(grafx,grafy);
    set(h,'Color','white');
    set(gca,'Color','black');
    hold on;
    grafx=[];
    grafy=[];
end
set(gca,'YDir','reverse');

[Hough,q,ro] = hough(img);
figure(5);
imshow(imadjust(rescale(Hough)),[],...
    'XData',q,...
    'YData',ro,...
    'InitialMagnification','fit');
axis on;
axis normal;
hold on
colormap(gca,hot)
    
