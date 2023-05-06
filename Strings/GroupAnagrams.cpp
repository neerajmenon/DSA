#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> m;
        vector<vector<string> > res;
        for(string s : strs){
            string hash = s;
            sort(hash.begin(),hash.end());
            if(m.find(hash)==m.end()){
                m[hash]= vector<string>();
            }
            m[hash].push_back(s);
        }
        for(auto &p:m){
            res.push_back(p.second);
        }
        return res;
        
    }
};
