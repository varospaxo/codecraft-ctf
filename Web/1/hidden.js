const longlist = [132, 56, 124, 109, 56, 123, 124, 104, 58, 73, 102, 122, 56, 102, 58, 106, 59, 119, 60, 130, 77, 91, 74, 82, 74];
const background = () => {
    let intermediateArray = [];
    let list = "";
    longlist.forEach((char, index) => {
        intermediateArray[index] = char ^ (index % 5);
    });
    const additionalProcessing = intermediateArray.map((char, index) => {
        return (char * 3 + 5 - index) % 256;
    });
    additionalProcessing.forEach(char => {
        if (char >= 32 && char <= 126) {
            list += String.fromCharCode(char);
        }
    });
    console.log("Debug info:", intermediateArray);
    console.log("Processed array:", additionalProcessing);
    console.log(list);
};
const runner = () => {
    let list = "";
    longlist.forEach(char => {
        char -= 7;
        list += String.fromCharCode(char);
    });
    list = list.split('').reverse().join('');
    console.log(list);
};
background();