//'node server.js'

const express = require('express');
const app = express();
//const http = require('http');
const fs = require('fs');
const path = require('path');
const port = 1999;//port for the server

const loggerite = {
    get_paths: function () {
        try {
            const timex = new Date();
            const thisfile = path.join(__dirname, `./logs/${timex.getMonth()}-${timex.getFullYear()}/${timex.getMonth()}-${timex.getDate()}.log`);// '/logs/mm-yyyy/mm-dd.log'

            return { thisfile, timex }
        } catch (error) {
            console.error(error);
            return { thisfile: path.join(__dirname, `./logs/default.log`), timex: 0 }
        }
    },
    checkfs: function () {
        // Check and make folders for logs
        console.log('checking log path');
        const log_path = this.get_paths();
        try {
            if (!fs.existsSync(log_path.thisfile)) {
                if (!fs.existsSync(path.dirname(log_path.thisfile))) {
                    console.log('Create: ', path.dirname(log_path.thisfile));
                    fs.mkdirSync(path.dirname(log_path.thisfile), { recursive: true });
                }
                console.log('Create: ', log_path.thisfile);
                fs.writeFileSync(log_path.thisfile, 'Start log\n', { encoding: 'utf8' });
            }
        } catch (error) {
            console.error(error);
        }
        return -1;
    },
    info: async function (datum) {//log happenings
        console.log(datum);
        const log_path = this.get_paths();
        writelog(datum);
        function writelog(datum) {
            try {
                fs.appendFileSync(log_path.thisfile, `${log_path.timex} : ${datum}\n`, { encoding: 'utf8' });
            } catch (error) {

                console.error("Logger Error", error);
                loggerite.checkfs();
                writelog(datum);
            }
        }
    }, error: async function (datum) {//log bad happenings
        console.error(datum);
        const log_path = this.get_paths();
        writelog(datum);
        function writelog(datum) {
            try {
                fs.appendFileSync(log_path.thisfile, `\n****************************************\nError:\n${log_path.timex} :\n${datum}\n******************************************\n\n`, { encoding: 'utf8' });
            } catch (error) {

                console.error("Logger Error", error);
                loggerite.checkfs();
                writelog(datum);
            }
        }
    }
}

async function notfoundpage(response, url) {//404 page goes here
    response.writeHead(404);
    response.write('404 page not , code: ' + url);
    loggerite.info('File not found: ' + url);
}

app.use(express.static('www'))
//app.use('/img', express.static(path.join(__dirname, 'img')))

app.get('/', (request, response) => { startingpoint(response) });//starting point request

app.get('/index.html', (request, response) => { startingpoint(response) });//starting point request

async function startingpoint(response) {//serve index.html
    try {
        response.setHeader('Acess-Control-Allow-Origin', '*');//allow access control from client, this will automatically handle most media files

        response.writeHead(200, { 'Content-type': 'text/html' });//200 ok

        fs.readFile('www/index.html', function (err, databuffer) {
            if (err) {
                loggerite.error(err);
            } else {
                response.write(databuffer);
            }
            response.end();//end response
        });
    } catch (err) {
        loggerite.error('Catastrophy on index: \n' + err);
    }
}

//A test get
app.get('/get/test', (req, res) => {
    // Receive a small amount of test data and send back a response
    try {
        console.log('test get server');
        req.on('data', function (data) {
            console.log('get raw payload: ', data, ' Parsed: ', JSON.parse(data));
            res.end(JSON.stringify({ test: "test get received" }));
        });
        res.writeHead(200, { 'Content-type': 'application/json' });
        res.send(JSON.stringify({ test: 'test get is okay' }));
    } catch (error) {
        console.log('Catastrophy on test get: ', err);
    }
});

//a test post
app.post('/post/test', (req, res) => {
    //receive more data than a get
    loggerite.info('test post to server');
    req.on('data', function (data) {
        loggerite.info('Posted : ' + data + ' Parsed: ' + JSON.parse(data));
        res.end(JSON.stringify({ test: "test post received" }));
    });
});

