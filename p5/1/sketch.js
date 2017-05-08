function setup() {
  createCanvas(windowWidth, windowHeight);
  //frameRate(60);
  //background(20, 20, 20);
  fill(0);
  posX = windowWidth / 2;
  posY = windowHeight /2;
  velX = 1;
  velY = 1;
  blendMode(REPLACE);
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  //background(20, 20, 20);
}

function draw() {
  ellipse(posX, posY, 80, 80);
  move();
}

function move() {
  posX += velX;
  if (posX > windowWidth) {
    velX *= -1;
  }
  posY += velY;
  if (posY > windowHeight) {
    velY *= -1;
  }
}