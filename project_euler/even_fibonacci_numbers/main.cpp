#include <iostream>
using namespace std;

int main() {
    const int limit = 4000000;

    long long f0 = 1;
    long long f1 = 2;
    long long sum = 0;

    // Add initial even term if it falls within the limit
    if (f1 % 2 == 0) {
        sum += f1;
    }

    while (true) {
        long long current = f0 + f1;
        if (current > limit) {
            break;
        }

        if (current % 2 == 0) {
            sum += current;
        }

        f0 = f1;
        f1 = current;
    }

    cout << "Sum : " << sum << endl;
    return 0;
}
