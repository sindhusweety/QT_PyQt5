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
			//float distx = x0 + xMap * (y0 - x0) / (floor((float)sizeX) - 1);
			//float disty = x0 + yMap * (y0 - x0) / (floor((float)sizeY) - 1);
			//float dist = distx - sigmaX;
			//float dist_ = dist * 2.0f;
			//float dis = -dist_;
			//pMap[yMap][xMap] = dis;
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
			qDebug() << pMap[i][j];
		}
	}
	int temp = 0;
	FILE* pgmn;
	pgmn = fopen("new.pgm", "wb");
	fprintf(pgmn, "P2\n");
	fprintf(pgmn, "%d %d \n", 400, 400);
	fprintf(pgmn, "255\n");
	for (int i = 0; i < sizeX; i++)
	{
		for (int j = 0; j < sizeY; j++)
		{
			temp = pMap[i][j];
			fprintf(pgmn, "%d", temp);
		}
		fprintf(pgmn, "\n");
	}

	
	system("pause");
}
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Gaussianui w;
	LinearSpacedArray(10, 20, 30);
	w.show();
	return a.exec();
}
