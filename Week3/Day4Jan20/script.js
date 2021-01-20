// I wrote the algorithm as a function so that 
// it would be a little more useful

let sentence = "The movie is not that bad really I like it";
let sentence2 = "The movie is good really I like it";

const notBadIsGood = (sentence) => {
    // console.log(`The original sentence was: ${sentence}`)
    let wordNot = "not";
    let wordBad = "bad";
    let sentenceArray = sentence.split(' ');
    let notIndex = sentenceArray.indexOf(wordNot);
    let badIndex = sentenceArray.indexOf(wordBad);
    // console.log(`The index of "not" is ${notIndex!=-1 ? notIndex : 'non-existent'} and the index of "bad" is ${badIndex!=-1 ? badIndex : 'non-existent'}.`) 
    if(badIndex!=-1 && notIndex!=-1 && badIndex > notIndex){
        sentenceArray.splice(notIndex, badIndex-2, 'good')
        return sentenceArray.join(' ')
    }
    return sentence;
}


console.log(notBadIsGood(sentence))
console.log(notBadIsGood(sentence2))