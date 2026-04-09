class Solution {
public:
    bool judgeCircle(string moves) {
        if (moves.size()==0)
            return true;

        int count_moves[4]={0,0,0,0};
        for (int i=0; i< moves.size(); ++i){
            if (moves[i]=='U')
                count_moves[0]++;
            else if (moves[i]=='D')
                count_moves[1]++;
            else if (moves[i]=='R')
                count_moves[2]++;
            else
                count_moves[3]++;
        }

        // for(int i=0;i<4;++i)
        //     cout<<count_moves[i]<<" ";
        if ((count_moves[0]==count_moves[1]) & (count_moves[2]==count_moves[3]))
            return true;
        else
            return false;
    }
};

/*
Just count the number characters and compare between 'U' and 'D'; 'L' and 'R'. 
*/