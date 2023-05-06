#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            ++freq[num];
        }
        
        vector<int> result;
        for (int i = 0; i < k; ++i) {
            int max_freq = 0;
            int max_num = 0;
            for (auto it = freq.begin(); it != freq.end(); ++it) {
                if (it->second > max_freq) {
                    max_freq = it->second;
                    max_num = it->first;
                }
            }
            result.push_back(max_num);
            freq.erase(max_num);
        }
        
        return result;
    }
};
