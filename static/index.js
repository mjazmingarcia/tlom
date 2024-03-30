  //Check if Storage is supported by the browser
  if (typeof(Storage) != 'undefined'){
    console.log(Storage);
  }else{
    alert("Storage no es complatible en este navegador. No podrá recordar las preferencias e historial de su última sesión en este sitio.")
  }


  var textarea = document.getElementById('textarea');
  //window.onload = textareaLength();
  // Display textarea typed char / maximum lenght
  function textareaLength() {
      var maxLength = 30;
      var textareaLength = textarea.value.length;
      //var charactersCount = maxLength - textAreaLength;
      var count = document.getElementById('char-counter');
      count.textContent = textareaLength + " / " + maxLength;
  }
  window.addEventListener("load", textareaLength, false);
  textarea.addEventListener('input', textareaLength, false);

  const srcLangSelect = document.querySelector('#select1');
  const tgtLangSelect = document.querySelector('#select2');

  // Save the selected choice to LocalStorage
  function saveSelect() {
    localStorage.setItem('SrcLang', srcLangSelect.value);
    localStorage.setItem('TgtLang', tgtLangSelect.value);
  }

  // Retrieve the saved choices from LocalStorage on page load
  if (localStorage.getItem('SrcLang')) {
    srcLangSelect.value = localStorage.getItem('SrcLang');
  }
  if (localStorage.getItem('TgtLang')) {
    tgtLangSelect.value = localStorage.getItem('TgtLang');
  }

  const optionsSrc = Array.from(srcLangSelect.options).map(option => option.value);
  const optionsTgt = Array.from(tgtLangSelect.options).map(option => option.value);
  
  //Swap select options when both selects values are the same
  const swap = document.querySelector(".swap-btn")  
  if (JSON.stringify(optionsSrc) === JSON.stringify(optionsTgt)){
    swap.addEventListener('click', swapOptions, false)}
  
  function swapOptions() {
    const srcLangValue = srcLangSelect.value;
    srcLangSelect.value = tgtLangSelect.value;
    tgtLangSelect.value = srcLangValue;

    saveSelect()
}


 ///storage history
 function saveHistory() {
     tableData =[]
     const tableRows = document.querySelectorAll("#my-history-list tr");
     tableRows.forEach((row) => {
        const cellValue = row.cells[0].textContent; // Assuming only one column
        tableData.push(cellValue);
     //store data
     localStorage.setItem("tableData", JSON.stringify(tableData));   
     console.log('Se actualizó el historial')
    });
 }


 const historyList= document.querySelector('#my-history-list')
 // Retrieve the saved history from LocalStorage on page load
 if (localStorage.getItem('tableData')) {
  const storedData = JSON.parse(localStorage.getItem("tableData") || "[]");
  console.log('Se importó historial desde LocalStorage');
  for (const item of storedData) {    
      const historyRow = document.createElement("tr");
      const historyItem = document.createElement('td');
      historyItem.textContent = item; 
      historyRow.appendChild(historyItem)
      historyList.appendChild(historyRow)
  }
 }

  //for burger menu show/hide
  const menu = document.querySelector("#nav-links")
  const burger = document.querySelector("#burger")  
  burger.addEventListener('click', ()=> {
    menu.classList.toggle("desktop")
    menu.classList.toggle("is-active")
    burger.classList.toggle("is-active")
  })

       // height of history
  function adjustHeight() {
    const topPosition = historyBox.offsetTop;
    const availableHeight = document.body.clientHeight - topPosition;
    historyBox.style.height = availableHeight + 'px';
  }
      // Set the initial height
  window.addEventListener("load", adjustHeight, false);

  
  const history = document.querySelector("#history-btn")
  const chevron = document.querySelector("#icon-chng")
  const historyBox = document.querySelector("#my-history")

    
  history.addEventListener('click', ()=> {
    history.classList.toggle("is-active");
    chevron.classList.toggle("fa-chevron-right");
    if (historyBox.style.display === "none") {
      historyBox.style.display = "block";
            adjustHeight();
    } else {
      historyBox.style.display = "none";
    }
    if (document.getElementById('main').style.marginRight) {
      document.getElementById('main').style.marginRight = '';
    } else {
      document.getElementById('main').style.marginRight = '170px';
    }
  })

      // Create a ResizeObserver instance
  const resizeObserver = new ResizeObserver(adjustHeight);
      // Observe the document body for size changes
  resizeObserver.observe(document.body);


