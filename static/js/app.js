// Start the app
var app = {  
    init: function() {
        console.log('init');
        /* Menu burger for mobile */
        const visibleMenu = document.querySelector('.menu__mobile');
        const menuBurger = document.querySelector('.menu-mobile');
        let menuOpen = false;
        menuBurger.addEventListener('click', () => {
            if(!menuOpen) {
                menuBurger.classList.add('open');
                visibleMenu.classList.add('active')
                menuOpen = true;
            } else {
                menuBurger.classList.remove('open');
                visibleMenu.classList.remove('active')
                menuOpen = false;
            }
        });

        /*Welcome animation */
        var text = document.querySelector(".intro-welcome");
        var strText = text.textContent;
        var splitText = strText.split("");
        text.textContent = "";


        for (let i = 0; i < splitText.length; i++) {
            text.innerHTML += "<strong>"+ splitText[i] + "</strong>";
            
        }

        let char = 0;
        let timer = setInterval(onTick, 130);

        function onTick() {
            const strong = text.querySelectorAll('strong')[char];
            strong.classList.add('fade');
            char++
            if (char === splitText.length) {
                complete();
                return;
            }
        }

        function complete() {
            clearInterval(timer);
            timer = null;
        }

        /* Auto writing animation */

        texts = [
            'le cinéma. (^o^) </h5>',
            'les livres SF. └[∵┌] </h5>', 
            'les sensations fortes. </h5>',
            'écouter de la musique. </h5>',
            'l\'ambiance Cyberpunk. └[ ∵ ]┘ </h5>',
            'les jeux vidéos ',
            'coder pendant des heures ! <3 </h5>',
        ],

        count = 0;
        index = 0;
        currentText = '';
        letter = '';

        (function type() {
            if (count === texts.length) {
                count = 0
            }
            currentText = texts[count];
            letter = currentText.slice(0, ++index);

            document.querySelector('.writting').textContent = letter;
            if (letter.length === currentText.length) {
                count++;
                index = 0;
            }

            setTimeout(type, 350);
        }());
    },

}


//  We want to start 'init' on the load of each page.
document.addEventListener('DOMContentLoaded', app.init);