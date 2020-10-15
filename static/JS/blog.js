$("#menu-toggle").click(()=>{
    if($("#sidebar").hasClass("c_close")){
        console.log("Clicked");
        $("#sidebar").removeClass("c_close");
        $("#sidebar").addClass("c_open");
    }else{
        $("#sidebar").removeClass("c_open");
        $("#sidebar").addClass("c_close");
    }
});

// $("#sidebar_btn").click(()=>{
//     if($("#sidebar").hasClass("c_close")){
//         console.log("Clicked");
//         $("#sidebar").removeClass("c_close");
//         $("#sidebar").addClass("c_open");
//     }else{
//         $("#sidebar").removeClass("c_open");
//         $("#sidebar").addClass("c_close");
//     }
// });
