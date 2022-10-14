#ifndef MAINWINDOW_HPP
#define MAINWINDOW_HPP

#include <string>
#include <iostream>
#include <QMainWindow>
#include <QMessageBox>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_convButton_clicked();

private:
    Ui::MainWindow *ui;
    QMessageBox msgbox;
};
#endif // MAINWINDOW_HPP
