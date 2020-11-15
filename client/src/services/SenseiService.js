// https://stackoverflow.com/questions/41164672/whats-the-equivalent-of-angular-service-in-vuejs/54165192#54165192
// https://www.qcode.in/api-error-handling-in-vue-with-axios/

import axios from 'axios';

let baseUrl = "http://localhost:5000/sensei/api/v1";
let axiosInstance = null;

export default new class {
    
    constructor(){
        axiosInstance = axios.create({
            baseURL: baseUrl,            
            headers: { 'Content-Type': 'application/json' }  
        });
    }

    //#region Students
    getStudents(){
        return axiosInstance("/students");
    }

    getStudents(id){
        return axiosInstance(`/students/${id}`);
    }

    saveStudent(item){
        return axiosInstance.post("/students", item);
    }
    //#endregion

    //#region Authenticate
    authenticate(creds){
        return axiosInstance.post("/authenticate", creds);
    }
    ////#endregion

 }