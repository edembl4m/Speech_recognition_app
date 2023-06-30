let num, array, width, context, logo, myElements, analyser, src, height;

let btn = document.querySelector('#start_rec');
let equal = document.querySelector('.equalizer');

num = 32; //кол-во столбцов

array = new Uint8Array(num*2);

width = 10; //ширина блока


function equalizer(x){

    if(context) return;

    console.log(x);

    for(var i = 0 ; i < num ; i++){
        logo = document.createElement('div');
        logo.className = 'logo';
        logo.style.background = '#2cb7ee';
        logo.style.minWidth = width+'px';
        equal.appendChild(logo);
    }

    myElements = document.getElementsByClassName('logo');
    context = new AudioContext();
    analyser = context.createAnalyser();

    navigator.mediaDevices.getUserMedia({
        audio: true
    }).then(stream => {
        src = context.createMediaStreamSource(stream);
        src.connect(analyser);
        loop();
    }).catch(error => {
        alert(error + '\r\n\ Отклонено. Страница будет обновлена!');
        location.reload();
    });
}


function loop() {
    window.requestAnimationFrame(loop);
    analyser.getByteFrequencyData(array);
    for(var i = 0 ; i < num ; i++){
        height = array[i+num];
        myElements[i].style.minHeight = height+'px';
        myElements[i].style.opacity = 0.008*height;
    }
}