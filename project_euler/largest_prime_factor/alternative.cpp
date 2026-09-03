#include <iostream>
using namespace std;

// largest prime number
// find the largest prime factor of a given number n
//
// alternative approach
// instead of iteratively searching for factors, and then checlking isprime()
// find the smallest factor, then divide it out (n/sf)
// continue factoring the smaller remaining number.
// by the time there are no more factors, whatever is left over is prime and is the largest prime factor
// this is much faster and how prime factorization algorithms work


long long find_factor(long long m) {
  for (int i=2; i*i<=m; i++) {
    if (m%i == 0) {
      m /= i;
      return find_factor(m);
    }
  }
  return m;
}

int main() {
  long long n;
  cin >> n;

  long long sf; // smallest factor

  long long lpf = find_factor(n);

  cout << "The largest prime factor of " << n << " is " << lpf << endl;
  return 0;
}
