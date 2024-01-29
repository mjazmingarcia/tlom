  //for burger menu show/hide
  const menu = document.querySelector("#nav-links")
  const burger = document.querySelector("#burger")  
  burger.addEventListener('click', ()=> {
    menu.classList.toggle("is-active")
    burger.classList.toggle("is-active")
  })

  //show/hide history list
  const history = document.querySelector("#history-btn")
  const chevron = document.querySelector("#icon-chng")
  const historyList = document.querySelector("#my-history")
  history.addEventListener('click', ()=> {
    history.classList.toggle("is-active");
    chevron.classList.toggle("fa-chevron-right");
    if (historyList.style.display === "none") {
      historyList.style.display = "block";
    } else {
      historyList.style.display = "none";
    }
    if (document.getElementById('main').style.marginRight) {
      document.getElementById('main').style.marginRight = '';
    } else {
      document.getElementById('main').style.marginRight = '170px';
    }
  })


//Client-side data validation and POST request
function validate() {
  const select1 = document.querySelector("#select1");
  const select2 = document.querySelector("#select2");
  const textarea = document.querySelector("#textarea");
  const parraf = document.getElementById('warning');
  parraf.innerHTML=''
  let text = textarea.value.trim();

  if (text.length === 0) {
    parraf.innerHTML="Por favor escriba algo de texto"
    return false;
  }else{
    if (select1.value == "" && select2.value == "" && textarea.value == "") {
      parraf.innerHTML="Por favor llena todos los campos"
      return false;
    }
    
    if (select1.value == "" && select2.value == "" && !textarea.value == "") {
      parraf.innerHTML="Por favor selecciona la lengua de tu texto y la lengua a la que deseas traducirlo";
      return false;
    }

    if (select1.value == "" && !select2.value == "" && !textarea.value == "") {
      parraf.innerHTML="Por favor selecciona la lengua de tu texto";
      return false;
    }

    if (select2.value == "" && !select1.value == "" && !textarea.value == "") {
      parraf.innerHTML="Por favor selecciona la lengua a la que deseas traducir tu texto";
      return false;
    }

    if (!select1.value == "" && select2.value == "" && textarea.value == "") {
      parraf.innerHTML="Por favor selecciona la lengua a la que deseas traducir y añade tu texto";
      return false;
    }

    if (textarea.value == "" && !select1.value == "" && !select2.value == "") {
      parraf.innerHTML="Por favor escribe un texto para traducir";
      return false;
    }
    }
  //return true;  
  sendData();
}

function sendData(){
        // Get DOM input and select objects
      const button = document.querySelector('#submit-btn');
      const select1 = document.querySelector('#select1');
      const select2 = document.querySelector('#select2');
      const textarea = document.querySelector('#textarea');

        // Get values
        const value1 = select1.value;
        const value2 = select2.value;
        const value3 = textarea.value;

        // build values object 
        const data = {
          text: value3,
          source_lang: value1,
          target_lang: value2
        };

        // send to server
        let path = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port;
        fetch(path + '/translate', {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
        })
        .catch(error => {
          console.error(error);
        });
      

  document.getElementById("mytextarea2").innerHTML='hola'

}

