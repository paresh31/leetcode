class Solution {
public:
    string finalString(string s) {
        string emptyString = "";
        for (char ch : s){
            if (ch != 'i'){
                emptyString += ch;
            }
            else{
                int start = 0;
                int end = emptyString.length() - 1;
                while (start < end) {
                    swap(emptyString[start], emptyString[end]);
                    start++;
                    end--;
                }
            }
        }
        return emptyString;
        
    }
};