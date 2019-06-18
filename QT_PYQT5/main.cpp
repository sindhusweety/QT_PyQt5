#include "Gaussianui.h"
#include <QtWidgets/QApplication>
#include <iostream>
#include <QDebug>
#include <vector>
#include <cmath>
using namespace std;

void LinearSpacedArray(float a, float b, float num)
{
	double min = -10;
	double max = 10;
	int n = 400;
	vector<double> result;
	// vector iterator
	int iterator = 0;

	for (int i = 0; i <= n - 2; i++)
	{
		double temp = min + i * (max - min) / (floor((double)n) - 1);
		result.insert(result.begin() + iterator, temp);
		iterator += 1;
	}

	//iterator += 1;

	result.insert(result.begin() + iterator, max);
	double arr_x0[400];
	for (double i : result)
	{
		qDebug() << i << "\n";
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
