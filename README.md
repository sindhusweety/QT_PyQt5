# QT_PyQt5

QT is a a free open source widget tool for creating graphical user interface as well as cross platform application that runs 
on various software and hardware such as linux,windows and etc

to install pyqt5
sudo apt install pyqt5

pyuic5 -x project.ui -o project.py

to import image
click 
"<RCC>
  <qresource prefix="home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images">
    <file>gaussian.qrc</file>
    <file>gaussian_formula.jpg</file>
  </qresource>
</RCC>
"
pyrcc5 image.qrc -o image_rc.py


python project.py
