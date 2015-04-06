var buttonnode= document.createElement('input');
buttonnode.setAttribute('type','button');
buttonnode.setAttribute('name','sal');
buttonnode.setAttribute('value','sal');
// cell1.appendChild(buttonnode);
buttonnode.attachEvent('OnClick',visitPage());
function visitPage(){
        window.location='http://www.google.com';
    }

