<script setup>
import { computed } from "vue";
import qrImg from "../assets/wechat-qr-yan.jpg";

const props = defineProps({
  // 2 / 3 / 4 —— 当前所属篇，用于展示对应单买价
  part: { type: String, default: "2" },
  // banner = 页首紧凑提示条；card = 正文切分处的完整购买卡
  variant: { type: String, default: "card" },
});

const PRICE = {
  "2": { single: "9.9", label: "第二篇 · 实战案例" },
  "3": { single: "19.9", label: "第三篇 · 进阶系统" },
  "4": { single: "29.9", label: "第四篇 · 岗位与行业" },
};

const current = computed(() => PRICE[props.part] ?? PRICE["2"]);
const isBanner = computed(() => props.variant === "banner");
</script>

<template>
  <!-- 页首紧凑提示条 -->
  <div v-if="isBanner" class="wb-pay wb-pay--banner">
    <span class="wb-pay__badge">试读版</span>
    <span class="wb-pay__banner-text">
      本篇为试读内容，完整版（含全部真实提示词、执行步骤表、验收标准）为付费飞书文档，密码解锁后在线阅读。
    </span>
    <a class="wb-pay__banner-link" href="/workbuddy-guide/bluebook/购买指南/">
      查看定价与购买方式 →
    </a>
  </div>

  <!-- 正文切分处完整购买卡 -->
  <div v-else class="wb-pay">
    <div class="wb-pay__head">
      <span class="wb-pay__badge">试读到此结束</span>
      <span class="wb-pay__title">完整版 · 飞书付费文档（密码解锁）</span>
    </div>

    <p class="wb-pay__lead">
      你刚才看到的是本章的<b>思路框架</b>。付费完整版还包含：
    </p>

    <ul class="wb-pay__list">
      <li>2–3 条<b>可直接复制</b>的真实提示词（含【】占位符说明）</li>
      <li><b>执行步骤表</b>：AI 做什么、你要确认什么</li>
      <li><b>实际效果 + 验收标准</b>：怎么判断"做完了、做对了"</li>
      <li><b>零成本 Skill 固化示范</b>：把这类活变成你的专属技能</li>
      <li><b>买断后免费更新</b>：修订直接发生在飞书文档里，打开永远是最新版</li>
    </ul>

    <div class="wb-pay__pricing">
      <div class="wb-pay__price-row">
        <span class="wb-pay__price-label">单篇买断</span>
        <span class="wb-pay__price-value">¥{{ current.single }}</span>
      </div>
      <div class="wb-pay__upgrade">
        <p><b>补差升级规则（脑洞剧分集价）：</b></p>
        <ul>
          <li>第二篇单买 ¥9.9；第三篇单买 ¥19.9（已购第二篇只补 ¥10）；</li>
          <li>第四篇 ¥29.9 = <b>全套锚定价</b>，已购任意一篇补差即可解锁全部：</li>
          <li>已购第二篇补 ¥20，已购第二、三篇补 ¥10。</li>
        </ul>
      </div>
    </div>

    <div class="wb-pay__buy">
      <img
        class="wb-pay__wechat-img"
        :src="qrImg"
        alt="微信二维码，扫码添加 Yan，备注 WorkBuddy 指南"
        loading="lazy"
      />
      <div class="wb-pay__buy-steps">
        <p><b>购买流程（1 分钟）：</b></p>
        <ol>
          <li>微信扫描/识别上方二维码添加好友（或搜索 <code>Wikiai_Yan</code>）；</li>
          <li>备注「WorkBuddy 指南」并告诉我要哪一篇；</li>
          <li>微信转账对应金额 → 我把<b>飞书文档链接 + 访问密码</b>发给你，打开链接输入密码即可在线阅读完整版（手机、电脑都能看，无需注册飞书）。</li>
        </ol>
      </div>
    </div>

    <p class="wb-pay__note">
      已购过一篇想升级？同样加微信报「已购第 X 篇」，按上表补差价即可，升级内容 =
      新一篇的链接和密码。
      更多细节见<a href="/workbuddy-guide/bluebook/购买指南/">购买指南</a>。
    </p>
  </div>
</template>

<style scoped>
.wb-pay {
  background: var(--wb-bg-card);
  border: 1.5px solid var(--wb-accent);
  border-radius: 14px;
  padding: 20px 22px;
  margin: 28px 0;
  color: var(--wb-ink);
  line-height: 1.7;
}

.wb-pay__head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.wb-pay__badge {
  display: inline-block;
  background: var(--wb-accent);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  padding: 2px 10px;
  border-radius: 999px;
  white-space: nowrap;
}

.wb-pay__title {
  font-weight: 700;
  font-size: 16px;
}

.wb-pay__lead {
  margin: 6px 0 10px;
  color: var(--wb-body);
}

.wb-pay__list {
  margin: 0 0 14px;
  padding-left: 20px;
  color: var(--wb-body);
}

.wb-pay__list li {
  margin: 4px 0;
}

.wb-pay__pricing {
  background: var(--wb-bg-alt);
  border-radius: 10px;
  padding: 12px 16px;
  margin-bottom: 14px;
}

.wb-pay__price-row {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 6px;
}

.wb-pay__price-label {
  font-size: 14px;
  color: var(--wb-muted);
}

.wb-pay__price-value {
  font-size: 26px;
  font-weight: 800;
  color: var(--wb-accent);
}

.wb-pay__upgrade {
  font-size: 13.5px;
  color: var(--wb-body);
}

.wb-pay__upgrade p {
  margin: 4px 0;
}

.wb-pay__upgrade ul {
  margin: 0;
  padding-left: 18px;
}

.wb-pay__buy {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  flex-wrap: wrap;
}

.wb-pay__wechat-img {
  width: 220px;
  max-width: 100%;
  border-radius: 10px;
  border: 1px solid var(--wb-border);
  flex-shrink: 0;
}

.wb-pay__buy-steps {
  flex: 1;
  min-width: 220px;
  font-size: 14px;
  color: var(--wb-body);
}

.wb-pay__buy-steps p {
  margin: 4px 0;
}

.wb-pay__buy-steps ol {
  margin: 0;
  padding-left: 18px;
}

.wb-pay__buy-steps li {
  margin: 4px 0;
}

.wb-pay__note {
  margin: 12px 0 0;
  font-size: 13px;
  color: var(--wb-muted);
}

.wb-pay__note a,
.wb-pay__banner-link {
  color: var(--wb-accent);
  font-weight: 600;
}

/* 页首紧凑提示条 */
.wb-pay--banner {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  padding: 10px 14px;
  margin: 0 0 20px;
  font-size: 14px;
}

.wb-pay__banner-text {
  color: var(--wb-body);
  flex: 1;
  min-width: 200px;
}

@media (max-width: 640px) {
  .wb-pay__buy {
    flex-direction: column;
  }
}
</style>
