// // I wrote the algorithm as a function so that 
// // it would be a little more useful

let sentence = "The movie is not that bad, really I like it";
let sentence2 = "The movie is good really I like it";
let sentence3 = "The movie is not bad really I like it and it is awesome";
let sentence4 = "not bad oh boy";
let sentence5 = "not bad! oh boy";

const notBadIsGood = (sentence) => {
    // console.log(`The original sentence was: ${sentence}`)
    let sentenceArray = sentence.split('');
    let notIndex = sentence.indexOf("not");
    let badIndex = sentence.indexOf("bad");
    let deleteCount = (badIndex-notIndex)+3; // needed for splice to specify delete count
    // console.log(`The index of "not" is ${notIndex!=-1 ? notIndex : 'non-existent'} and the index of "bad" is ${badIndex!=-1 ? badIndex : 'non-existent'}.`) 
    if(badIndex!=-1 && notIndex!=-1 && badIndex > notIndex){ // only if both the word "not" and "bad" are in the sentence continue
        sentenceArray.splice(notIndex, deleteCount, 'good') 
        return sentenceArray.join('')
    }
    return sentence;
}

console.log(notBadIsGood(sentence))
console.log(notBadIsGood(sentence2))
console.log(notBadIsGood(sentence3))
console.log(notBadIsGood(sentence4))
console.log(notBadIsGood(sentence5))