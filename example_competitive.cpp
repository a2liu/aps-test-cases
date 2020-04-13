#include <bits/stdc++.h>
using namespace std;

// What do you mean by good software practice again?

// compile with g++ -DLOCAL_MACHINE -ggdb thisfile.cpp
#ifdef LOCAL_MACHINE
#define debug(expr)                                                            \
  cerr << "\033[1;31m"                                                         \
       << "at line " << __LINE__ << ": "                                       \
       << "\033[0m" << #expr << " equals `" << expr << '`' << std::endl;
#else
#define debug(expr)
#endif

// When you skiped the Algorithm class but still want to implement a BST
// uncomment the below line to use
// #define USE_POLICY_STL
#ifdef USE_POLICY_STL
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <typename T>
using OrderedTree = tree<T, null_type, less<T>, splay_tree_tag,
                         tree_order_statistics_node_update>;
#endif

/*
** Tips:
** 1. gcc has cool hidden features
**   - Policy STL (above)
**   - gp_hash_table (faster than unordered_*)
**   - Rope (at ext/)
**   - __gcd(a, b)
**
** 2. There are 'modern' C++ features you can use
**   - e.g. for (auto& [k, v] : s) to iterate a set
**   - decltype
**   - auto
** Will add more later
*/

int main() {
  // C-style IO will not work anymore
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  debug(1 + 1);
}
