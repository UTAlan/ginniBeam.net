function updateChoices(textBox, selectBox) {
	var selectedArray = new Array();
	var count = 0;
	for(var i=0; i<selectBox.options.length; i++) {
		if(selectBox.options[i].selected) {
			selectedArray[count++] = selectBox.options[i].value;
		}
	}
	textBox.value = selectedArray;
}

// Show the specified div when the first two parameters are equal
// Hide otherwise
function showOnEqual(selectBox, val, divID) {
  var myDiv = document.getElementById(divID);
  
  if(val == selectBox.options[selectBox.selectedIndex].value) {
    var newClass    = myDiv.className;
    myDiv.className = newClass.replace("hide", "");
  } else {
    myDiv.className += " hide";
  }
}

function resetForm(id) {
	$('#'+id).each(function(){
    this.reset();
	});
}