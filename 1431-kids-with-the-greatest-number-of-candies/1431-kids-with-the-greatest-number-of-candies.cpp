class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> vec;
        int max = 0;
        int c; 
        for(int i=0; i < candies.size(); i ++){
            c = candies[i];
            max = c > max? c : max;
        }
        for(int i=0; i < candies.size(); i ++){
            c = candies[i];
            bool r = c + extraCandies >= max? true: false;
            vec.push_back(r);
        }
        return vec;
    }
    
};