public class Solution_ReverseWordsInString {
    public String reverseWords(String s) {
        String output =  "";
        String[] substr = s.split("\s");
        for (int i = substr.length -1; i >= 0; i--) {
            if (! substr[i].trim().isEmpty()){
                output +=  substr[i];
                if (i != 0){
                    output += " ";
                }
                System.out.println(output);
            }
        }
        return output.trim();
    }
}
