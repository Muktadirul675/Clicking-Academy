
var dir = "up";
const animate = () => {
    if(dir == "up"){
        $("#home_img").css({"margin-top":"47%"});
        dir = "down";
    }
    else if(dir == "down"){
        $("#home_img").css({"margin-top":"50%"});
        dir = "up";
    }
}


setInterval(animate, 1000);
