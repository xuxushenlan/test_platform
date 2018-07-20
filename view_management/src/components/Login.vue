<template>
  <div class="login">
      <h1>测试平台</h1>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" class="demo-ruleForm">
    <div class="main-login-input">
        <el-form-item prop="username">
            <el-input placeholder="请输账号" v-model="ruleForm.username">
                <template slot="prepend">账号</template>
            </el-input>
        </el-form-item>
    </div>
    <div class="main-login-input">
        <el-form-item prop="password">
            <el-input placeholder="请输入密码" type="password"v-model="ruleForm.password">
                <template slot="prepend">密码</template>
            </el-input>
        </el-form-item>
    </div>
    <div class="main-login-button">
        <el-button id="loginButton" type="info" @click="submitForm('ruleForm')">登录</el-button>
    </div>
    </el-form>
  </div>
</template>

<script>

import {fetchUserLogin} from  "../request/fetchPersonal"

export default {
  name: 'login',
  data () {
    return {
        ruleForm: {
            username: 'test@mail.com',
            password: 'test123456',
        },
        rules: {
            username: [
                {required: true, message: '请输入账号', trigger: 'blur'},
            ],
            password: [
                {required: true, message: '请输入密码', trigger: 'blur'},
            ],
        }
    }
  },
  methods: {
      // 表单验证
    submitForm(formName) {
        this.$refs[formName].validate((valid) => {
            if (valid) {
            this.loginSubmit();
          }
        });
    },
    // 执行登录
    loginSubmit: function(){
        const loading = this.$loading({
          fullscreen: true,
        });
        console.log("用户名", this.ruleForm.username);
        console.log("密码", this.ruleForm.password);
         // 保存上传的文件
        fetchUserLogin(this.ruleForm.username, this.ruleForm.password).then(data => {
          if ("true" === data.success) {
            let result = data.data;
            console.log(result.Token);
            this.$store.commit('login', result.Token);
            this.$router.push({path: '/function'});
            console.log('wtf', this.$route.query.redirect);
            this.$router.push(this.$route.query.redirect || '/function');
            loading.close();
          } else {
            loading.close();
            this.$message.error(data.message);
          }
        });
      },
  },
  mounted() {

  },

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
