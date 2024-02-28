/*
 * Implement an autocomplete system. That is given a query string 's' 
 * and a set of possible query strings, return all strings in the set
 * that have 's' as a prefix
 * 
 * For example, given a query string de and the set of strings [dog, 
 * deer, deal] return [deer, deal]
 */

let queryString = "de";
let possibleStrings = ["dog", "deer", "deal"];
let autocomplete = [];

possibleStrings.forEach(s => {
    if (s.startsWith(queryString))
        autocomplete.push(s)
});

console.log(autocomplete)