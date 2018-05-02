(function (window, undefined) {
    "use strict";
    //resolucao aqui
    const botao = document.getElementsByClassName('action-add');

    let totalNodes= 0;

    const randomColor = () => {
        const hexadecimais = '0123456789ABCDEF';
        let cor = '#';
        for (var i = 0; i < 6; i++ ) {
            cor += hexadecimais[Math.floor(Math.random() * 16)];
        }
        return cor;
    }

    const createNode = () =>{
      const pool= document.getElementById('pool');


      let thing = document.createElement('div');
      thing.setAttribute('class','thing')
      thing.setAttribute('style', 'background-color: '+ randomColor())
      pool.appendChild(thing);
      totalNodes++
      document.getElementById('info').innerHTML = "A Piscina Contém " + totalNodes + " Coisas."
      console.log(totalNodes  )
    }


    SEA.addEventListener(botao[0],"click", () => { createNode() })


}(window));

