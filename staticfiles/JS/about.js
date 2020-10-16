
var name = "Clicking Academy: A platform to learn code";
var msg = "";
var i = 0;

const write = () => {
    if (i >= name.length){
        clearInterval(interval);
        return 
    } 
    $("#name").html(msg += name[i++]);
}

const interval = setInterval(write, 200);
