/**
 * Given an integer k and a string s, find the length of the longest
 * substring that contains the most k distinct characters
 * 
 * For example, given s = "abcba" and k = 2, the longest substring
 * with k distinct characters is "bcb".
 */

var longestSubstringofKCharacters = function(s, k) {
    let dict = {};
    let currentWindowLength = 0;
    let startWindow = 0, maxLength = 1;

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        dict[char] = i;       

        if (Object.keys(dict).length > k) {
            startWindow = Math.min.apply(null, Object.values(dict));
            delete dict[s[startWindow]]
            startWindow++;
        }

        currentWindowLength = i - startWindow + 1;
        maxLength = Math.max(currentWindowLength, maxLength);
    }
    
    return maxLength;
}

console.log(longestSubstringofKCharacters("abcba", 2))