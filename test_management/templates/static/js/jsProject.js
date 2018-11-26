var ProjectInit = function (_cmbProject, _cmbModule, defaultProject, defaultModule) {
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var dataList = [];

    //window.alert(defaultProject);
    //window.alert(defaultMudle);
    //设置默认选项
    function cmbSelect(cmb, str) {
        for(var i=0; i< cmb.options.length; i++){
            if(cmb.options[i].value == str){
                cmb.selectedIndex = i;
                return;
            }
        }
    }
    //创建下拉选项
    function cmbAddOption(cmb, str, obj) {
        console.log(str);
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        option.obj = obj;
    }

    //改变模块
    function changeModule() {
        //cmbArea.options.length = 0;
        if (cmbModule.selectedIndex == -1) {
            return;
        }
        var item = cmbModule.options[cmbModule.selectedIndex].obj;
        // 当前选中模块的名称
        console.log("777", cmbModule.options[cmbModule.selectedIndex].value);
        
        // for (var i = 0; i < item.areaList.length; i++) {
        //     cmbAddOption(cmbArea, item.areaList[i], null);
        // }
        //cmbSelect(cmbArea, defaultArea);
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        cmbModule.onchange = null;
        console.log("2222", cmbProject.selectedIndex);
        
        if (cmbProject.selectedIndex == -1) {
            return;
        }
        var item = cmbProject.options[cmbProject.selectedIndex].obj;
        console.log("asdfasdfa", item);
        for (var i = 0; i < item.moduleList.length; i++) {
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
            //$("#result").html(resp);
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