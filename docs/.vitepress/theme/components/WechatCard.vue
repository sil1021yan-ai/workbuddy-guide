<script setup>
import qrImg from "../assets/wechat-qr-yan.jpg";
import wechatImg from "../assets/wechat-wikiai-yan.png";
</script>

<template>
  <div class="wb-wechat-card">
    <img
      class="wb-wechat-card__qr"
      :src="qrImg"
      alt="微信二维码，扫码添加 Yan，备注：WorkBuddy 指南"
      loading="lazy"
    />
    <div class="wb-wechat-card__side">
      <img
        class="wb-wechat-card__id"
        :src="wechatImg"
        alt="微信号 Wikiai_Yan"
        loading="lazy"
      />
      <p class="wb-wechat-card__tip">
        扫不进？微信搜索上方微信号，或把本页截图发到微信里"识别图中二维码"。<br />
        添加时请备注「<b>WorkBuddy 指南</b>」。
      </p>
    </div>
  </div>
</template>

<style scoped>
.wb-wechat-card {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  background: var(--wb-bg-card);
  border: 1.5px solid var(--wb-accent);
  border-radius: 14px;
  padding: 18px 20px;
  margin: 20px 0;
  color: var(--wb-ink);
}

.wb-wechat-card__qr {
  width: 200px;
  max-width: 45%;
  border-radius: 10px;
  border: 1px solid var(--wb-border);
  flex-shrink: 0;
}

.wb-wechat-card__side {
  flex: 1;
  min-width: 200px;
}

.wb-wechat-card__id {
  width: 180px;
  max-width: 100%;
  border-radius: 8px;
  border: 1px solid var(--wb-border);
  margin-bottom: 8px;
}

.wb-wechat-card__tip {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--wb-body);
}

@media (max-width: 640px) {
  .wb-wechat-card {
    flex-direction: column;
    align-items: flex-start;
  }
  .wb-wechat-card__qr {
    max-width: 240px;
  }
}
</style>
