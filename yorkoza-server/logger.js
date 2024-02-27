const fs = require('fs');
const path = require('path');

const loggerite = {
    get_paths: function () {//Paths for logs are generated 
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

module.exports = loggerite;