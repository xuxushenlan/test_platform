<template>
  <div id="function" index="function">
    <el-menu
      id="navigation"
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item class="logo-title">测试平台</el-menu-item>
      <el-menu-item index="1">项目管理</el-menu-item>
      <el-submenu index="2">
        <template slot="title">接口测试</template>
        <el-menu-item index="testCase">测试用例</el-menu-item>
        <el-menu-item index="testTask">测试任务</el-menu-item>
        <el-menu-item index="testEnv">测试环境</el-menu-item>
        <el-menu-item index="TestTag">TAG管理</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">测试工具</template>
        <el-menu-item index="tools">工具1</el-menu-item>
        <el-menu-item index="3-2">工具2</el-menu-item>
        <el-menu-item index="3-3">工具3</el-menu-item>
      </el-submenu>
      <el-submenu index="personal" id="personalMeun">
        <template slot="title">{{ user }}</template>
        <el-menu-item index="4-1">个人信息</el-menu-item>
        <el-menu-item index="4-2">修改密码</el-menu-item>
        <el-menu-item index="logout">退出</el-menu-item>
      </el-submenu>
    </el-menu>
    <div class="line"></div>
    <div class="BodyTab" v-if="defaultBody===1">
      <div>测试任务管理</div>
      <ProjectList v-if="showProjectList"></ProjectList>
    </div>
    <div class="BodyTab" v-if="defaultBody===2">
      <div>测试用例管理</div>
    </div>
    <div class="BodyTab" v-if="defaultBody===3">
      <div>测试任务管理</div>
    </div>
    <div class="BodyTab" v-if="defaultBody===4">
      <div>测试环境管理</div>
    </div>
    <div class="BodyTab" v-if="defaultBody===5">
      <div>测试标签管理</div>
    </div>
    <div class="BodyTab" v-if="defaultBody===6">
      <div>测试工具1管理</div>
    </div>
  </div>
</template>

<script>

import {fetchGetUsername} from  "../request/fetchPersonal"
import {fetchUserLogout} from  "../request/fetchPersonal"
import ProjectList from "./project/PorjectList"


export default {
  name: 'function',
  components: {
      // 引用子组件
      ProjectList,
    },
  data() {
    return {
      user: "admin@mail.com",
      activeIndex: '1',
      defaultBody: 1,

      showProjectList: false,
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log("key:",key);
      console.log("keyPath",keyPath);

      // 个人中心--退出
      if(key === "logout"){
        let token = this.$store.state.token;
        fetchUserLogout(token).then(data => {
          if ("true" === data.success) {
            this.$store.commit('logout');
            this.$router.push({path: '/login'});
          } else {
            this.$message.error(data.message);
          }
        });
      }
      // 项目管理
      else if(key === "1"){
        this.defaultBody = 1;
        this.showProjectList = true
      }
      // 接口测试--用例管理
      else if(key === "testCase"){
        this.defaultBody = 2;
      }
      // 接口测试--任务管理
      else if(key === "testTask"){
        this.defaultBody = 3;
      }
      // 接口测试--测试环境
      else if(key === "testEnv"){
        this.defaultBody = 4;
      }
      // 接口测试--测试标签
      else if(key === "TestTag"){
        this.defaultBody = 5;
      }
      // 接口测试--测试标签
      else if(key === "tools"){
        this.defaultBody = 6;
      }
    },
    // 获取用户名
    getUserName: function() {
      let token = this.$store.state.token;
      fetchGetUsername(token).then(data => {
          if ("true" === data.success) {
            console.log(data.data);
            this.user = data.data.username;
          } else {
            this.$message.error(data.message);
          }
        });
    }

  },
  created() {
    this.getUserName();
  },
}
</script>

<style>
#function #personalMeun{
  float: right;
}
.BodyTab {
  width: 1200px;
  min-height: 590px;
  border-radius: 1px;
  background-color: #ffffff;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  padding: 20px 40px 40px 40px;
}
.logo-title{
 font-weight: 600;
 font-size: 18px;
}

</style>

