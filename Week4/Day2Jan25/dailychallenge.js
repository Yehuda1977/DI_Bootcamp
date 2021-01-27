// Ask a user for several words (separated by commas).
// Push the words into an array.
// Console.log them, one per line, in a rectangular frame.
// For example, if the user gives you:
// Hello, World, in, a frame of asterisks
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

const frameWords = (words) => {
    
    let wordArray = words.split(',').map((word) => word.trim());
    

    console.log(wordArray)
    let longestWord = '';

    for(word of wordArray){
        if(word.length>=longestWord.length){
            longestWord = word;
        }
    }
    
    console.log('* '.repeat(longestWord.length))

    for(word of wordArray){
        console.log(`* ${word}${' '.repeat(longestWord.length-word.length)}  *`)
    }

    console.log('* '.repeat(longestWord.length))
    
}


let words = prompt("Write a series of words seperated by commas")
console.log(frameWords(words));