//a test post
app.post('/post/phonehome', (req, res) => {
    //receive more data than a get
    req.on('data', function (data) {
        loggerite.info('Phoned home: ' + JSON.parse(data).payload);
        res.end(JSON.stringify({ logged: "phone rang" }));
    });
});

app.listen(port, () => { loggerite.info('Running on port ' + port) })//Listen for requests, this starts the server

async function writeresponce(res, filepath) {
    //write files in responses

    try {
        fs.readFile(filepath, function (err, databuffer) {
            if (err) {
                res.writeHead(404);//not okay
                loggerite.error(err);
            } else {
                res.writeHead(200);//200 ok
                res.write(databuffer);
            }
            res.end();//end response
        })
    } catch (error) {
        loggerite.error(error);
    }
}

// prototype json database, just wanted to see if i could do it
let database = {
    initalize: function () {
        loggerite.info('Initalize database');
        try {
            if (!fs.existsSync(path.join(__dirname, './database/'))) {
                loggerite.error("Database does not exist");
                fs.mkdirSync(path.join(__dirname, './database/'));
            }

            if (!fs.existsSync(path.join(__dirname, './database/users.json'))) {
                loggerite.info('Creating users record');
                fs.writeFileSync(path.join(__dirname, './database/users.json'),
                    JSON.stringify({
                        db_version: 0,
                        users: [//test users
                            { uname: "Anthonym", password: "0000" },
                            { uname: "test", password: "0000" }
                        ]
                    })
                );
            }

            if (!fs.existsSync(path.join(__dirname, './database/userdata/'))) {
                loggerite.error('Creating user data directory' + path.join(__dirname, './database/userdata/'));
                fs.mkdirSync(path.join(__dirname, './database/userdata/'));
            }
            loggerite.info("Database check succeded");
        } catch (error) {
            console.log('Startup error, check if node runtime has write permission in ', __dirname);
            console.warn(error);
        }
    },
    cleanup: async function () {
        loggerite.info('CLean up database')
    },
    Create_user: async function (userdetails) {
        console.log('Add new user entry to database :', userdetails);
        /* 
            request Expects format: 
            userdetails = {
                uname:"",
                password:"",
                data:{}//initial data for user
            }
        */

        //!! Need to forbid unwritable characters or convert username with another primary key
        try {
            //check if this user already exists
            let userdata = JSON.parse(fs.readFile(path.join(__dirname, '/database/users.json'), { encoding: 'utf-8' }));

            //!! Improve matching later
            let user_is_found = false;
            for (let iterate in userdata.users) {
                if (userdata.users[iterate].uname == userdetails["uname"]) {
                    user_is_found = true;
                    console.log('Found user at: ', iterate);
                    break;
                }
            }
            if (user_is_found) {
                return false;//user will not be overwritten
            } else {
                //update users record
                userdata.users.push({
                    uname: userdetails.uname,
                    password: userdetails.password,
                });

                userdata.db_version = Number(userdata.db_version) + 1;
                fs.writeFileSync(path.join(__dirname, '/database/users.json'), JSON.stringify(userdata), { encoding: 'utf-8' });

                //create this specific users file
                fs.writeFileSync(path.join(__dirname, './database/userdata/' + userdetails["uname"] + '.json'), JSON.stringify({
                    version: 0,
                    lastupdate: new Date().getTime(),
                    data: userdetails.data || {},//initial data if any
                }));
                return true;//user should now be in database

            }



        } catch (error) {
            console.log('error ', error)
            return false;//handle later
        }


    },
    does_user_exist: async function (username) {
        console.log('Check database for user: ', username);

        let userdata = JSON.parse(fs.readFile(path.join(__dirname, '/database/users.json'), { encoding: 'utf-8' }));
        //check if this user already exists

        for (let iterate in userdata.users) {
            if (userdata.users[iterate].uname == username) {
                console.log('Found user at: ', iterate);
                return true;
            }
        }
        return false;
    }
};

database.initalize();