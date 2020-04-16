#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define debug(expr)                                                            \
  cerr << "\033[1;31m"                                                         \
       << "at line " << __LINE__ << ": "                                       \
       << "\033[0m" << #expr << " equals `" << expr << '`' << std::endl;

/*
 * Tips:
 * 1. std::set is ordered, you want std::unordered_set for a hashset
 * 2. Same for maps, std::unordered_map is the hashmap
 * 3. You can multiply numbers by -1 to turn a Min heap into a max heap
 * 4. #include <algorithm> gets you 90% of the way through most problems;
 * there's some mighty fine wheels in there, so don't reinvent them if you don't
 * have to
 */

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
}
