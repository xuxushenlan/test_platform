<!--接口测试：创建项目列表
/**
* @module views
* @desc 项目管理列表
* @author bugmaster
* @date 2018年8月22日
*/
-->
<template>
  <div class="layout-shade" @keyup.esc="CancelCreateModal" tabindex="10" id="createTag">
    <div class="create-body">
      <div class="main-title">创建项目</div>
      <div class="main-line"></div>
    </div>

    <div class="layout-box">
      <div class="main-option">
        <div class="main-dec">
          * 项目名称
        </div>
        <el-input v-model="name" placeholder="输入项目名称" style="margin-top: 10px"></el-input>
      </div>
      <div class="main-option">
        <div class="main-dec">
          * 项目描述
        </div>
        <el-input type="textarea" :rows="3" placeholder="请项目描述" v-model="describe"></el-input>
      </div>

      <div class="main-create-confirm">
        <el-button style="margin-left: 220px;" @click="cancelCreate">取消</el-button>
        <el-button type="info" @click="saveCreate">保存</el-button>
      </div>
      <div class="end-height"></div>
    </div>

  </div>
</template>

<script>
  import {fetchCreateProject} from "../../request/fetchProjectData"


  export default {
      name: "CreateTag",
      data(){
        return{
          name: '',
          describe: '',

        }
      },
      methods:{
        // 取消创建
        cancelCreate: function(){
          this.$emit('onCancelClick', {});
        },
        //保存创建
        saveCreate: function(){
          if(this.name === ""){
              this.$message.error("请输入项目名称");
          }else if(this.describe === ""){
              this.$message.error("请输入项目描述");
          }
          // 打开loading
          const loading = this.$loading({fullscreen: true});
          let token = this.$store.state.token;
          fetchCreateProject(token, this.name, this.describe).then(resp => {
             if (resp.success === "true") {
               this.$message.success("创建成功");
               this.$emit('onSaveClick', {});
             }else{
               this.$message.error(resp.message);
             }
             loading.close();
          })

        },

      },
      mounted(){
        document.getElementById("createTag").focus();
      }

    }
</script>

<style scoped>

  .layout-shade {
    /*width: 1440px;*/
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1001;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    overflow-y: auto;
    color: white;
  }
  .layout-box {
    width: 500px;
    height: auto;
    border-radius: 2px;
    background-color: #ffffff;
    margin: 0 auto;
    margin-top: -30px;
  }
  .create-body {
    width: 500px;
    border-radius: 2px;
    background-color: #ffffff;
    margin-left: auto;
    margin-right: auto;
    margin-top: 110px;
    padding: 23px 0 36px 0;
  }

  .main-title {
    width: 120px;
    height: 28px;
    font-family: PingFangSC;
    font-size: 20px;
    font-weight: 600;
    text-align: center;
    color: #333333;
  }

  .main-line {
    margin-top: 5px;
    width: 500px;
    height: 16px;
    background-color: #ffffff;
    box-shadow: inset 0 -1px 0 0 #e0e0e0;
  }

  .main-option {
    width: 360px;
    margin-right: auto;
    margin-left: auto;
    margin-top: 24px;
  }

  .main-dec {
    height: 17px;
    font-family: Helvetica;
    font-size: 14px;
    text-align: left;
    color: #333333;
    margin-bottom: 8px;
  }

  .main-create-confirm {
    width: 360px;
    margin-right: auto;
    margin-left: auto;
    margin-top: 24px;
    display: flex;
    justify-content: space-between;
  }

  .end-height {
    height: 40px;
    margin-bottom: 70px;
  }
</style>
