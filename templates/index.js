var canvas;
var context;

function draw(e) {
    if (isDrawing === true) {   
        var x = e.pageX - canvas.offsetLeft;
        var y = e.pageY - canvas.offsetTop;
		
		context.lineTo(x, y);
		context.stroke();
	}
}

function startDrawing (e) {
	isDrawing = true;
	context.beginPath();
	context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop);
}

function stopDrawing () {
    isDrawing = false;	
}

function clearCanvas () {
	context.clearRect(0, 0, canvas.width, canvas.height);
}

window.onload = function () {
    
    canvas = document.getElementById("drawingCanvas");
    context = canvas.getContext("2d");
    context.strokeStyle = 'rgb(0,0,0)';
    context.lineWidth = 5;
    canvas.onmousedown = startDrawing;
    canvas.onmouseup = stopDrawing;
    canvas.onmouseout = stopDrawing;
    canvas.onmousemove = draw;
}