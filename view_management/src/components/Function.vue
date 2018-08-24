<template>
  <div id="function" index="function">
    <el-menu
      id="navigation" :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
      @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
      <el-menu-item index="0" class="logo-title">测试平台</el-menu-item>
      <el-menu-item index="1">项目管理</el-menu-item>
      <el-menu-item index="2">接口管理</el-menu-item>
      <el-menu-item index="3">测试工具</el-menu-item>
      <el-submenu index="personal" id="personalMeun">
        <template slot="title">{{ user }}</template>
        <el-menu-item index="4-1">个人信息</el-menu-item>
        <el-menu-item index="4-2">修改密码</el-menu-item>
        <el-menu-item index="logout">退出</el-menu-item>
      </el-submenu>
    </el-menu>
    <div class="line"></div>

    <!--项目管理 -->
    <div class="secondary-menu" v-if="defaultBody===1">
      <el-menu default-active="2" class="el-menu-vertical-demo"
               style="height: 700px">
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">项目</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-document"></i>
        <span slot="title">模块</span>
      </el-menu-item>
    </el-menu>
    </div>

    <!-- 用例管理 -->
    <div class="secondary-menu" v-else-if="defaultBody===2">
      <el-menu default-active="2" class="el-menu-vertical-demo"
               style="height: 700px">
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">用例</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-document"></i>
        <span slot="title">任务</span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-document"></i>
        <span slot="title">环境</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-document"></i>
        <span slot="title">标签</span>
      </el-menu-item>
    </el-menu>
    </div>

    <!-- 测试工具 -->
    <div class="secondary-menu" v-else-if="defaultBody===3">
      <el-menu default-active="2" class="el-menu-vertical-demo"
               style="height: 700px">
        <el-menu-item index="1">
          <i class="el-icon-menu"></i>
          <span slot="title">工具1</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-document"></i>
          <span slot="title">工具2</span>
        </el-menu-item>
      </el-menu>
    </div>

    <div class="BodyTab" v-if="defaultBody===1">
      <div>项目管理</div>
      <ProjectList></ProjectList>
    </div>
    <div class="BodyTab" v-if="defaultBody===2">
      <div>测试用例</div>
    </div>
    <div class="BodyTab" v-if="defaultBody===3">
      <div>测试工具</div>
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
      // 接口测试
      else if(key === "2"){
        this.defaultBody = 2;
      }
      // 测试工具
      else if(key === "3"){
        this.defaultBody = 3;
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

.secondary-menu{
  width: 220px;
  height: 800px;
  float: left;
 }
.BodyTab {
  float: left;
  width: 1000px;
  min-height: 590px;
  border-radius: 1px;
  /*background-color: red;*/
  /*background-color: #F5F5F5;*/
  margin-right: auto;
  margin-top: 20px;
  padding: 10px 40px 40px 40px;
  margin-left: 10px;
}
.logo-title{
 font-weight: 600;
 font-size: 18px;
}

</style>

