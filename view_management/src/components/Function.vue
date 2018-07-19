<template>
  <div id="function">    
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1">项目管理</el-menu-item>
      <el-submenu index="2">
        <template slot="title">接口测试</template>
        <el-menu-item index="2-1">测试用例1</el-menu-item>
        <el-menu-item index="2-2">测试任务2</el-menu-item>
        <el-menu-item index="2-3">测试环境3</el-menu-item>
        <el-menu-item index="2-3">TAG管理</el-menu-item>
      </el-submenu>  
      <el-submenu index="3">
        <template slot="title">测试工具</template>
        <el-menu-item index="3-1">工具1</el-menu-item>
        <el-menu-item index="3-2">工具2</el-menu-item>
        <el-menu-item index="3-3">工具3</el-menu-item>
      </el-submenu>
      <el-submenu index="4" id="user">
        <template slot="title">{{ user }}</template>
        <el-menu-item index="4-1">个人信息</el-menu-item>
        <el-menu-item index="4-2">修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
    <div class="line"></div>
  </div>
</template>

<script>
export default {
  name: 'function',
  data() {
    return {
      user: "admin@mail.com",
      activeIndex: '1',
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style>
#function #user{
  float: right;
} 
</style>