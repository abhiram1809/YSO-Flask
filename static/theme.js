
 function myFunc(phrases) {
    for (i=0;i<phrases.length;i++){
    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = 'phrase';
    checkbox.name = 'interest';
    checkbox.value = 'phrase';
 
    var label = modal.createElement('label')
    label.htmlFor = 'phrase';
    label.appendChild(modal.createTextNode('${phrases[i]}'));
 
    var br = document.createElement('br');
    }
}