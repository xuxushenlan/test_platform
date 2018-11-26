var ProjectInit = function (_cmbProject, _cmbModule, defaultProject, defaultModule) {
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var dataList = [];

    var pro_name = "";
    var mod_name = "";

    //设置默认选项
    function cmbSelect(cmb, str) {
        for(let i=0; i< cmb.options.length; i++){
            if(cmb.options[i].value === str){
                cmb.selectedIndex = i;
                return;
            }
        }
    }
    //创建下拉选项
    function cmbAddOption(cmb, str, obj) {
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        option.obj = obj;
    }

    //改变模块
    function changeModule() {
        if (cmbModule.selectedIndex === -1) {
            return;
        }
        // 当前选中模块的名称
        mod_name = cmbModule.options[cmbModule.selectedIndex].value;
        console.log("模块名称：", mod_name);
        console.log("项目名称：", pro_name);

        // 获取某模块的用例列表接口
        $.post("/interface/get_case_list/", {
            "pName": pro_name,
            "mName": mod_name,
        }, function (resp) {
            if (resp.success === "true") {
                console.log(resp.data);
            }else{
                window.alert(resp.message);
            }
        });
        
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        cmbModule.onchange = null;
        
        if (cmbProject.selectedIndex === -1) {
            return;
        }
        pro_name = cmbProject.options[cmbProject.selectedIndex].value;

        let item = cmbProject.options[cmbProject.selectedIndex].obj;
        for (let i = 0; i < item.moduleList.length; i++) {
            cmbAddOption(cmbModule, item.moduleList[i], null);
        }

        cmbSelect(cmbModule, defaultModule);
        changeModule();
        cmbModule.onchange = changeModule;
    }

    function getProjectList(){
        // 调用项目服务列表接口
        $.get("/interface/get_project_list", {}, function (resp) {
            if(resp.success === "true"){
                dataList = resp.data;
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i].name, dataList[i]);
                }

                cmbSelect(cmbProject, defaultProject);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            cmbSelect(cmbProject, defaultProject);

        });
    }
    // 调用getProjectList函数
    getProjectList(); 
    
};

// 数据格式
// var dataList = [{
//     name: '项目AAAA',
//     moduleList: [
//         "模块a", "模块b", "模块c"
//     ]
// },
// {
//     name: '项目BBB',
//     moduleList: [
//         "模块1", "模块2", "模块3"
//     ]
// }
// ]