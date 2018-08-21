<template>
  <div id="project">

  </div>
</template>

<script>
  import {fetchGetProjectList} from "../../request/fetchProjectData";


  export default {
    name: "PorjectList.vue",
    props: [],  //组件变量
    components: {
      // 引用组件
    },
    data(){
      // 定义数据
      return{
        ProjectList: "",
      }
    },

    mounted(){
      // 定义初始化动作
      this.getProjectList();
    },

    methods: {
      // 定义方法
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
      }
    }

  }
</script>

<style scoped>

</style>
