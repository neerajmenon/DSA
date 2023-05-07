#include <unordered_map>
#include <vector>

using namespace std;

//Solution with map and bucket sort
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (int n : nums) {
            count[n] = 1 + count[n];
        }

        for (auto& p : count) {
            freq[p.second].push_back(p.first);
        }

        vector<int> res;
        for (int i = freq.size() - 1; i > 0 && res.size() < k; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};


//Solution with map only
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
