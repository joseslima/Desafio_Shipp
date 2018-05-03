(function (window, undefined) {
    "use strict";
    //resolucao aqui

    let idsThings = 0;

    const controler = () => {
      removeAll();

      const adicionar = (document.getElementsByClassName('action-add'))[0];
      SEA.addEventListener(adicionar,"click", () => { createNode() })

      const remover = (document.getElementsByClassName('action-remove'))[0];
      SEA.addEventListener(remover,"click", () => {removeAll()})

    }

    const removeAll = () =>{
      const pool = document.getElementById('pool');

      while (pool.firstChild){
        pool.removeChild(pool.firstChild)
      }

    }

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
        let counter = pool.childElementCount + 1
        let thing = document.createElement('div');

        thing.setAttribute('class','thing');
        thing.style.background = randomColor();
        thing.setAttribute('id', idsThings);

        let color = (document.createElement('button'))
        color.setAttribute('class','action-change-color');
        color.setAttribute('id',idsThings+'color')

        SEA.addEventListener(color,"click", (e) => {
          let thing = (document.getElementById(e.toElement.attributes.id.value)).parentNode;
          thing.style.background = randomColor();
         } )

        let remove = (document.createElement('a'));

        remove.setAttribute('class','action-remove');
        remove.setAttribute('id', idsThings+"remove");
        remove.setAttribute('href','#')

        SEA.addEventListener(remove, "click", (e) =>{
          e.preventDefault();
          let thing = (document.getElementById(e.toElement.attributes.id.value)).parentNode;
          thing.parentNode.removeChild(thing)

        })

        remove.appendChild(document.createTextNode('remover'));

        color.appendChild(document.createTextNode('color'));
        thing.appendChild(color);

        thing.appendChild(remove)
        pool.appendChild(thing);

        idsThings ++;

        document.getElementById('info').innerHTML = "A Piscina Contém " + counter + " Coisas.";

    }

    controler();



}(window));
