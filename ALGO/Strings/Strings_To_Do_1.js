// Remove Blanks
// Create a function that, given a string, returns all of that string’s contents, but without blanks. 

function removeBlanks(string) {
    array = string.split(" ")
    string = array.join("")
    console.log(string)
}

// removeBlanks(" Pl ayTha tF u nkyM usi c ") => "PlayThatFunkyMusic"
removeBlanks(" Pl ayTha tF u nkyM usi c ")
// removeBlanks("I can not BELIEVE it's not BUTTER") => "IcannotBELIEVEit'snotBUTTER"
removeBlanks("I can not BELIEVE it's not BUTTER")


// Get Digits
// Create a JavaScript function that given a string, returns the integer made from the string’s digits. You are allowed to use isNaN() and Number().

function getDigits(string) {
    number = ""
    for (i = 0; i <= string.length; i++) {
        if (isNaN(string[i]) == false) {
            number += string[i]
        }
    }
    number = Number(number)
    console.log(number)
}


// getDigits("abc8c0d1ngd0j0!8") => 801008
getDigits("abc8c0d1ngd0j0!8")
// getDigits("0s1a3y5w7h9a2t4?6!8?0") => 1357924680
getDigits("0s1a3y5w7h9a2t4?6!8?0")


// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized). You are allowed to use .split() and .toUpperCase().
function acronym(string) {
    array = string.split(" ")
    string1 = ""
    for (i = 0; i < array.length; i++) {
        string1 += array[i][0]
    }
    string1 = string1.toUpperCase()
    console.log(string1)
}
// acronym(" there's no free lunch - gotta pay yer way. ") => "TNFL-GPYW". 
acronym("there's no free lunch - gotta pay yer way.")
// acronym("Live from New York, it's Saturday Night!") => "LFNYISN".
acronym("Live from New York, it's Saturday Night!")

// Count Non-Spaces
// Create a function that, given a string, returns the number of non-space characters found in the string. 

function countNonSpaces(string) {
    array = string.split(" ")
    num = 0
    for (i = 0; i < array.length; i++) {
        num += array[i].length
    }
    console.log(num)
}

// countNonSpaces("Honey pie, you are driving me crazy") => 29
countNonSpaces("Honey pie, you are driving me crazy")
// countNonSpaces("Hello world !") => 11
countNonSpaces("Hello world !")

// Remove Shorter Strings
// Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.

function removeShorterStrings(array, num) {
    new_array = []
    for (i = 0; i < array.length; i++) {
        if (array[i].length >= num) {
            new_array.push(array[i])
        }
    }
    console.log(new_array)
}

// removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4) => ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)
// removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3) => ['There', 'bug', 'the', 'system']
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)