import { basePath } from "../../config/globalValues";

const baseUrl = basePath + 'personal/';

// Json格式传参
// export const fetchUserLogin = (username, password) => fetch(baseUrl + 'user_login', {
//     method: "POST",
//     body: JSON.stringify({
//         username: username,
//         password: password
//     }),
//     mode: "cors",
//     credentials: 'include',
// }).then(function (response) {
//     return response.json()
// });

// from-data 格式传参
export const fetchUserLogin = (username, password) => {
    let headers = new Headers({
        'Access-Control-Allow-Origin': '*',
    })
    let formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return fetch(baseUrl + 'user_login', {
        method: "POST",
        body: formData,
        headers: {
            'Access-Control-Allow-Origin': '*'
        },
        mode: "cors",
        credentials: 'include',
    }).then(function (response) {
        return response.json()
    });
};