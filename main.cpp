#include "Gaussianui.h"
#include <QtWidgets/QApplication>
#include <iostream>
#include <QDebug>
#include <vector>
#include <cmath>
#include <fstream>
#include <QImageReader.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;



#include <opencv2/highgui.hpp>


int maintest()
{
	Mat output;
	int uX=400/2;
	int uY=400/2;
	float sigmaX=1.0;
	float sigmaY=1.0;
	int amplitude = 1;
	Mat temp(400,400, CV_32F);
	for (int r = 0; r < 400; r++)
	{
		for (int c = 0; c < 400; c++)
		{
			float x = ((c - uX) * ((float)c -uX)) /(2.0f * sigmaX *sigmaY);
			float y = ((c - uY) * ((float)c - uY)) / (2.0f * sigmaX *sigmaY);
			float value = amplitude * exp(-(x + y));
			temp.at<float>(r, c) = value;
		}
	}
	normalize(temp, temp, 0.0f,1.0f, NORM_MINMAX);
	output = temp;
	imshow("Gaussian.png", temp);
	return 0;
}

void LinearSpacedArray(float a, float b, float num)
{

	const int sizeX = 400;
	const int sizeY = 400;
	float pMap[sizeX][sizeY] = { 0 };
	float sigmaX = 0.5;
	const float x0 = 200;
	const float y0 = 200;
	int center_x = sizeY / 2;
	int center_y  = sizeX / 2;
	for (int yMap = 0; yMap < sizeY; yMap++)
	{
		for (int xMap = 0; xMap < sizeX; xMap++)
		{
			float distx = abs(xMap - center_x);
			float disty = abs(yMap - center_y);
			float dist = sqrt(distx * distx + disty * disty);
			float dis  =dist- sigmaX;
			float dista = dis * 2;
			pMap[yMap][xMap] = dista;
		}
	}
	for (int i = 0; i < sizeX; i++)
	{
		for (int j = 0; j < sizeY; j++)
		{
			if (pMap[i][j] > 0) 
			{
				pMap[i][j] *= 255;
			}
		}
	}
	for (int i = 0; i < sizeX; i++)
	{
		for (int j = 0; j < sizeY; j++)
		{
			pMap[i][j] /= 255;
			
		}
	}
	Mat grayImage(400, 400, CV_32F, pMap);
	Mat image;
	imwrite("Gray_Image_new.png", grayImage);
	
	system("pause");
}
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Gaussianui w;
	maintest();
	LinearSpacedArray(10, 20, 30);
	maintest();
	w.show();
	return a.exec();
}
