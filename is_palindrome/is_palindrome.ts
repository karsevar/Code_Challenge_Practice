// Bruteforce with single loop.
// o(log(n)) I believe is the time complexity since we are only going through at most half of 
// the passed in number each function call due to the two pointers.
function isPalindrome(x: number): boolean {
    const xString: string = x.toString();
    console.log(xString[0]);

    let i: number = 0;
    let j: number = xString.length - 1;

    while (i != j && i < j){
        if (xString[i] != xString[j]) {
            return false
        } else {
            i += 1;
            j -= 1;
        }
    }
    return true
};

function isPalindromeSplit(x: number): boolean {
    // using the same convert the number into a string method I can actually find the middle point
    // of the resulting string and split the two halves from that mid point and reverse the left 
    // half and simply use an equal operation to check for if the string is a palindrome or not.

    // issue is that I will need to watch out for odd number length x values. 

    let xString: string = x.toString();
    let midPoint: number = Math.floor(xString.length / 2);
    if (xString.length % 2 !== 0) {
        console.log(xString.slice(0, midPoint))
        console.log(xString.slice(midPoint+1, xString.length))
        return xString.slice(0, midPoint) === xString.slice(midPoint+1, xString.length).split("").reverse().join("");
    } else {
        console.log(xString.slice(0, midPoint))
        console.log(xString.slice(midPoint, xString.length))
        return xString.slice(0, midPoint) === xString.slice(midPoint, xString.length).split("").reverse().join("");
    }
};