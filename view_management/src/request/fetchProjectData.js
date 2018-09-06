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


// 创建项目
export const fetchCreateProject = (token, name, describe) => fetch(baseUrl + 'add_project', {
    headers: {"Token": token},
    method: "POST",
    body: JSON.stringify({
      "token":token,
      "name":name,
      "describe":describe,
    }),
    mode: "cors",
    credentials: 'include',
}).then(function (response) {
    return response.json()
});
