
window.addEventListener('load', async function () {//Starting point
    try {
        await config.load()
    } catch (err) {
        console.warn('Something bad happened: ', err)
    } finally {
        code_handler.initalize();
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

let ui_handler = {
    initalize: async function () {

    },
    blurse: async function () {
        console.log('Blur UI')
        document.getElementById('headbar').classList = "headbar blured"
        document.getElementById('blurser').classList = "blurser visible"
        document.getElementById('Coding_view').classList = "main_view visible blured"

    }
}

let code_handler = {
    state: {
        running: false,
    },
    editor: false,
    initalize: async function () {
        document.getElementById('compile_button').addEventListener('click', code_handler.compile_and_run);

        this.editor = ace.edit("editor", {
            //theme: "ace/theme/GitHub",
            //theme: "ace/theme/dracula",
            //theme: "ace/theme/twilight",
            theme: "ace/theme/vibrant_ink",
            mode: "ace/mode/javascript",
            //maxLines: 30,
            wrap: true,
            autoScrollEditorIntoView: true
        });
        //editor.setTheme("ace/theme/monokai");
        //editor.session.setMode("ace/mode/javascript");
    },
    compile_and_run: async function () {

        /**
     * The function `compile_and_run` takes user input code, sends a POST request to a server, receives
     * output, and displays it in a console emulation space on a webpage.
     * @returns The `compile_and_run` function is returning `false` if the program is already running. If
     * there is an error during the execution of the function, it does not explicitly return anything, so
     * it implicitly returns `undefined`.
     */

        if (code_handler.state.running) {
            console.log('Program allready running');
            code_handler.state.running = false;

            //Replace with reset function later
            code_handler.compile_and_run()
            return false;
        }
        try {
            document.getElementById('console_emulation_space').classList = "console_emulation_space_focus";

            let code_string = code_handler.editor.getValue();

            console.log('compile and run', code_string)
            code_handler.state.running = true;

            //call to server
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

    },
    abort_run: async function () {

    },
    reset_run: async function () {

    },
    clear_screen: async function () {

    }
}
