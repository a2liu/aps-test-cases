#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define block_value_count block_size * 64
#define even_bitmask -6148914691236517206
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
struct PrimeIncremental {
  uint32_t value;
  uint32_t progress;

  inline PrimeIncremental(uint32_t _value, uint32_t _progress)
      : value(_value), progress(_progress) {}
};

uint32_t block_size;
uint32_t n;
uint32_t min_value = 2;
vector<uint64_t> values;
vector<PrimeIncremental> primes;

bool get_value(uint32_t idx) {
  const uint64_t &v = values[idx / 64];
  uint32_t bit_offset = idx % 64;
  return 0 != ((((uint64_t)1) << bit_offset) & v);
}
void set_value(uint32_t idx, bool value) {
  uint64_t &v = values[idx / 64];
  uint32_t bit_offset = idx % 64;
  if (value) {
    v |= ((uint64_t)1) << bit_offset;
  } else {
    v &= ~(((uint64_t)1) << bit_offset);
  }
}

void reset_sieve() {
  for (int i = 0; i <= block_size; i++)
    values[i] = even_bitmask;
}

void sieve_first_block(uint32_t max_value) {
  for (int p = 3; p < max_value; p++) {
    if (get_value(p - min_value)) {
      for (int i = p * p; i < max_value; i += p)
        set_value(i - min_value, false);
    }
  }

  for (int i = min_value; i < max_value; i++) {
    if (get_value(i - min_value)) {
      primes.emplace_back(i, max_value / i * i);
    }
  }

  min_value = max_value;
}

void sieve_incremental(uint32_t max_value) {
  reset_sieve();
  for (auto &prime : primes) {
    uint32_t starting_point = prime.progress;
    if (starting_point < min_value)
      starting_point += prime.value;
    uint32_t i;
    for (i = starting_point; i < max_value; i += prime.value) {
      set_value(i - min_value, false);
    }
    prime.progress = i;
  }
  min_value = max_value;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  uint32_t n;
  cin >> n;

  block_size = sqrt(n);
  values.reserve(block_size);
  primes.reserve(block_size / 4);
  for (int i = 0; i < block_size; i++) {
    values.push_back(even_bitmask);
  }
}
