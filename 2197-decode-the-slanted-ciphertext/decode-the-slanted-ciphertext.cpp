class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {

        if (rows==1)
            return encodedText;

        int count_letters = 0;
        for (int i=0; i < encodedText.size(); ++i){
            if (encodedText[i]!=' ')
                count_letters +=1;
        }
        int columns_num = encodedText.size()/rows;
        string res="";
        for(int i=0; i<columns_num; ++i){
            int move_next_column = 0;
            for(int j=0; j< rows; ++j){
                int index = i + j*columns_num + move_next_column;
                if (index < encodedText.size()){
                    res.push_back(encodedText[index]);
                    if (encodedText[index]!=' ') count_letters--;
                    if (count_letters == 0)
                        return res; //Dừng
                }
                move_next_column++;
            }
        }
        return res;
    }
};

/*
(i,j) -> (i+1,j+1)

(i,j) => i*columns_num + j
(i+1,j+1) => (i+1)*columns_num + (j+1)
             = i*columns_num + j + columns_num + 1

*/