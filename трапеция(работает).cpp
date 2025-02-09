#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return x * 5 * sin(x) * sin(x);
}

double trapezoidalIntegration(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (f(a) + f(b));

    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        sum += f(x);
    }

    return h * sum;
}

int main() {
    double a;  
    double b;  
    int n = 1000; 
    double e = 0.100;   
    
     cout << "Введите начальное значение интервала интегрирования: ";
    cin >> a;

    cout << "Введите конечное значение интервала интегрирования: ";
    cin >> b;
    
    
    double result = trapezoidalIntegration(a, b, n);
    cout << "Значение интеграла: " << result << std::endl;

    return 0;
}

