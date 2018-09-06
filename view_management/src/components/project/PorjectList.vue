<!--接口测试：项目管理
/**
* @module views
* @desc 项目管理列表
* @author bugmaster
* @date 2018年8月22日
*/
-->
<template>
  <div id="project">
    <div class="title-main">
      <el-button type="info" @click="createProject">创建</el-button>
    </div>

    <el-table :data="tableData" border style="width: 100%;">
      <el-table-column prop="name" label="名称" width="180"></el-table-column>
      <el-table-column prop="describe" label="描述" width="280"></el-table-column>
      <el-table-column prop="status" label="状态" width="100"></el-table-column>

      <el-table-column fixed="right" label="操作">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          <el-button type="text" size="small">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 创建项目 -->
    <CreateProjectTag v-if="showCreateProject" v-on:onCancelClick="closeCreateProject" v-on:onSaveClick="saveCreateProject"></CreateProjectTag>

  </div>

</template>

<script>
  import {fetchGetProjectList} from "../../request/fetchProjectData";
  import CreateProject from "./CreateProject"

  export default {
    name: "ProjectList",
    props: [],  //组件变量
    components: {
      // 引用组件
      CreateProjectTag: CreateProject
    },
    data(){
      // 定义数据
      return{
        ProjectList: "",
        tableData: [],

        showCreateProject: false,
      }
    },

    mounted(){
      // 定义初始化动作
      this.getProjectList();
    },

    methods: {
      // 获取项目列表
      getProjectList: function() {
        this.tableData = [];
        let token = this.$store.state.token;
        fetchGetProjectList(token).then(resp => {
          if ("true" === resp.success) {
            let result = resp.data;
            for(let i=0; i< result.length; i++){
              if (result[i].status === true){
                 result[i].status = "开启";
              }else{
                result[i].status = "禁用";
              }
              this.tableData.push(result[i]);
            }
          } else {
            this.$message.error(resp.message);
          }
        });
      },
      //创建项目
      createProject: function () {
        this.showCreateProject = true;
        //$('body').css('overflow', 'auto');
      },
      //取消创建项目
      closeCreateProject: function() {
        this.showCreateProject = false;
      },
      //创建项目成功
      saveCreateProject: function() {
        this.showCreateProject = false;
        this.getProjectList();
      },
      //点击查看
      handleClick(row) {
        console.log(row);
      }
    }

  }
</script>

<style>
  .cell{
    text-align: center;
  }
</style>
<style scoped>
  .title-main {
    float: left;
    height: 50px;
  }

</style>
