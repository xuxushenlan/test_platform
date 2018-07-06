<template>
  <div class="login">
    <div class="main-login-input">
        <el-input placeholder="请输账号" v-model="username">
            <template slot="prepend">账号</template>
        </el-input>
    </div>
    <div class="main-login-input">
        <el-input placeholder="请输入密码" v-model="password">
            <template slot="prepend">密码</template>
        </el-input>
    </div>
    <div class="main-login-button">
        <el-button id="loginButton" type="primary">登录</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
        username: '',
        password: '',
    }
  }
}
</script>

<!-- element-ui style -->
<style>
.login #loginButton{
    width: 300px;
    height: auto;
}
</style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login{
    width: 300px;
    text-align:center;
    margin-left:auto;
    margin-right:auto;
}
.main-login-input{
    margin-top: 5px;
    margin-bottom: 10px;
}


h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
