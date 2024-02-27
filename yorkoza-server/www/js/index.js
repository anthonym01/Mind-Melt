
window.addEventListener('load', async function () {//Starting point
    try {
        await config.load()
    } catch (err) {
        console.warn('Something bad happened: ', err)
    } finally {

    }
});
async function request(what) {//basic request template

    try {
        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {//wait for and handle response
            if (this.readyState == 4 && this.status == 200) {
                console.log('Server replied with: ', this.responseText, ' In response: ', this.response)
                return this.responseText
            }
        };

        xhttp.open("GET", what, true);//get request
        xhttp.send();
    } catch (err) {
        console.warn('xhttp request failed ', err);
    }

}

async function post(what, where) {//basic post
    let xhttp = new XMLHttpRequest()
    
    /*let response = await xhttp.onreadystatechange(()=>{

    })*/

    xhttp.onreadystatechange = function () {//wait for and handle response
        if (this.readyState == 4 && this.status == 200) {
            console.log('Server replied with: ', this.responseText, ' In response: ', this.response)
        }
    };
    xhttp.open("POST", where, true);
    xhttp.send(JSON.stringify(what));
}

//Test post button
document.getElementById('testpost_btn').addEventListener('click',function(){
    console.log("testpost");
    post(JSON.stringify({payload:document.getElementById('postablegarbage').value}),'/post/test');
})

//local storage handler
let config = {
    data: {//Loacal app data
        
    },
    save: async function () {//Save the config file
        console.table('Configuration is being saved', config.data)
        localStorage.setItem("express_cfg", JSON.stringify(config.data))
    },
    load: function () {//Load the config file
        console.warn('Configuration is being loaded')
        config.data = JSON.parse(localStorage.getItem("express_cfg"))
        console.log('config Loaded from application storage')
    },
    delete: function () {//Wjipe stowage
        localStorage.clear("express_cfg");//yeet the storage key
        console.log('config deleted: ');
        console.table(config.data);
        config.data = {};
    },

}
