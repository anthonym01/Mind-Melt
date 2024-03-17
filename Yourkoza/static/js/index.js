
window.addEventListener('load', async function () {//Starting point
    try {
        await config.load()
    } catch (err) {
        console.warn('Something bad happened: ', err)
    } finally {
        this.document.getElementById('compile_button').addEventListener('click', compile_and_run);
    }
});

let state = {
    running: false,
}

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


async function compile_and_run() {
    /**
 * The function `compile_and_run` takes user input code, sends a POST request to a server, receives
 * output, and displays it in a console emulation space on a webpage.
 * @returns The `compile_and_run` function is returning `false` if the program is already running. If
 * there is an error during the execution of the function, it does not explicitly return anything, so
 * it implicitly returns `undefined`.
 */

    if (state.running) {
        console.log('Program allready running');
        state.running = false;

        //Replace with reset function later
        compile_and_run()
        return false;
    }
    try {
        document.getElementById('console_emulation_space').classList="console_emulation_space_focus";
        
        let code_string = document.getElementById('codeinput').value;
        console.log('compile and run', code_string)
        state.running = true;

        /* This block of code is making a POST request to the server with the code input provided by the user. */
        const response = await fetch('/post/code_string', {
            method: "POST",
            body: JSON.stringify({ code_string }),
            headers: { "Content-type": "application/json; charset=UTF-8" }
        });

        if (!response.ok) { throw new Error('Network failiure'); }

        const code_output = await response.json();
        console.log(code_output);

        document.getElementById('console_emulation_space').innerHTML = "";

        for (const line_number in code_output) {
            let Console_block = document.createElement('div');
            Console_block.classList = "Console_block";
            Console_block.setAttribute('name', line_number)
            Console_block.setAttribute('id', line_number)

            Console_block.innerText = `${code_output[line_number]}`;

            document.getElementById('console_emulation_space').appendChild(Console_block)
        }
        /*
        code_output.forEach(console_line_text => {
            let Console_block = document.createElement('div');
            Console_block.classList="Console_block";
            Console_block.setAttribute('name',console_line_text)
            Console_block.innerText=console_line_text;
            
            document.getElementById('console_emulation_space').appendChild(Console_block)
        });*/

    } catch (error) {

    }

}