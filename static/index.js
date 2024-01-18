
//open or closed dropdown
function state(id){
    var menu = document.getElementById(id);
        if (menu.classList.contains("is-active")) {
          menu.classList.remove("is-active");
        } else {
          menu.classList.add("is-active");
        }
  }
  
  //select language
  function select(id1, id2) {
    var menu = document.getElementById(id1);
    menu.addEventListener("click", function select(event) {
        var opcionSeleccionada = event.target.textContent;
        document.getElementById(id2).innerHTML = opcionSeleccionada;
      });
  }

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

  