//Client-side data validation and POST request
function validate() {
  const parraf = document.getElementById('warning');
  parraf.textContent='';
  let text = textarea.value.trim();

  if (text.length === 0) {
    parraf.textContent="Por favor escriba algo de texto"
    return false;
  }else{
    if (srcLangSelect.value == "" && tgtLangSelect.value == "" && textarea.value == "") {
      parraf.textContent="Por favor llena todos los campos"
      return false;
    }
    
    if (srcLangSelect.value == "" && tgtLangSelect.value == "" && !textarea.value == "") {
      parraf.textContent="Por favor selecciona la lengua de tu texto y la lengua a la que deseas traducirlo";
      return false;
    }

    if (srcLangSelect.value == "" && !tgtLangSelect.value == "" && !textarea.value == "") {
      parraf.textContent="Por favor selecciona la lengua de tu texto";
      return false;
    }

    if (tgtLangSelect.value == "" && !srcLangSelect.value == "" && !textarea.value == "") {
      parraf.textContent="Por favor selecciona la lengua a la que deseas traducir tu texto";
      return false;
    }

    if (!srcLangSelect.value == "" && tgtLangSelect.value == "" && textarea.value == "") {
      parraf.textContent="Por favor selecciona la lengua a la que deseas traducir y añade tu texto";
      return false;
    }

    if (textarea.value == "" && !srcLangSelect.value == "" && !tgtLangSelect.value == "") {
      parraf.textContent="Por favor escribe un texto para traducir";
      return false;
    }
    }
  //return true;  
  sendData();
}

submitButton = document.getElementById('submit-btn')
//resultArea = 
function showLoad(){
  submitButton.classList.add('is-loading');
  document.getElementById('mytextarea2').textContent='Traduciendo...'
}

function removeLoad(){
  submitButton.classList.remove('is-loading')
}

function sendData(){
      console.log('Traduciendo....')  
      showLoad();
        // Get values
        const value1 = srcLangSelect.value;
        const value2 = tgtLangSelect.value;
        const value3 = textarea.value.trim();

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
            'Content-Type': 'application/json; charset=UTF-8'
          }
        })
        .then(response => response.json())
        .then(data => {
          removeLoad();
          //aquí agregar selección de elemento traduccion{} y agregar respuesta
          document.getElementById('mytextarea2').textContent=data.translation;
          console.log(data.translation)
          //aqui historial
          updateHistory(data);
          saveHistory();
          //aqui agregar seleccionde elemento de diccionario y agregar palabras
          if (data.examples){
            updateDictionary(data);
            //console.log(data.examples);
          }else{document.querySelector('#my_dictionary').textContent='No hay ejemplos para mostrar'}
        })
        .catch(error => {
          console.error(error);
        });
      
}


function updateDictionary(obj){
  const section= document.querySelector('#my_dictionary');
  section.textContent = ""
  const examples = obj.examples;

  for (const [key1, value1] of Object.entries(examples)) {
    const myArticle = document.createElement("div");
    myArticle.classList.add('columns'); // Add any desired CSS class
    const myColumn1 = document.createElement("div");
    myColumn1.classList.add('column', 'is-narrow', 'pt-5');
    const myColumn2 = document.createElement("div");
    const myH2=document.createElement('h2');
    myColumn2.classList.add('column');
    const myList = document.createElement("ol");
    //console.log(key1 + ':', value1);
    myH2.textContent = key1;
    

    for (const [key, value] of Object.entries(value1)) {
      const listItem = document.createElement("li");
      const valueSpan1 = document.createElement("span");
      valueSpan1.textContent = `${key}`;
      valueSpan1.classList.add('has-text-weight-medium', 'has-text-black-ter');
      listItem.appendChild(valueSpan1);
      
      const lineBreak = document.createElement("br");
      listItem.appendChild(lineBreak);

      const valueSpan2 = document.createElement("span");
      valueSpan2.textContent = value;
      valueSpan2.style.fontStyle = "italic";
      listItem.appendChild(valueSpan2);
      
      myList.appendChild(listItem);
    }
    myColumn1.appendChild(myH2)
    myArticle.appendChild(myColumn1);
    myColumn2.appendChild(myList);
    myArticle.appendChild(myColumn2);

    section.appendChild(myArticle);
  }
}

function updateHistory(obj){
  const historyRow = document.createElement("tr");
  const historyItem= document.createElement('td');
  historyItem.textContent = obj.srctext+': '+obj.translation; 
  historyRow.appendChild(historyItem)
  historyList.appendChild(historyRow)
}