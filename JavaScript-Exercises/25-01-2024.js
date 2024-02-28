/* Exercise: 
 * Given a list of numbers and a number k, return whether any two of numbers
 * add from the list add up to k.
 * 
 * Example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
 */

let k = 17
const numbers = [10, 15, 3, 7];

numbers.every(i => {
    numbers.every(j => {
        if(i + j == k){
            console.log(i + " + " + j + " equals " + k);
            return false;
        }
        return true;
    })
})