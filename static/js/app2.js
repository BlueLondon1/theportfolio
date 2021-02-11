// Start the app
var app = {  

    elements: [],

    init: function() {
        console.log('init');

        app.elements.daysEl = document.getElementById('days');
        app.elements.hoursEl = document.getElementById('hours');
        app.elements.minsEl = document.getElementById('mins');
        app.elements.secondsEl = document.getElementById('seconds');

        const newYears = '24 March 2021';

        function countdown() {
            const newYearsDate = new Date(newYears);
            const currentDate = new Date();

            const totalSeconds = (newYearsDate - currentDate) / 1000;

            const days = Math.floor(totalSeconds / 3600 / 24);
            const hours = Math.floor(totalSeconds / 3600) % 24;
            const mins = Math.floor(totalSeconds / 60) % 60;
            const seconds = Math.floor(totalSeconds) % 60;

            app.elements.daysEl.innerHTML = days;
            app.elements.hoursEl.innerHTML = hours;
            app.elements.minsEl.innerHTML = mins;
            app.elements.secondsEl.innerHTML = formatTime(seconds);
            
        };

        function formatTime(time) {
            return time < 10 ? (`0${time}`) : time;
        }

        setInterval(countdown, 1000)

        /* Menu burger for mobile */
        app.elements.visibleMenu = document.querySelector('.menu__mobile');

        app.elements.menuBurger = document.querySelector('.menu-mobile');

        let menuOpen = false;


        app.elements.menuBurger.addEventListener('click', () => {
            if(!menuOpen) {
                app.elements.menuBurger.classList.add('open');
                app.elements.visibleMenu.classList.add('active')
                menuOpen = true;
            } else {
                app.elements.menuBurger.classList.remove('open');
                app.elements.visibleMenu.classList.remove('active')
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
            'le cinéma. (^o^)</h5>',
            'lire des tonnes de livres └[∵┌] </h5>', 
            'les sensations fortes</h5>',
            'écouter de la musique</h5>',
            'l\'ambiance Cyberpunk └[ ∵ ]┘ </h5>',
            'les jeux vidéos',
            'coder pendant des heures <3 ! </h5>',
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

            setTimeout(type, 300);
        }());
    },


    

}


//  We want to start 'init' on the load of each page.
document.addEventListener('DOMContentLoaded', app.init);