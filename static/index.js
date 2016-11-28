var canvas;
var context;

function draw(e) {
    if (isDrawing === true) {   
        var x = e.pageX - canvas.offsetLeft;
        var y = e.pageY - canvas.offsetTop - 100;
		
		context.lineTo(x, y);
		context.stroke();
	}
}

function startDrawing (e) {
	isDrawing = true;
	context.beginPath();
	context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop - 100);
}

function stopDrawing () {
    isDrawing = false;	
}

function clearCanvas () {
	context.clearRect(0, 0, canvas.width, canvas.height);
}

function scaleCanvas (canvas, width, height) {
		var w = canvas.width,
			h = canvas.height;
		if (width == undefined) {
			width = w;
		}
		if (height == undefined) {
			height = h;
		}

		var retCanvas = document.createElement('canvas');
		var retCtx = retCanvas.getContext('2d');
		retCanvas.width = width;
		retCanvas.height = height;
		retCtx.drawImage(canvas, 0, 0, w, h, 0, 0, width, height);
		return retCanvas;
	}

function SendRequest(){
    var canvas_buffer = scaleCanvas(canvas, 28, 28);
    var image = canvas_buffer.toDataURL("image/png");
    image = image.replace('data:image/png;base64,', '');
    $.ajax({
            type: 'POST',
            url: "/",
            data: '{ "ImageData" : "' + image + '" }',
            dataType: "json",    
            contentType: "application/json; charset=utf-8",
            success: function(response) {
                $("#Answer").animate({
                opacity: 0.0,
                }, 700, function() {
                     $("#Answer").text(response.answer);
                     $("#Answer").animate({ opacity: 1 }, 700 );
                }
     );
}
    });
}

window.onload = function () {
    
    canvas = document.getElementById("drawingCanvas");
    context = canvas.getContext("2d");
    
    context.strokeStyle = 'rgb(0,0,0)';
    context.lineWidth = 15;
    context.lineCap = "round";
    
    canvas.onmousedown = startDrawing;
    canvas.onmouseup = stopDrawing;
    canvas.onmouseout = stopDrawing;
    canvas.onmousemove = draw;
}



