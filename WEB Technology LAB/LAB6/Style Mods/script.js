const styleBox = document.getElementById("styleBox");

function colorPicker(){
  var colorPicker = document.getElementById("colorPicker");
  styleBox.style.backgroundColor = colorPicker.value;
}

function textColorPicker(){
  var textColorPicker = document.getElementById("textColorPicker");
  styleBox.style.color = textColorPicker.value;
}

function textSize(){
  var textSize = document.getElementById("textSize");
  styleBox.style.fontSize = `${textSize.value}px`;
}

function widthInput(){
  var widthInput = document.getElementById("widthInput");
  styleBox.style.width = `${widthInput.value}px`;
}

function heightInput(){
  var heightInput = document.getElementById("heightInput");
  styleBox.style.height = `${heightInput.value}px`;
}

function borderRadiusRange(){
  var borderRadiusRange = document.getElementById("borderRadiusRange");
  styleBox.style.borderRadius = `${borderRadiusRange.value}px`;
}
