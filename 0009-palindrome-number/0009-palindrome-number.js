/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){
        return false
    }
    let copy = x
    // copy = copy.split('').reverse().join('')
    return copy == x.toString().split("").reverse().join('')
    
};