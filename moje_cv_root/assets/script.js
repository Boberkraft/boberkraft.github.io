 function randint(min, max) {
// includes min and max, returns int between.
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


//words in <head>
let total_combinations = first_word.length + second_word.length * words.length;


let last_word = 'xxxxx';

function start_typing() {


    let word = '';
    let i = 0;
    function type() {

        if (i < word.length) {
            document.getElementById('my_typing').innerHTML += word.charAt(i);
            i++;
            setTimeout(type, 100);
        } else {
            i = 0;

            setTimeout(function () {
                document.getElementById('my_typing').innerHTML = '';
                setTimeout(start_typing, 500);
            }, 1000);
        }

    }

    do {
        let choice = randint(1, total_combinations);

        if (choice <= words.length) {
            word = words[randint(0, words.length-1)];
        } else {
            n1 = first_word[randint(0, first_word.length-1)];
            n2 = second_word[randint(0, second_word.length-1)];
            word = `${n1} ${n2}`;
        }
    } while (word === last_word)
    last_word = word;
    type();


}
start_typing();



function activate_link(id) {
    let el = document.getElementById(id);
    el.setAttribute('data-edited', '1');
    setTimeout(function () {
        if (el.getAttribute("data-edited") === "1") {
            el.setAttribute('href', el.getAttribute("data-hidden-url"));
//            console.log(`OK dla ${id}`);
        }

    },300);
}
function deactivate_link(id) {
        let el = document.getElementById(id);
        el.setAttribute('data-edited', '2');
        el.removeAttribute('href');
//        console.log(`NIE dla ${id}`);

}