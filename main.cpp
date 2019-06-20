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

void PerlinNoise2D(int nWidth, int nHeight, float *fSeed, int nOctaves, float fBias, float *fOutput)
{
	// Used 1D Perlin Noise
	for (int x = 0; x < nWidth; x++)
		for (int y = 0; y < nHeight; y++)
		{
			float fNoise = 0.0f;
			float fScaleAcc = 0.0f;
			float fScale = 1.0f;

			for (int o = 0; o < nOctaves; o++)
			{
				int nPitch = nWidth >> o;
				int nSampleX1 = (x / nPitch) * nPitch;
				int nSampleY1 = (y / nPitch) * nPitch;

				int nSampleX2 = (nSampleX1 + nPitch) % nWidth;
				int nSampleY2 = (nSampleY1 + nPitch) % nWidth;

				float fBlendX = (float)(x - nSampleX1) / (float)nPitch;
				float fBlendY = (float)(y - nSampleY1) / (float)nPitch;

				float fSampleT = (1.0f - fBlendX) * fSeed[nSampleY1 * nWidth + nSampleX1] + fBlendX * fSeed[nSampleY1 * nWidth + nSampleX2];
				float fSampleB = (1.0f - fBlendX) * fSeed[nSampleY2 * nWidth + nSampleX1] + fBlendX * fSeed[nSampleY2 * nWidth + nSampleX2];

				fScaleAcc += fScale;
				fNoise += (fBlendY * (fSampleB - fSampleT) + fSampleT) * fScale;
				fScale = fScale / fBias;
			}

			// Scale to seed range
			fOutput[y * nWidth + x] = fNoise / fScaleAcc;
		}

}


/*
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
*/

void LinearSpacedArray(float a, float b, float num)
{

	const int sizeX = 400;
	const int sizeY = 400;
	float pMap[sizeX][sizeY] = { 0 };
	float sigmaX = 0.5;
	int center_x = sizeY / 2;
	int center_y  = sizeX / 2;
	int Largest_value = 1;
	for (int yMap = 0; yMap < sizeY; yMap++)
	{
		for (int xMap = 0; xMap < sizeX; xMap++)
		{
			float distx = abs(xMap - center_x);
			float disty = abs(yMap - center_y);
			float dist = sqrt(distx * distx + disty * disty);
			pMap[yMap][xMap] = dist;
		}
	}
	// Find Largest value in 2D array
	for (int i = 0; i < sizeX; i++)
	{
		for (int j = 0; j < sizeY; j++)
		{
			if (pMap[i][j] > Largest_value)
			{
				Largest_value = pMap[i][j];
			}
		}
	}
	qDebug() << "\nLargest number:" << Largest_value;
	for (int i = 0; i < sizeX; i++)
	{
		for (int j = 0; j < sizeY; j++)
		{
			float circle_grad = pMap[i][j] / Largest_value;
			float circle_sigmaX = circle_grad - sigmaX;
			float circle_mul = circle_sigmaX * 2;
			float circle_min = -circle_mul;
			
			float circle_normalize = circle_min * 255;
			float cicle_div = circle_normalize / 255;
			pMap[i][j] = circle_normalize;	
		}
	}
	Mat grayImage(400, 400, CV_32F, pMap);
	imwrite("Gray_Image_new.png", grayImage);
	system("pause");
}
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Gaussianui w;
	LinearSpacedArray(10, 20, 30);
	PerlinNoise2D(int nWidth, int nHeight, float *fSeed, int nOctaves, float fBias, float *fOutput);
	//maintest();
	w.show();
	return a.exec();
}
