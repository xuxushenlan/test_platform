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

// 获取项目信息
export const fetchGetProjectInfo = (token, id) => fetch(baseUrl + 'get_project_info', {
    headers: {"Token": token},
    method: "POST",
    body: JSON.stringify({
      "token": token,
      "id": id,
    }),
    mode: "cors",
    credentials: 'include',
}).then(function (response) {
    return response.json()
});

// 保存项目信息
export const fetchUpdateProjectInfo = (token, id, name, describe, status) => fetch(baseUrl + 'update_project', {
    headers: {"Token": token},
    method: "POST",
    body: JSON.stringify({
      "token": token,
      "id": id,
      "name": name,
      "describe": describe,
      "status": status
    }),
    mode: "cors",
    credentials: 'include',
}).then(function (response) {
    return response.json()
});
