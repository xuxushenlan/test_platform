var CaseInit = function (case_id) {
    
    function getCaseInfo() {
        // 调用用例信息接口
        $.post("/interface/get_case_info/", {
            "caseId": case_id,
        }, function (resp) {
            if (resp.success === "true") {
                let caseInfo = resp.data;
                console.log(caseInfo);
                document.querySelector("#req_name").value = caseInfo.name;
                document.querySelector("#req_url").value = caseInfo.url;
                document.querySelector("#req_header").value = caseInfo.header;
                document.querySelector("#req_parameter").value = caseInfo.parameter_body;
                
                document.querySelector("#get").removeAttribute("checked");
                if (caseInfo.method == "post"){
                    document.querySelector("#post").setAttribute("checked", "");
                } else if (caseInfo.method == "put") {
                    document.querySelector("#put").setAttribute("checked", "");
                } else if (caseInfo.method == "delete") {
                    document.querySelector("#delete").setAttribute("checked", "");
                }

                console.log(caseInfo.parameter_type);
                
            }else{
                window.alert(resp.message);
            }
            //$("#result").html(resp);
        });
    }
    // 调用getCaseInfo()函数
    getCaseInfo();

}