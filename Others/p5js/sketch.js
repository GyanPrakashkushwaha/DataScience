
/* 
Here setup() function only run 1 time but the draw() function continuously runs for infinite times
We Can laverage multiple things because of this
*/

function setup() {
  createCanvas(1500, 600);
  console.log('setup function')
}

// code for random numbers 
function getRandomArtitrary(max,min) {
  return Math.random() *(max-min)+min;
  
}

function draw(){
  // background(200);

  // // line(200,200,300,300);

  // triangle(100,200,300,400,400);

  // rect(200,200,300,300)
  // console.log('draw function')

  R = getRandomArtitrary(0,255);
  G = getRandomArtitrary(0,255);
  B = getRandomArtitrary(0,255);
  
  fill(R,G,B)

  ellipse(mouseX,mouseY ,20,20)
  

}

