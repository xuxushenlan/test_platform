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

  <el-table :data="tableData" style="width: 100%;">
    <el-table-column prop="date" label="日期" width="180"></el-table-column>
    <el-table-column prop="name" label="姓名" width="180"></el-table-column>
    <el-table-column prop="address" label="地址"></el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
        <el-button type="text" size="small">编辑</el-button>
      </template>
    </el-table-column>
  </el-table>
  </div>
</template>

<script>
  import {fetchGetProjectList} from "../../request/fetchProjectData";


  export default {
    name: "PorjectList",
    props: [],  //组件变量
    components: {
      // 引用组件
    },
    data(){
      // 定义数据
      return{
        ProjectList: "",
        tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
      }
    },

    mounted(){
      // 定义初始化动作
      this.getProjectList();
    },

    methods: {
      // 获取项目列表
      getProjectList: function() {
        let token = this.$store.state.token;
        fetchGetProjectList(token).then(resp => {
          if ("true" === resp.success) {
            //this.$message.success("已删除上传的接口文件");
            console.log(resp.data);
          } else {
            this.$message.error(resp.message);
          }
        });
      },
      // 点击查看
      handleClick(row) {
        console.log(row);
      }
    }

  }
</script>

<style scoped>

</style>
