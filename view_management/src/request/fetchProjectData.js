const baseUrl = '/api/project/';


// 获取项目列表
export const fetchGetProjectList = (token) => fetch(baseUrl + 'get_projects', {
    headers: {"Token": token},
    method: "POST",
    body: JSON.stringify({"token":token}),
    mode: "cors",
    credentials: 'include',
}).then(function (response) {
    return response.json()
});
