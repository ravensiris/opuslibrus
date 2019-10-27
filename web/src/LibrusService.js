const axios = require('axios').default;

axios.defaults.baseURL = 'http://localhost:5000/api';

export class LibrusService {
    getToken (username, password) {
        const auth = 'Basic ' + Buffer.from(`${username}:${password}`).toString('base64');
        return axios.get('/token/get', {
            headers: {Authorization:auth}
        });
    }

    getTimetable(token, timestamp = ''){
        if (timestamp){
            timestamp = `/${timestamp}`;
        }
        return axios.get(`/timetable/get${timestamp}`,{
            headers:{'X-API-KEY':token}
        });
    }

    checkToken(token){
        if(!token){
            return false;
        }
        return axios.get('/token/check', {
            headers:{'X-API-KEY':token}
        });
    }

}

//let ls = new LibrusService();
/*ls.getToken('6354793u','QLawy123!').then(a => {
console.log(a.data);
}).catch(b => {
console.log(b.response.data);
});
*/
/*const ts = (Date.now() / 1000 | 0) + 3600*24;
console.log(ts);
ls.getTimetable('L35~ee73da969c0375266151fa7ed41efde8', ts).then(a => {
console.log(a.data);
}).catch(b => {
console.log(b.response.data);
});
*/
