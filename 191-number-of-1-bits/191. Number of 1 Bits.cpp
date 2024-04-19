class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t totalBits = sizeof(n)*8;
        int oneBit = 0;
        for(int checkBit=0;checkBit<totalBits;checkBit++){
            if(n & (1<<checkBit)){
                oneBit++;
            }
        }
        return oneBit;
    }
};