#include "mainwindow.hpp"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    msgbox.setWindowTitle("Message");
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_convButton_clicked()
{
    if (ui->cVal->text() == "" && ui->fVal->text() != "") {
        QString fD = ui->fVal->text();
        QString out = QString::number((9 / 5) * (fD.toFloat() - 32));
        ui->cVal->setText(out);
    }
    else if (ui->fVal->text() == "" && ui->cVal->text() != "") {
            QString cD = ui->cVal->text();
            QString out = QString::number(((9/5) * cD.toFloat()) + 32);
            ui->fVal->setText(out);
    }
    else {
        QString msg = "Both field should not be filled or left empty";
        msgbox.setText(msg);
        msgbox.exec();
    }
}
