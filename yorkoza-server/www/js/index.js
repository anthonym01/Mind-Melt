
window.addEventListener('load', async function () {//Starting point
    try {
        await config.load()
    } catch (err) {
        console.warn('Something bad happened: ', err)
    } finally {

    }
});

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
