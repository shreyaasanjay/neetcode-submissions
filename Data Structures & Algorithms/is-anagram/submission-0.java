class Solution {
    public boolean isAnagram(String s, String t) {
        char [] sarry = s.toCharArray();
        char [] tarry = t.toCharArray();
        Arrays.sort(tarry);
        Arrays.sort(sarry);
        if (tarry.length != sarry.length) {
            return false;
        }
        for (int i=0; i<tarry.length; i++) {
            if (!(tarry[i]==sarry[i])) {
                return false;
            }
        }
        return true;
        
            // for (int i=0; i<s.length(); i++) {
            //     if (!(t.contains(s.CharAt(i)))) {
            //         return false;
            //     }
            //     else if {
            //         if (t.contains(s.CharAt(i))) {
            //             if(t.substring(s.CharAt()))
            //         }
                    

            //     }
            // }
            // return true;
        
    }
}
//hi
//first check if string t contains all the letters that string s contains
//then make a new substring of s for every character of t checked 
// for ex: abcd and bcad once a is checked --> bcd is the new string t
// then keep going until string t length is zero and check if string s length us zero

