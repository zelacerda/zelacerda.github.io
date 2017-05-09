var bolas;

function setup() {
    createCanvas(windowWidth, windowHeight);
    fill(255);
    bolas = new Bolas(20);  
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

function draw() {
    background(51);
    bolas.update();
}

// The Bola class
var Bola = function() {
    this.size = random(40) + 10;
    this.x = windowWidth / 2;
    this.y = windowHeight / 2;
    this.xVel = random(-3, 3);
    this.yVel = random(-3, 3);
};

Bola.prototype.run = function() {
    this.move();
    this.draw();
};

Bola.prototype.move = function() {
    this.x += this.xVel;
    if (this.x > windowWidth - this.size/2 || this.x < this.size/2) {
        this.xVel *= -1;
    }

    this.y += this.yVel;
    if (this.y > windowHeight - this.size/2 || this.y < this.size/2) {
        this.yVel *= -1;
    }
};

Bola.prototype.draw = function() {
    ellipse(this.x, this.y, this.size, this.size)
};

// A class for balls
var Bolas = function(number) {
    this.number = number;
    this.bolas = [];
    for (var i = 0; i < this.number; i++) {
        this.bolas.push(new Bola());
    }
};

Bolas.prototype.update = function() {
    for (var i = 0; i < this.number; i++) {
        this.bolas[i].run();
    }
};