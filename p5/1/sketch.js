function setup() {
    createCanvas(windowWidth, windowHeight);
    fill(255);
    bola = new Bola(50);  
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    //background(20, 20, 20);
}

function draw() {
    background(51);
    bola.move();
    bola.draw();
}

// The Bola class
function Bola(size) {
    this.size = size;
    this.x = windowWidth / 2;
    this.y = windowHeight / 2;
    this.xVel = random(-3, 3);
    this.yVel = random(-3, 3);
    
    this.move = function() {
        this.x += this.xVel;
        if (this.x > windowWidth - this.size/2 || this.x < this.size/2) {
            this.xVel *= -1;
        }
        
        this.y += this.yVel;
        if (this.y > windowHeight - this.size/2 || this.y < this.size/2) {
            this.yVel *= -1;
        }
    }
    
    this.draw = function() {
        ellipse(this.x, this.y, this.size, this.size)
    }
}