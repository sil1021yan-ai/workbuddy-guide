<script setup>
import wechatImg from "../assets/wechat-wikiai-yan.png";
</script>

<template>
  <img
    class="wb-wechat-card"
    :src="wechatImg"
    alt="微信号 Wikiai_Yan，添加时备注：WorkBuddy 指南"
    loading="lazy"
  />
</template>

<style scoped>
.wb-wechat-card {
  width: 320px;
  max-width: 100%;
  border-radius: 12px;
  border: 1px solid var(--wb-border);
}
</style>
