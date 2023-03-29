class Solution {
    public int solution(int n) {
        int answer = n;
        String nBinary = Integer.toBinaryString(n);
        int nCount = 0;
        
        for(int i = 0; i<nBinary.length(); i++){
            if(nBinary.charAt(i) == '1'){
                nCount++;
            }
        }
        
        
        while(true){
            answer += 1;
            String answerBinary = Integer.toBinaryString(answer);
            int answerCount = 0;
            
            for(int i = 0; i<answerBinary.length(); i++){
                if(answerBinary.charAt(i) == '1'){
                    answerCount++;
                }
            }
            if(nCount == answerCount){
                break;
            }
        }
        
        return answer;
    }
}